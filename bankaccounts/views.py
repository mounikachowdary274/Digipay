from django.shortcuts import render,redirect
from bankaccounts.forms import KYC_form
from django.contrib import messages
from bankaccounts.models import Account
from bankaccounts.models import KYC
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction
from accounts.models import user_profile
from transactions.forms import Creditcard_Form
from transactions.models import Credit_Card
 
# Create your views here.
@login_required(login_url="signup")
def account(request):
    kyc=KYC.objects.get(user=request.user)
    account=Account.objects.get(user=request.user)
    context={
        'kyc':kyc,
        'account':account
    }
    return render(request,"account/account.html",context)

@login_required(login_url="signup")
def kyc_reg(request):
    user=request.user
    account=Account.objects.get(user=user)
    try:
        kyc=KYC.objects.get(user=user)
    except:
        kyc=None
    if request.method=="POST":
        form=KYC_form(request.POST,request.FILES,instance=kyc)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=user
            new_form.account=account
            new_form.save()
            messages.success(request,'Kyc form submitted successfully,In review ')
            return redirect('accounts:dashboard')
    else:
        form=KYC_form(instance=kyc)
    context={ 
        "account":account,
        "form":form,
        "kyc":kyc,
    }
    return render(request,'partials/kyc_form.html',context)

@login_required(login_url="signup")
def dashboard(request):
    user=request.user
    account=Account.objects.get(user=user)
    transaction=Transaction.objects.all()
    kyc=KYC.objects.get(user=user) 
    credit_card=Credit_Card.objects.all()
    if request.method=="POST":
       form=Creditcard_Form(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=Creditcard_Form()
    context={
           'account':account,
            'kyc':kyc,
            'transaction':transaction,
            'form':form ,
            'credit_card':credit_card    
    }
    return render(request,'account/dashboard.html',context)
# def creditcard(request):
#     form=Creditcard_Form()
#     return render(request,'account/creditcard.html',{'form':form})