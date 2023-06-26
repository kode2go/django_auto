# Django Automation

```
#!/bin/bash

# Prompt for project name
read -p "Enter project name: " project_name

# Create Django project
django-admin startproject $project_name

# Move into the project directory
cd $project_name

python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '1@1.com', 'admin')" | python manage.py shell

python manage.py startapp app

# Update settings.py file
echo -e "\nINSTALLED_APPS.append('app')" >> $project_name/settings.py

# Create urls.py file in app folder
echo -e "from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path('', views.index, name='index'),\n]" > app/urls.py

# Create views.py file in app folder
echo -e "from django.shortcuts import render\n\n\ndef index(request):\n    context = {}\n    return render(request, 'index.html', context)" > app/views.py

# Update urls.py file
echo -e "\nfrom django.urls import include\n\nurlpatterns += [\n    path('', include('app.urls')),\n]" >> $project_name/urls.py

awk '/"DIRS":/ {$0 = "        \"DIRS\": [os.path.join(BASE_DIR, \x27templates\x27)],"} 1' $project_name/settings.py > $project_name/temp.py && mv $project_name/temp.py $project_name/settings.py

awk '/from pathlib import Path/ {print; print "import os"; next} 1' $project_name/settings.py > $project_name/temp.py && mv $project_name/temp.py $project_name/settings.py

mkdir -p app/templates/
echo "<p>Test Project</p>" > app/templates/index.html
```


## Changes
dj_2:
- Copied all templates and static to app folders
- Create url links in script for urls.py
- Add view functions views.py file

dj_3:
- Created pyfiles folder, and copy that to app/ directory
- Updated script to move url patterns to urls.py file instead

dj_4: 
- Added dummy person
- Added requirements file
- Added DRF
- Added serializers.py
- Updated views.py and urls.py for API

pyfiles updates:
Goal was to setup mail server:
- send email notification once person logs in
- used same domain to make testing easier
- many options explored, Postmark was the easiest, then SendGrid
- SendGrid verification took a day, Postmark was immediate
- Update view.py with send_email_verification on login

Postmark Setup:

https://postmarkapp.com/send-email/python

```
pip install postmarker
```

```
from postmarker.core import PostmarkClient
postmark = PostmarkClient(server_token='API TOKEN')
postmark.emails.send(
  From='email@registered_domain.co.za',
  To='email@gmail.com',
  Subject='Postmark test',
  HtmlBody='HTML body goes here'
)

```

SendGrid code:

From their site, it seems you need to setup the keys like this:

```
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

Then:

```
pip install sendgrid
```

Then the example code:

```
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='mail@gmail.com',
    to_emails='mail@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
``


