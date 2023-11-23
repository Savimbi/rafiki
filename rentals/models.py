from collections.abc import Iterable
from datetime import timedelta
from django.db import models

from books.models import Book
from customers.models import Customer

STATUS_CHOICES = (
    ('#0','rented'),
    ('#1','returned'),
    ('#2','lost'),
    ('#3','delayed'),
)

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    rent_start_date = models.DateField(help_text='When the book was rented')
    rent_end_date = models.DateField(help_text='deadline', blank=True)
    return_date = models.DateField(help_text='Actual return date', null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.book.book_id} rented by {self.customer.username}"
    
    def save(self,*args, **kwargs ) :
        if not self.rent_end_date:
            self.rent_end_date = self.rent_start_date + timedelta(days=14)
        return super().save(*args, **kwargs)