from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=100)
    # id_proof = models.CharField(max_length=20)
    # account_type = models.CharField(max_length=10)
    # email_address = models.EmailField()
    # date_of_birth = models.DateField()
    residential_address = models.TextField()
    # digital_picture = models.ImageField(upload_to='digital_pictures/')
    citizenship = models.CharField(max_length=50)
    # initial_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    # agree_t_and_c = models.BooleanField()

    def __str__(self):
        return self.full_name
