from accounts import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
   path("",views.sign_up,name="register"),
   path("register/",views.sign_in,name="signup"),
   path("sigin/",views.dashboard,name="dashboard"),
   path("userlogout/",views.user_logout,name="userlogout"),
]