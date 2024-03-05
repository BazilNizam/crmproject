from django.shortcuts import render

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