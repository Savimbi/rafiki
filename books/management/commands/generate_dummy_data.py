import random
from typing import Any
from django.core.management.base import BaseCommand
from authors.models import Author
from customers.models import Customer
from books.models import Book, BookTitle
from publishers.models import Publisher
from django_countries.fields import Country



class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
    
            author_list = ['John smith', 'Adams Jones', 'Jane Jon', 'Claire Dukuze']
            
            for name in author_list:
                Author.objects.create(name=name)
                
            # generate publishers    
            publishers_list = [
                {'name': 'X book', 'country':Country(code="us")},
                {'name': 'Bookz', 'country':Country(code="de")},
                {'name': 'Edmondo', 'country':Country(code="rw")},
                {'name': 'Next book', 'country':Country(code="gb")},
                {'name': 'Ikirezi', 'country':Country(code="pl")},
            ]
            
            for item in publishers_list:
                Publisher.objects.create(**item)
                
            # generate book titles
            book_title_list = ['Inkuba na gikeri','Imana yingore','Umwami numwana','Akaga mubantu','Ikirere gisa']
            publishers = [x.name for x in Publisher.objects.all()]
            items = zip(book_title_list, publishers)
            
            for item in items:
                author = Author.objects.order_by('?')[0]
                publisher= Publisher.objects.get(name=item[1])
                BookTitle.objects.create(title=item[0], publisher=publisher, author=author)
                
                
            #generate books
            print("generating books")
            book_titles = BookTitle.objects.all()
            
            for title in book_titles:
                quantity =  random.randint(1,5)
                
                for i in range(quantity):
                    Book.objects.create(title = title)
                    
            #generate customers
            customer_list = [
                {"first_name" : 'John' , 'last_name': 'Ben'},
                {"first_name" : 'Orla' , 'last_name': 'Duke'},
                {"first_name" : 'Ken' , 'last_name': 'Horris'},
            ]
            
            for item in customer_list:
                Customer.objects.create(**item)
                