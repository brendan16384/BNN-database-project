from django.contrib import admin
from BN_App.models import Employee
from BN_App.models import Product
from BN_App.models import Book
from BN_App.models import Game
from BN_App.models import Inventory
from BN_App.models import Location
from BN_App.models import SalesAtLocation
from BN_App.models import Sale

# Register your models here.
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Game)
admin.site.register(Inventory)
admin.site.register(Location)
admin.site.register(SalesAtLocation)
admin.site.register(Sale)
