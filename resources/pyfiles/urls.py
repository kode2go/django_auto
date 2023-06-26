from django.urls import path
from . import views
from .views import PersonListView

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', PersonListView.as_view(), name='person-list'),
]

urlpatterns += [
    path('login/', views.login_view, name='login'),
]

urlpatterns += [
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += [
    path('register/', views.register_view, name='register'),
]

urlpatterns += [
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]

urlpatterns += [
    path('tables/', views.tables, name='tables'),
]

urlpatterns += [
    path('charts/', views.charts, name='charts'),
]

urlpatterns += [
    path('error_404/', views.error_404, name='error_404'),
]

urlpatterns += [
    path('blank/', views.blank, name='blank'),
]

urlpatterns += [
    path('update_person/', views.update_person, name='profile'),
]
