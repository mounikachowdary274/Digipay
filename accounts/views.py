from django.shortcuts import render,redirect
from accounts.forms import user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from bankaccounts.forms import KYC_form
from django.contrib import messages
from bankaccounts.models import Account
from bankaccounts.models import KYC

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully.")
    else:
        form = user_form()
    return render(request,"account/register.html",{'form':form})

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # user = User.objects.get(email=email)
            user = authenticate(username=username, password=password)
            print(user)
            if user: # if there is a user
                login(request, user)
                messages.success(request, "You are logged.")
                return redirect("bankaccounts:accountpage")
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect("accounts:signup")
        except:
            messages.warning(request, "User does not exist")
    return render(request,"account/signin.html")

def dashboard(request):
    return render(request,"account/dashboard.html",{})
def user_logout(request):
    logout(request)
    return redirect("accounts:signup")


# def account(request):
#     user=request.user
#     account=Account.objects.get(user=user)
#     try:
#         kyc=KYC.objects.get(user=user)
#     except:
#         kyc=None
#     if request.method=="POST":
#         form=KYC_form(request.POST,request.FILES,instance=kyc)
#         if form.is_valid():
#             new_form=form.save(commit=False)
#             new_form.user=user
#             new_form.account=account
#             new_form.save()
#             messages.success(request,'Kyc form submitted successfully,In review ')
#             return redirect('accounts:dashboard')
#     else:
#         form=KYC_form(instance=kyc)
#     context={ 
#         "account":account,
#         "form":form,
#         "kyc":kyc,
#     }
#     return render(request,"account/account.html",context)