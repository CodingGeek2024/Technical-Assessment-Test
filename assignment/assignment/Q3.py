from django.db import models
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def get_top_5_customers_last_6_months(cls):
        six_months_ago = timezone.now() - timedelta(days=180)
        return cls.objects.filter(
            order_date__gte=six_months_ago
        ).values(
            'customer'
        ).annotate(
            total_spent=Sum('total_amount')
        ).order_by(
            '-total_spent'
        )[:5]

# Assuming you have a Customer model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

# In views.py
from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    top_customers = Order.get_top_5_customers_last_6_months()
    context = {'top_customers': top_customers}
    return render(request, 'top_customers.html', context)
