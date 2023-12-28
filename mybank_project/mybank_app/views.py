from django.shortcuts import render, redirect
from .models import BankAccount,Service
from .forms import BankAccountForm


def home(request):
    services = BankAccount.objects.all()
    return render(request, 'home.html', {'services': services})


def create_account(request):
    if request.method == "POST":
        full_name = request.POST['fullName']
        phone_number = request.POST['phoneNumber']
        residential_address = request.POST['residentialAddress']
        citizenship = request.POST['citizenship']
        value = BankAccount(
         full_name=full_name,
         phone_number=phone_number,
         residential_address= residential_address,
         citizenship=citizenship   
        )
        value.save()
    return render(request, 'create_account.html')
