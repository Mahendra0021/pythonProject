from django import forms



class BankAccountForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    phone_number = forms.IntegerField()
    # id_proof = forms.CharField(max_length=20)
    # account_type = forms.CharField(max_length=10)
    # email_address = forms.EmailField()
    # date_of_birth = forms.DateField()
    residential_address = forms.CharField(max_length=100)
    # digital_picture = forms.ImageField(upload_to='digital_pictures/')
    citizenship = forms.CharField(max_length=50)
    # initial_deposit = forms.DecimalField(max_digits=10, decimal_places=2)
    # agree_t_and_c = forms.BooleanField()
