from bankaccounts import views
from django.urls import path

app_name="bankaccounts"
urlpatterns=[
    path('',views.kyc_reg),
    path("account/",views.account,name="accountpage"),
    path("dashboard/",views.kyc_reg,name='dashboard'),
    path("newdashboard/",views.dashboard,name='newdashboard'),
    # path("creditcard/",views.creditcard,name="creditcard")
]