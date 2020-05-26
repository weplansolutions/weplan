from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('index.html',views.index),
    path('success', views.client),
    path('getdetails',views.registered),
    path('eiplans.html',views.eiplans),
    path('internships.html',views.internship),
    path('seminars.html',views.seminar),
    path('workshops.html',views.workshop),
    path('sciencefair.html',views.sciencefair),
    path('login.html',views.login),
    path('loginchoose.html',views.loginchoose),
    path('login',views.logindata),
    path('collaborations.html',views.collab),
    path('about.html',views.about),
    path('ourteam.html',views.ourteam),
    path('careers.html',views.careers),
    path('terms&conditions.html',views.terms),
    path('contact.html',views.contact),
    path('analysis.html',views.check),
    path('registration.html',views.registration),
    path('institutionlogin.html',views.institution),
]