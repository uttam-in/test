from django.urls import path
from account.controller import accountview
from account import views
from account.controller import accountview
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("register", accountview.Register.as_view(), name='register'),
    path("login", accountview.Login.as_view(), name='login'),
    path("addpatient", accountview.AddPatient.as_view(), name='addpatient'),
    path("listpatient", accountview.ListPatient.as_view(), name='listpatient'),
    path("updateprofile", accountview.UpdateProfile.as_view(), name='updateprofile'),
    path("selectlanguages", accountview.SelectLanguages.as_view(), name='selectlanguages'),

    ]