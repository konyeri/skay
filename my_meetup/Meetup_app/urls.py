from django.urls import path
from . import views
from .views import MeetupUpdate, MeetupDelete, MeetupCreate
from django.contrib.auth.views import LogoutView


urlpatterns=[
   # path('', views.index, name='home'),
    path('', views.home, name='home'),
    #path('contact/', views.contact, name='contact')
    path('logout/',  LogoutView.as_view(next_page='home'), name='logout' ),
    path('login', views.loginPage, name='login'),
    path('create-meetup', MeetupCreate.as_view(), name='create-meetup'),
    path('meetup/success', views.comfirm_registration, name='comfirm-registration'),
    path('upcoming-meetups', views.upcoming_meetups, name='upcoming-meetups'),
    path('meetup/<slug:slug>', views.meetup_details, name='meetup-details'),
    path('register/', views.register, name='register'), 
    path('add-speaker/<slug:slug>', views.add_speaker, name='add-speaker'),
    path('user-meetups/<int:pk>', views.user_meetups, name='user-meetups'),
    
   
    path('meetup-update/<int:pk>', MeetupUpdate.as_view(), name='meetup-update'),
    
    path('meetup-delete/<int:pk>', MeetupDelete.as_view(), name='meetup-delete')

]
