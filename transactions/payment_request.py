from django.shortcuts import render
from bankaccounts.models import Account,KYC
from django.db.models import Q
from transactions.models import Transaction
from django.shortcuts import redirect
from django.contrib import messages
def user_request_payment_by_accnum(request):
    account=Account.objects.all()
    query=request.POST.get("account_number")
    if query:
        account=account.filter(
            Q(account_number=query)
        ).distinct()
    
    context={
        'account':account,
        'query':query
    }
    return render(request,'payment_request/user_request_payment.html',context)
# def request_amount(request,account_number):
#     account=Account.objects.get(account_number=account_number)
#     if request.method=="POST":
#         amount=request.POST.get("amount-send")
#         description=request.POST.get("description")
#         print(amount)
#         print(description)
#         return redirect("transactions:request_confirmation",account.account_number)
#     return render(request,'payment_request/request_amount.html',{'account':account})

def request_amount(request,account_number):
    account=Account.objects.get(account_number=account_number)
    sender=request.user
    receiver=account.user
    sender_account=request.user.account
    receiver_account=account
    if request.method=="POST":
        amount=request.POST.get("amount-send")
        description=request.POST.get("description")
        print(amount)
        print(description)
        if sender_account.account_balance >0 and amount:
            new_transaction=Transaction.objects.create(
                user=request.user,
                description=description,
                amount=amount,
                sender_account=sender_account,
                sender=sender,
                receiver=receiver,
                receiver_account=receiver_account,
                status="request_sent",
                transaction_type="request"
            )
            new_transaction.save()
            transaction_id=new_transaction.transaction_id
            return redirect("transactions:request_confirmation",account.account_number,transaction_id)
    return render(request,'payment_request/request_amount.html',{'account':account})


def request_confirmation(request,account_number,transaction_id):
  try:
      transaction=Transaction.objects.get(transaction_id=transaction_id)
      account=Account.objects.get(account_number=account_number)
      sender_account=request.user.account
      receiver=account.user
      if request.method=="POST":
          Entered_pin_number=request.POST.get("pin-number")
          if transaction.amount<=account.account_balance:
              if account.pin_number==Entered_pin_number:
                 print(Entered_pin_number)
                 account.account_balance=account.account_balance-transaction.amount
                 account.save()
                 print("Available Balance is => ",account.account_balance)
                 transaction.status="request_sent"
                 transaction_type="request"
                 transaction.save()
                 print(transaction.status)
                 return redirect("transactions:request_success",account_number,transaction_id)
              else:
                  print("Invalid Pinnumber")
          else:
              print("Insufficient Balance")

  except:
      messages.warning("Account does not exist")
     
  context={
          'transaction':transaction,
           'account':account,
           'receiver':receiver,
           'sender_account':sender_account,
  }
  return render(request,'payment_request/request_amount_confirmation.html',context)

def request_success(request,account_number,transaction_id):
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    account=Account.objects.get(account_number=account_number)
    kyc=KYC.objects.get(user=request.user)
    receiver=account.user

    context={
          'transaction':transaction,
           'account':account,
           'kyc':kyc,
          'receiver':receiver

    }
    return render(request,'payment_request/request_success.html',context)

def send_Confirmation(request,account_number,transaction_id):
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    account=Account.objects.get(account_number=account_number)
    if request.method=="POST":
      return redirect("transactions:send_completed",account_number,transaction_id)
    return render(request,'payment_request/send_confirmation.html',{'account':account})
def send_processing(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    sender=request.user
    sender_account=request.user.account
    if request.method=="POST":
        pin_number=request.POST.get("pin-number")
        if pin_number==request.user.account.pin_number:
            if sender_account.account_balance <=0 or sender_account.account_balance<transaction.amount:
                messages.warning(request,'Insufficient Funds ,Fund you account and tryagain')
            else:
                sender_account.account_balance-=transaction.amount
                sender_account.save()

                account.account_balance+=transaction.amount
                account.save()

                transaction.status="completed"
                transaction.save()

                messages.success(request,f"Setteled to {account.user.kyc.full_name} was successfull")
                return redirect("transactions:send_amount_completed",account.account_number,transaction.transaction_id)
        else:
            messages.warning(request,'pin number is not matching')
    context={
        'account':account,
        'transaction':transaction
    }
    return render(request,'payment_request/send_completed.html',context)
def send_amount_completed(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    sender=request.user
    sender_account=request.user.account

    context={
        'account':account,
        'transaction':transaction,
        'sender':sender,
        'sender_account':sender_account
    }
    return render(request,'payment_request/send_amount_completed.html',context)
