from transactions.models import Credit_Card
from django.shortcuts import render
from bankaccounts.models import Account,KYC
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import DeleteView

def credit_card_detail(request,number,account_number):
    user=request.user
    account=Account.objects.get(account_number=account_number)
    kyc=KYC.objects.get(user=user)
    credit=Credit_Card.objects.get(number=number)
    context={
        'account':account,
        'kyc':kyc,
        'credit':credit
    }
    return render(request,'account/creditcard-detail.html',context)

def credit_card_bill(request,card_id):
    user=request.user
    credit_card_bil=Credit_Card.objects.get(card_id=card_id)
    account=Account.objects.get(user=user)
    kyc=KYC.objects.get(user=user)
    if request.method=="POST":
            amount=request.POST.get("amount-send")
            print(amount)
            print(type(amount))
            if account.account_balance <=0 or account.account_balance<int(amount):
                messages.warning(request,'Insufficient Funds ,Fund you account and tryagain')
            else:
                account.account_balance-=int(amount)
                account.save()

                credit_card_bil.card_amount+=int(amount)
                credit_card_bil.save()

                messages.success(request,f"Payed Bill to {account.user.kyc.full_name} was successfull")
                return redirect("transactions:credit_card_detail",credit_card_bil.number,account.account_number)
    context={
        'credit_card_bil':credit_card_bil,
        'kyc':kyc,
        'account':account
    }
    return render(request,'account/credit_card_bill.html',context)
def withdraw_amount(request,card_id):
    user=request.user
    withdraw=Credit_Card.objects.get(card_id=card_id)
    account=Account.objects.get(user=user)
    if request.method=="POST":
            amount=request.POST.get("amount-send")
            if withdraw.card_amount <=0 or withdraw.card_amount<int(amount):
                messages.warning(request,'Insufficient Funds ,Fund you account and tryagain')
            else:
                withdraw.card_amount-=int(amount)
                withdraw.save()

                account.account_balance+=int(amount)
                account.save()

                messages.success(request,f"Withdrawed amount from {account.user.kyc.full_name} account was successfull")
                return redirect("transactions:credit_card_detail",withdraw.number,account.account_number)
    context={
        'withdraw':withdraw,
        'account':account
    }
    return render(request,'account/withdraw_amount.html',context)

def delete_card(request,card_id):
    user=request.user
    card_delete_details=Credit_Card.objects.get(card_id=card_id)
    account=Account.objects.get(user=user)
    if request.method=="POST":
          if card_delete_details.card_amount>0:
               account.account_balance+=card_delete_details.card_amount
               account.save()
               card_delete_details.delete()
          else:
               card_delete_details.delete()
          return redirect("bankaccounts:newdashboard")
          
    context={
        'card_delete_details':card_delete_details,
        'account':account
    }
    return render(request,'account/delete_card.html',context)
          

               