from django.shortcuts import render
from datetime import date
from BN_App.models import Product
from BN_App.models import Sale
from BN_App.models import Book
from BN_App.models import Game
from BN_App.models import Employee
from BN_App.models import Location
from BN_App.models import Inventory

# Create your views here.

def index(request):
    return render(request, 'BN_App/home.html')

def addProduct(request):
    return render(request, 'BN_App/addProduct.html')

def addProductConfirmed(request):
    id=request.GET['id']
    name=request.GET['name']
    description=request.GET['description']
    price=request.GET['price']
    damaged=request.GET['damaged']

    prod=Product()
    prod.prod_id=id
    prod.prod_name=name
    prod.prod_description=description
    prod.prod_price=price
    prod.prod_sales=0
    prod.prod_returns=0
    prod.prod_damaged=damaged
    prod.prod_thefts=0
    prod.save()

    return render(request, 'BN_App/addProductConfirmed.html')

def searchProducts(request):
    return render(request, 'BN_App/searchProducts.html')

def displayProducts(request):
    name=request.GET['name']
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']
    address=request.GET['address']

    query_set=Product.objects.all().select_related('sale_sale').select_related('inventory')
    return_set=[]
    
    if(address):
        query_set=query_set.filter(inventory__location_loc__loc_address__icontains=address)

    for obj in query_set:
        if(obj.sale_sale):
            if(obj.sale_sale.sale_enddate):
                if(obj.sale_sale.sale_startdate <= date.today() <= obj.sale_sale.sale_enddate):
                    obj.prod_price=(float(obj.prod_price)*(1-float(obj.sale_sale.sale_percent)/100.0))
            else:
                if(obj.sale_sale.sale_startdate <= date.today()):
                    obj.prod_price=(float(obj.prod_price)*(1-float(obj.sale_sale.sale_percent)/100.0))
        if(minPrice):
            if(maxPrice):
                if(name in obj.prod_name and obj.prod_price>=float(minPrice) and obj.prod_price<=float(maxPrice)):
                        return_set.append(obj)
            else:
                if(name in obj.prod_name and obj.prod_price>=float(minPrice)):
                        return_set.append(obj)
        else:
            if(maxPrice):
                if(name in obj.prod_name and obj.prod_price<=float(maxPrice)):
                        return_set.append(obj)
            else:
                if(name in obj.prod_name):
                        return_set.append(obj)
    
    context = {
        'obj_instance' : return_set,
    }
    return render(request, 'BN_App/displayProducts.html',context)

def addBook(request):
    return render(request, 'BN_App/addBook.html')

def addBookConfirmed(request):
    id=request.GET['id']
    name=request.GET['name']
    description=request.GET['description']
    price=request.GET['price']
    damaged=request.GET['damaged']
    cover=request.GET['cover']
    author=request.GET['author']
    genre=request.GET['genre']
    pages=request.GET['pages']

    prod=Product()
    prod.prod_department="books"
    prod.prod_id=id
    prod.prod_name=name
    prod.prod_description=description
    prod.prod_price=price
    prod.prod_sales=0
    prod.prod_returns=0
    prod.prod_damaged=damaged
    prod.prod_thefts=0
    prod.save()

    book=Book()
    book.product_prod=prod
    book.book_cover=cover
    book.book_author=author
    book.book_genre=genre
    book.book_pages=pages
    book.save()

    return render(request, 'BN_App/addBookConfirmed.html')

def searchBooks(request):
    return render(request, 'BN_App/searchBooks.html')

def displayBooks(request):
    name=request.GET['name']
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']
    auth=request.GET['author']
    genre=request.GET['genre']
    cover=request.GET['cover']
    minPages=request.GET['minPages']
    maxPages=request.GET['maxPages']
    address=request.GET['address']
    
    query_set=Product.objects.filter(prod_department='books').select_related('book').select_related('inventory')
    query_set=query_set.filter(prod_name__icontains=name)
    query_set.select_related('sale_sale')

    if(auth):
        query_set=query_set.filter(book__book_author__icontains=auth)

    if(genre):
        query_set=query_set.filter(book__book_genre__icontains=genre)

    if(cover):
        query_set=query_set.filter(book__book_cover__icontains=cover)

    if(minPages):
        query_set=query_set.filter(book__book_pages__gte=minPages)

    if(maxPages):
        query_set=query_set.filter(book__book_pages__lte=maxPages)
    
    if(address):
        query_set=query_set.filter(inventory__location_loc__loc_address__icontains=address)

    return_set=[]

    for obj in query_set:
        if(obj.sale_sale):
            if(obj.sale_sale.sale_enddate):
                if(obj.sale_sale.sale_startdate <= date.today() <= obj.sale_sale.sale_enddate):
                    obj.prod_price=(float(obj.prod_price)*(1-float(obj.sale_sale.sale_percent)/100.0))
            else:
                if(obj.sale_sale.sale_startdate <= date.today()):
                    obj.prod_price=(float(obj.prod_price)*(1-float(obj.sale_sale.sale_percent)/100.0))
        if(minPrice):
            if(maxPrice):
                if(name in obj.prod_name and obj.prod_price>=float(minPrice) and obj.prod_price<=float(maxPrice)):
                        return_set.append(obj)
            else:
                if(name in obj.prod_name and obj.prod_price>=float(minPrice)):
                        return_set.append(obj)
        else:
            if(maxPrice):
                if(name in obj.prod_name and obj.prod_price<=float(maxPrice)):
                        return_set.append(obj)
            else:
                if(name in obj.prod_name):
                        return_set.append(obj)
    
    context = {
        'obj_instance' : query_set
    }
    return render(request, 'BN_App/displayBooks.html',context)

def addGame(request):
    return render(request, 'BN_App/addGame.html')

def addGameConfirmed(request):
    id=request.GET['id']
    name=request.GET['name']
    description=request.GET['description']
    price=request.GET['price']
    damaged=request.GET['damaged']
    manufacturer=request.GET['manufacturer']
    gtype=request.GET['type']
    age=request.GET['age']
    pieces=request.GET['pieces']

    prod=Product()
    prod.prod_department="games"
    prod.prod_id=id
    prod.prod_name=name
    prod.prod_description=description
    prod.prod_price=price
    prod.prod_sales=0
    prod.prod_returns=0
    prod.prod_damaged=damaged
    prod.prod_thefts=0
    prod.save()

    game=Game()
    game.product_prod=prod
    game.game_manufacturer=manufacturer
    game.game_type=gtype
    if(age):
        game.game_age=age
    if(pieces):
        game.game_piece=pieces
    game.save()

    return render(request, 'BN_App/addGameConfirmed.html')

def searchGames(request):
    return render(request, 'BN_App/searchGames.html')

def displayGames(request):
    name=request.GET['name']
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']
    manufacturer=request.GET['manufacturer']
    gtype=request.GET['type']
    age=request.GET['age']
    address=request.GET['address']

    query_set=Product.objects.filter(prod_department="games").select_related("game").select_related('sale_sale').select_related('inventory')
    if(manufacturer):
        query_set=query_set.filter(game__game_manufacturer__icontains=manufacturer)
    if(gtype):
        query_set=query_set.filter(game__game_type__icontains=gtype)
    if(age):
        query_set=query_set.filter(game__game_age__lte=age)
    return_set=[]
    if(address):
        query_set=query_set.filter(inventory__location_loc__loc_address__icontains=address)

    for obj in query_set:
        if(obj.sale_sale):
            if(obj.sale_sale.sale_enddate):
                if(obj.sale_sale.sale_startdate <= date.today() <= obj.sale_sale.sale_enddate):
                    obj.prod_price=(float(obj.prod_price)*(1-float(obj.sale_sale.sale_percent)/100.0))
            else:
                if(obj.sale_sale.sale_startdate <= date.today()):
                    obj.prod_price=(float(obj.prod_price)*(1-float(obj.sale_sale.sale_percent)/100.0))
        if(minPrice):
            if(maxPrice):
                if(name in obj.prod_name and obj.prod_price>=float(minPrice) and obj.prod_price<=float(maxPrice)):
                        return_set.append(obj)
            else:
                if(name in obj.prod_name and obj.prod_price>=float(minPrice)):
                        return_set.append(obj)
        else:
            if(maxPrice):
                if(name in obj.prod_name and obj.prod_price<=float(maxPrice)):
                        return_set.append(obj)
            else:
                if(name in obj.prod_name):
                        return_set.append(obj)
    
    context = {
        'obj_instance' : return_set,
    }
    return render(request, 'BN_App/displayGames.html',context)

def login(request):
    return render(request, 'BN_App/login.html')

def addEmployee(request):
    return render(request, 'BN_App/addEmployee.html')

def addEmployeeConfirmed(request):
    
    id=request.GET['id']
    location=Location.objects.get(loc_id=request.GET['location'])
    firstName=request.GET['firstName']
    lastName=request.GET['lastName']
    position=request.GET['position']
    phone=request.GET['phone']
    email=request.GET['email']
    address=request.GET['address']
    username=request.GET['username']
    password=request.GET['password']

    employee=Employee()
    employee.employee_id=id
    employee.location_loc=location
    employee.employee_fname=firstName
    employee.employee_lname=lastName
    employee.employee_position=position
    employee.employee_phone=phone
    employee.employee_email=email
    employee.employee_address=address
    employee.employee_username=username
    employee.employee_password=password
    employee.save()

    return render(request, 'BN_App/addEmployeeConfirmed.html')

def searchEmployees(request):
    return render(request, 'BN_App/searchEmployees.html')

def displayEmployees(request):
    id=request.GET['id']
    locationID=request.GET['location']
    firstName=request.GET['firstName']
    lastName=request.GET['lastName']
    position=request.GET['position']
    phone=request.GET['phone']
    email=request.GET['email']
    address=request.GET['address']

    query_set=Employee.objects.all() 
    if(id):
        query_set=query_set.filter(employee_id=id)
    if(locationID):
        query_set=query_set.filter(location_loc=Location.objects.get(loc_id=locationID))
    if(firstName):
        query_set=query_set.filter(employee_fname__icontains=firstName)
    if(lastName):
        query_set=query_set.filter(employee_lname__icontains=lastName)
    if(position):
        query_set=query_set.filter(employee_position__icontains=position)
    if(phone):
        query_set=query_set.filter(employee_phone__icontains=phone)
    if(email):
        query_set=query_set.filter(employee_email__icontains=email)
    if(address):
        query_set=query_set.filter(employee_address__icontains=address)
    
    context = {
        'obj_instance' : query_set,
    }
    return render(request, 'BN_App/displayEmployees.html',context)

def empHome(request):
    username=request.GET['username']
    password=request.GET['password']

    emp=Employee.objects.get(employee_username=username)
    if(emp.employee_password==password):
        context = {
            'emp' : emp
        }
        return render(request, 'BN_App/empHome.html', context)
    else:
        return render(request, 'BN_App/failedLogin.html')

def checkout(request):
    location=int(request.GET['locID'])
    num=int(request.GET['num'])
    context={
        'location' : location,
        'num' : num
    }

    return render(request, 'BN_App/checkout.html', context)

def confirmCheckout(request):
    total=0.0
    location=request.GET['location']
    for q in range(int(request.GET['num'])):
        prod=Product.objects.get(prod_id=request.GET['prodID'+str(q)])
        quantity=int(request.GET['quantity'+str(q)])
        if(prod.sale_sale):
            if(prod.sale_sale.sale_enddate):
                if(prod.sale_sale.sale_satrtdate<=date.today() and prod.sale_sale.sale_enddate>=date.today()):
                    prod.prod_price=float(prod.prod_price)*(1-float(prod.sale_sale.sale_percent)/100.0)
            else:
                if(prod.sale_sale.sale_startdate<=date.today()):
                    prod.prod_price=float(prod.prod_price)*(1-float(prod.sale_sale.sale_percent)/100.0)
        total+=float(prod.prod_price*quantity)

        inv=Inventory.objects.filter(location_loc=location)
        inv=inv.get(prod=prod)
        inv.inventory_quantity-=quantity
        inv.save()

    context={
        'total' : total
    }

    return render(request, 'BN_App/confirmCheckout.html', context)

def addInventory(request):
    return render(request, 'BN_App/addInventory.html')

def addInventoryConfirmed(request):
    id=request.GET['product']
    prod=Product.objects.get(prod_id=id)
    location=Location.objects.get(loc_id=request.GET['location'])
    recieved=int(request.GET['recieved'])
    damaged=int(request.GET['damaged'])
    prod.prod_damaged=prod.prod_damaged+damaged
    
    inv=Inventory.objects.filter(prod=prod).filter(location_loc=location)
    
    inv=Inventory()
    inv.prod=prod
    inv.location_loc=location
    inv.inventory_quantity=recieved-damaged

    inv.save()

    return render(request, 'BN_App/addInventoryConfirmed.html')

def searchProductReport(request):
    return render(request, 'BN_App/searchProductReport.html')

def displayProductReport(request):
    
    id=request.GET['id']

    prod=Product.objects.get(prod_id=id)

    context = {
        'obj_instance' : prod,
    }
    return render(request, 'BN_App/displayProductReport.html', context)

def searchLocations(request):
    return render(request, 'BN_App/searchLocations.html')

def displayLocations(request):

    street=request.GET['street']
    zipCode=request.GET['zipCode']
    city=request.GET['city']
    state=request.GET['street']

    query_set=Location.objects.all() 
    if(street):
        query_set=query_set.filter(loc_address__icontains=street)
    if(city):
        query_set=query_set.filter(loc_address__icontains=city)
    if(zipCode):
        query_set=query_set.filter(loc_address__icontains=zipCode)
    if(state):
        query_set=query_set.filter(loc_address__icontains=state)
    
    context = {
        'obj_instance' : query_set,
    }
    return render(request, 'BN_App/displayLocations.html',context)

def searchProductEdit(request):
    return render(request, 'BN_App/searchProductEdit.html')

def editProduct(request):
    prod=Product.objects.get(prod_id=request.GET['id'])
    context={
        'prod':prod
    }
    return render(request, 'BN_App/editProduct.html',context)

def editProductConfirmed(request):
    id=request.GET['id']
    name=request.GET['name']
    description=request.GET['description']
    price=request.GET['price']
    department=request.GET['department']
    sales=request.GET['sales']
    returns=request.GET['returns']
    damaged=request.GET['damaged']
    thefts=request.GET['thefts']

    prod=Product()
    prod.prod_id=id
    prod.prod_name=name
    prod.prod_description=description
    prod.prod_price=price
    prod.prod_department=department
    prod.prod_sales=sales
    prod.prod_returns=returns
    prod.prod_damaged=damaged
    prod.prod_thefts=thefts
    prod.save()

    return render(request, 'BN_App/editProductConfirmed.html')

def searchEmployeeToEdit(request):
    return render(request, 'BN_App/searchEmployeeToEdit.html')

def editEmployee(request):
    emp=Employee.objects.get(employee_id=request.GET['id'])
    context={
        'employee':emp
    }
    return render(request, 'BN_App/editEmployee.html',context)

def editEmployeeConfirmed(request):
    
    id=request.GET['id']
    fname=request.GET['fname']
    lname=request.GET['lname']
    location=request.GET['location']
    position=request.GET['position']
    address=request.GET['address']
    phone=request.GET['phone']
    email=request.GET['email']
    username=request.GET['username']
    password=request.GET['password']

    employee=Employee()
    employee.employee_id=id
    employee.employee_fname=fname
    employee.employee_lname=lname
    employee.location_loc_id=location
    employee.employee_position=position
    employee.employee_address=address
    employee.employee_phone=phone
    employee.employee_email=email
    employee.employee_username=username
    employee.employee_password=password

    employee.save()
    
    context = {
        'obj_instance' : return_set,
    }
    return render(request, 'BN_App/editEmployeeConfirmed.html',context)

def deleteProduct(request):
    return render(request, 'BN_App/deleteProduct.html')

def deleteProductConfirm(request):
    prod=Product.objects.get(prod_id=request.GET['id'])
    prod.delete()
    return render(request,'BN_App/deleteProductConfirm.html')

def deleteEmployee(request):
    return render(request, 'BN_App/deleteEmployee.html')

def deleteEmployeeConfirmed(request):
    
    employee=Employee.objects.get(employee_id=request.GET['id'])
    employee.delete()

    return render(request, 'BN_App/deleteEmployeeConfirmed.html')

def addLocation(request):
    return render(request, 'BN_App/addLocation.html')

def addLocationConfirmed(request):
    id=request.GET['id']
    address=request.GET['address']

    location=Location()
    location.loc_id=id
    location.loc_address=address
    location.save()

    return render(request, 'BN_App/addLocationConfirmed.html')

def deleteLocation(request):
    return render(request, 'BN_App/deleteLocation.html')

def deleteLocationConfirmed(request):
    
    location=Location.objects.get(loc_id=request.GET['id'])
    location.delete()

    return render(request, 'BN_App/deleteLocationConfirmed.html')

