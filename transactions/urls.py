from django.urls import path
from transactions import transfer,payment_request,credit_card
from bankaccounts.models import Account
app_name="transactions"
urlpatterns=[
    path("",transfer.search_user_by_acc_num,name="search"),
    path("amount_transfer/<account_number>/",transfer.amount_transfer,name="amount_transfer"),
    path("amount_transfer_process/<account_number>/",transfer.amount_transfer_process,name="amount_transfer_process"),
    path("transfer_confirmation/<account_number>/<transaction_id>/",transfer.transfer_confirmation,name="transfer-confirmation"),
    path("transfer_success/<account_number>/<transaction_id>/",transfer.transfer_success,name="transfer-success"),
    path("transaction_detail/<transaction_id>/",transfer.transaction_detail,name="transaction_detail"),
    path("user_request_payment/",payment_request.user_request_payment_by_accnum,name="user_request_payment"),
    path("request_amount/<account_number>/",payment_request.request_amount,name="request_amount"),
    path("request_confirmation/<account_number>/<transaction_id>/",payment_request.request_confirmation,name="request_confirmation"),
    path("request_success/<account_number>/<transaction_id>/",payment_request.request_success,name="request_success"),
    path("transaction_list/",transfer.transaction_list,name="transaction_list"),
    path("send_confirmation/<account_number>/<transaction_id>/",payment_request.send_Confirmation,name="send_confirmation"),
    path("send_completed/<account_number>/<transaction_id>/",payment_request.send_processing,name="send_completed"),
    path("send_amount_completed/<account_number>/<transaction_id>/",payment_request.send_amount_completed,name="send_amount_completed"),
    path("creditcard/<number>/<account_number>/",credit_card.credit_card_detail,name="credit_card_detail"),
    path("credit_card_bill/<card_id>/",credit_card.credit_card_bill,name="credit_card_bill"),
    path("withdraw_amount/<card_id>/",credit_card.withdraw_amount,name="withdraw_amount_card"),
    path("delete_Card/<card_id>/",credit_card.delete_card,name="delete_card")
]