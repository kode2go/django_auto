# Django Auto

Ever wanted to get up and running with Django quickly without having to do the same initial steps each time!
Well this is Django Auto. A few simple scripts that automate the fundamental setup of Django so you can get
to what you really want to do with Django!

## Changes
dj_1:
- baseline

dj_2:
- Manual process of writing to urls.py and views.py:
-- Create url links in script for urls.py
-- Add view functions views.py file
- Copied all templates and static to app folders


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

## Postmark Setup:

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

## SendGrid Setup:

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


