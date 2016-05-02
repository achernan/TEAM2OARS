from __future__ import unicode_literals

from django.db import models

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
YESNO_CHOICES = (('Y', 'Yes'), ('N', "No"))
MARRIAGE_CHOICES = (('M', 'Married'), ('S', 'Single'))
RENTAL_STATUS_CHOICES = (('S', 'Signed but Not Occupied'), ('O', 'Occupied'))

class Staff (models.Model):
    ASSISTANT = 'Assistant'
    MANAGER = 'Manager'
    SUPERVISOR = 'Supervisor'
    CUSTOMERSERVICE = 'Customer Service'
    POSITION_CHOICES = ((ASSISTANT, 'assistant'), (MANAGER, 'manager'),
                        (SUPERVISOR, 'supervisor'), (CUSTOMERSERVICE, 'customer service'))
    staff_no = models.TextField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    position = models.CharField(max_length=16, choices=POSITION_CHOICES, default=ASSISTANT)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    date_of_birth = models.DateField()
    salary = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.staff_no)

class Apartment (models.Model):
    VACANT = 'V'
    RENTED = 'R'
    STATUS_CHOICES = ((VACANT, 'Vacant'), (RENTED, 'Rented'))
    apt_no = models.CharField(primary_key=True, max_length=3)
    apt_type = models.CharField(max_length=1)
    apt_status = models.CharField(max_length=6, choices=STATUS_CHOICES,  default=VACANT)
    apt_utility = models.CharField(max_length=3, choices=YESNO_CHOICES, default='N')
    apt_deposit_amt = models.FloatField(max_length=5)
    apt_rent_amt = models.FloatField(max_length=5)

    def __str__(self):
        return "Apt Num - " + str(self.apt_no)

class Handle_Rents (models.Model):
    LEASE_OPTION_CHOICES = (('one', 'One'), ('six', 'Six'))
    rental_no = models.AutoField(primary_key=True)
    rental_date = models.DateField()
    rental_status = models.CharField(max_length=50, choices=RENTAL_STATUS_CHOICES, default='S')
    cancel_date = models.DateField()
    lease_type = models.CharField(max_length=50, choices=LEASE_OPTION_CHOICES, default='one')
    lease_start = models.DateField()
    lease_end = models.DateField()
    renewal_date = models.DateField()
    staff_no = models.ForeignKey(Staff, on_delete=models.CASCADE)
    apt_no = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return "Rental Num - " + str(self.rental_no)


class Tenant(models.Model):
    tenant_ss = models.TextField(primary_key=True)
    tenant_name = models.TextField()
    tenant_DOB = models.DateField()
    marital = models.CharField(max_length=1)
    work_phone = models.PositiveIntegerField()
    home_phone = models.PositiveIntegerField()
    gender = models.CharField(max_length=1)
    employer = models.TextField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    rental_no = models.ForeignKey(Handle_Rents, on_delete=models.CASCADE)

    def __str__(self):
        return self.tenant_name + " - " + self.username


class Automobiles (models.Model):
    license_no = models.CharField(max_length=8, primary_key=True)
    auto_make = models.TextField(max_length=20)
    auto_model = models.CharField(max_length=20)
    auto_year = models.TextField()
    auto_color = models.TextField(max_length=20)
    tenant_ss = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_no + " - " + self.auto_model

class Tenant_Family(models.Model):
    family_ss = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    spouse = models.TextField()
    child = models.TextField()
    divorced = models.CharField(max_length=3, choices=YESNO_CHOICES, default='N')
    single = models.CharField(max_length=3, choices=YESNO_CHOICES, default='N')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    date_of_birth = models.DateField()
    tenant_ss = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return "Name - " + self.name

class Invoices (models.Model):
    CC_CHOICES = (('visa', 'Visa'), ('mastercard', 'Mastercard'),
              ('american express', 'American Express'), ('discover', 'Discover'))
    invoice_no = models.PositiveSmallIntegerField(primary_key=True)
    invoice_date = models.DateField()
    invoice_due = models.FloatField(max_length=5)
    CC_no = models.BigIntegerField()
    CC_type = models.CharField(max_length=30, choices=CC_CHOICES, default='visa')
    CC_exp_date = models.DateField()
    CC_amt = models.FloatField(max_length=5)
    rental_no = models.ForeignKey(Handle_Rents, on_delete=models.CASCADE)

    def __str__(self):
        return "Invoice Num - " + str(self.invoice_no)

class Complaints (models.Model):
    COMPLAINT_STATUS_CHOICES = (('F', 'Fixed'), ('P', 'Pending'), ('Null', 'Undetermined'))
    complaint_id = models.AutoField(primary_key=True)
    complaint_date = models.DateField()
    rental_complaint = models.TextField()
    apt_complaint = models.TextField()
    status = models.CharField(max_length=30, choices=COMPLAINT_STATUS_CHOICES)
    rental_no = models.ForeignKey(Handle_Rents, on_delete=models.CASCADE)
    apt_no = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.complaint_id)

class Testimonies(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    testimonial_date = models.DateField()
    testimonial_content = models.TextField()
    tenant_ss = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.testimonial_content
