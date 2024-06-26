from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=225, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, default='default-profile-pic.jpg')

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, verbose_name='Assigned to')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name


class Lead(models.Model):
    SOURCES = (
        ('Facebook', 'Facebook'),
        ('Google', 'Google'),
        ('Friend to Friend', 'Friend to Friend'),
        ('Twitter', 'Twitter'),
        ('By Company', 'By Company'),
        ('LinkedIn', 'LinkedIn'),
    )

    STATUS = (
        ('Lead', 'Lead'),
        ('Opportunity', 'Opportunity'),
        ('Customer', 'Customer'),
    )
    source = models.CharField(max_length=20, null=True, choices=SOURCES)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name='Assigned To')
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    comment = models.TextField(max_length=100, null=True, blank=True)
    delete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'leads'

    def class_name(self):
        return self._meta.model_name

    def __str__(self):
        return self.company.company_name


class Opportunity(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name='Assigned To')
    delete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'opportunities'

    def class_name(self):
        return self._meta.model_name


class Company(models.Model):
    company_name = models.CharField(max_length=255, null=True)
    company_phone = models.CharField(max_length=15, null=True)
    company_email = models.EmailField(max_length=255, null=True)
    address = models.TextField(max_length=255, null=True)
    website = models.URLField(max_length=255)
    profile_pic = models.ImageField(null=True, blank=True, default='default-company-pic.png', verbose_name="Logo/Photo")
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name_plural = 'companies'

    def class_name(self):
        return self._meta.model_name

    def __str__(self):
        return self.company_name


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=255, null=True)
    designation = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    lead = models.ForeignKey(Lead, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'contacts'

    def class_name(self):
        return self._meta.model_name

    def __str__(self):
        return self.name


class Customer(models.Model):
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    opportunity = models.OneToOneField(Opportunity, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'customers'

    def class_name(self):
        return self._meta.model_name

    def __str__(self):
        return str(self.contact.name)


class Email(models.Model):
    subject = models.CharField(max_length=255, null=True)
    img = models.ImageField(null=True, blank=True, default='LOGO.png')
    message = models.TextField(max_length=255, null=True)

    def __str__(self):
        return str(self.subject)


class Call(models.Model):
    CALL_TYPES = (
        ("Call", "Call"),
        ("Conference", "Conference"),
        ("Skype", "Skype"),
        ("WhatsApp", "WhatsApp"),
    )

    FLAGS = (
        ("No Answer", "No Answer"),
        ("Important", "Important"),
        ("Busy", "Busy"),
        ("Urgent", "Urgent"),
        ("Left message", "Left message"),
        ("Reschedule", "Reschedule"),
    )
    lead = models.ForeignKey(Lead, null=True, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True)
    call_type = models.CharField(max_length=255, null=True, choices=CALL_TYPES)
    flag = models.CharField(max_length=255, null=True, choices=FLAGS)
    description = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'calls'

    def class_name(self):
        return self._meta.model_name

    def __str__(self):
        return f"{self.call_type} on {self.date}"


class Meeting(models.Model):
    REMINDER = (
        ("None", "None"),
        ("At the time of meeting", "At the time of meeting"),
        ("5 minutes before", "5 minutes before"),
        ("15 minutes before", "15 minutes before"),
        ("30 minutes before", "30 minutes before"),
        ("1 hour before", "1 hour before"),
        ("1 day before", "1 day before"),
    )
    title = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    lead = models.ForeignKey(Lead, null=True, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    host = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)
    reminder = models.CharField(max_length=255, null=True, choices=REMINDER, default="15 minutes before")

    class Meta:
        verbose_name_plural = 'meetings'

    def class_name(self):
        return self._meta.model_name

    def __str__(self):
        return self.title
