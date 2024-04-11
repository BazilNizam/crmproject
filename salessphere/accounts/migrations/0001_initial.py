# Generated by Django 5.0.4 on 2024-04-12 04:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('Facebook', 'Facebook'), ('Google', 'Google'), ('Friend to Friend', 'Friend to Friend'), ('Twitter', 'Twitter'), ('By Company', 'By Company'), ('LinkedIn', 'LinkedIn')], max_length=20, null=True)),
                ('status', models.CharField(choices=[('Lead', 'Lead'), ('Opportunity', 'Opportunity'), ('Customer', 'Customer')], max_length=200, null=True)),
                ('comment', models.TextField(blank=True, max_length=100, null=True)),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'leads',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, null=True)),
                ('img', models.ImageField(blank=True, default='LOGO.png', null=True, upload_to='')),
                ('message', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=225, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default-profile-pic.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=255, null=True)),
                ('company_phone', models.CharField(max_length=15, null=True)),
                ('company_email', models.EmailField(max_length=255, null=True)),
                ('address', models.TextField(max_length=255, null=True)),
                ('website', models.URLField(max_length=255)),
                ('profile_pic', models.ImageField(blank=True, default='default-company-pic.png', null=True, upload_to='', verbose_name='Logo/Photo')),
                ('lead', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.lead')),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('designation', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.lead')),
            ],
            options={
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.AddField(
            model_name='lead',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.employee', verbose_name='Assigned To'),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(null=True)),
                ('from_time', models.TimeField(null=True)),
                ('to_time', models.TimeField(null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('reminder', models.CharField(choices=[('None', 'None'), ('At the time of meeting', 'At the time of meeting'), ('5 minutes before', '5 minutes before'), ('15 minutes before', '15 minutes before'), ('30 minutes before', '30 minutes before'), ('1 hour before', '1 hour before'), ('1 day before', '1 day before')], default='15 minutes before', max_length=255, null=True)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.contact')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.lead')),
            ],
            options={
                'verbose_name_plural': 'meetings',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.employee', verbose_name='Assigned To')),
            ],
            options={
                'verbose_name_plural': 'opportunities',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('call_type', models.CharField(choices=[('Call', 'Call'), ('Conference', 'Conference'), ('Skype', 'Skype'), ('WhatsApp', 'WhatsApp')], max_length=255, null=True)),
                ('flag', models.CharField(choices=[('No Answer', 'No Answer'), ('Important', 'Important'), ('Busy', 'Busy'), ('Urgent', 'Urgent'), ('Left message', 'Left message'), ('Reschedule', 'Reschedule')], max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.lead')),
                ('opportunity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.opportunity')),
            ],
            options={
                'verbose_name_plural': 'calls',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=20, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.employee', verbose_name='Assigned to')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.contact')),
                ('opportunity', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.opportunity')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.product')),
            ],
            options={
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
