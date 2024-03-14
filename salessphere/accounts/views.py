from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user, admin_only, allowed_users
from .forms import CreateUserForm, LeadForm, CompanyForm, ContactForm
from .models import *


# Create your views here.



@login_required(login_url='login')
@admin_only
def home(request):
    print(request.user)
    leads = Lead.objects.all().filter(status="Lead", delete=False)
    products = Product.objects.all()
    opportunities = Lead.objects.all().filter(status="Opportunity", delete=False)
    customers = Lead.objects.all().filter(status="Customer", delete=False)
    orders = Order.objects.all()
    employees = User.objects.filter(groups__name='employee')
    total_employees = employees.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    last_five_orders = orders.order_by('-id')[:5]

    employee_data = []

    for emp in employees:
        _leads = emp.employee.lead_set.filter(status="Lead", delete=False)
        _opportunities = emp.employee.lead_set.filter(status="Opportunity", delete=False)
        _customers = emp.employee.lead_set.filter(status="Customer", delete=False)

        employee = [
            emp.username,
            _leads.count(),
            _opportunities.count(),
            _customers.count(),
        ]
        employee_data.append(employee)

    context = {'orders': orders, 'employees': employees,
               'total_orders': total_orders, 'total_employees': total_employees,
               'delivered': delivered, 'pending': pending, 'last_five_orders': last_five_orders,
               'total_leads': leads.count(), 'total_opportunities': opportunities.count(),
               'total_customers': customers.count(),
               'employee_data': employee_data, 'products': products,
               }
    render(request, "accounts/base.html", context)

    return render(request, 'accounts/dashboard.html', context)

# -----------------Lead start----------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['employee', 'admin'])
def index(request):
    return render(request, 'accounts/leads.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_lead(request):
    context = {}

    lead_form = LeadForm()
    contact_form = ContactForm()
    company_form = CompanyForm()

    if request.method == 'POST':
        lead_form = LeadForm(request.POST)
        contact_form = ContactForm(request.POST)
        company_form = CompanyForm(request.POST)

        print('Pre save')
        print(lead_form.errors)
        print(contact_form.errors)
        print(company_form.errors)
        if lead_form.is_valid() and contact_form.is_valid() and company_form.is_valid():
            lead = lead_form.save()
            lead.status = "Lead"
            print('lead save')
            company = company_form.save()
            print('company save')
            contact = contact_form.save(commit=False)
            setattr(lead, 'company', company)
            contact.lead = lead
            contact_form.save()
            lead.save()
            lead_form.save()

            return redirect('http://localhost:8000/leads/')

    context = {'lead_form': lead_form, 'contact_form': contact_form, 'company_form': company_form}
    return render(request, 'accounts/lead_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['employee', 'admin'])
def update_lead(request, id):
    lead = Lead.objects.get(id=id)

    lead_form = LeadForm(instance=lead)
    print(lead.company)
    company_form = CompanyForm(instance=lead.company)
    contact_form = ContactForm(instance=lead.contact_set.all().first())

    if request.method == 'POST':
        lead_form = LeadForm(request.POST, instance=lead)
        contact_form = ContactForm(request.POST, instance=lead.contact_set.all().first())
        company_form = CompanyForm(request.POST, instance=lead.company)
        print("pre save")
        if lead_form.is_valid() and contact_form.is_valid() and company_form.is_valid():
            lead = lead_form.save()
            contact_form.save()
            company_form.save()
            print("post save")
            messages.success(request, f'Succesfully updated Lead {lead.company}')
            return redirect('http://localhost:8000/leads/')

    context = {'lead_form': lead_form, 'contact_form': contact_form, 'company_form': company_form}
    return render(request, 'accounts/lead_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['employee', 'admin'])
def delete_lead(request, id):
    lead = Lead.objects.get(id=id)

    if request.method == 'POST':
        if lead.delete:
            lead.delete()
        else:
            lead.delete = True
            lead.save()
        return redirect('http://localhost:8000/leads/')

    context = {'data': lead, 'delete': f'delete_lead', 'reverse': lead._meta.verbose_name_plural}
    return render(request, 'accounts/delete.html', context)

# -----------------Lead end----------------------------------------------

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:

            login(request, user)
            print(request.user)
            return redirect('home')
        else:
            messages.warning(request, 'Username or Password is incorrect.')

    context = {}
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

