from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns= [
    path('', views.index, name='index'),

    path('addProduct/', views.addProduct, name='addProduct'),
    path('addProductConfirmed/', views.addProductConfirmed, name='addProductConfirmed'),
    path('searchProducts/', views.searchProducts, name='searchProducts'),
    path('displayProducts/', views.displayProducts, name='displayProducts'),

    path('addBook/', views.addBook, name='addBook'),
    path('addBookConfirmed/', views.addBookConfirmed, name='addBookConfirmed'),
    path('searchBooks/', views.searchBooks, name='searchBooks'),
    path('displayBooks/', views.displayBooks, name='displayBooks'),

    path('addGame/', views.addGame, name='addGame'),
    path('addGameConfirmed/', views.addGameConfirmed, name='addGameConfirmed'),
    path('searchGames/', views.searchGames, name='searchGames'),
    path('displayGames/', views.displayGames, name='displayGames'),

    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('addEmployeeConfirmed/', views.addEmployeeConfirmed, name='addEmployeeConfirmed'),
    path('searchEmployees/', views.searchEmployees, name='searchEmployees'),
    path('displayEmployees/', views.displayEmployees, name='displayEmployees'),

    path('empHome/', views.empHome, name='empHome'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmCheckout/', views.confirmCheckout, name='confirmCheckout'),
    path('addInventory/', views.addInventory, name='addInventory'),
    path('addInventoryConfirmed/', views.addInventoryConfirmed, name='addInventoryConfirmed'),

    path('searchProductReport/', views.searchProductReport, name='searchProductReport'),
    path('displayProductReport/', views.displayProductReport, name='displayProductReport'),
    
    path('searchLocations/', views.searchLocations, name='searchLocations'),
    path('displayLocations/', views.displayLocations, name='displayLocations'),

    path('searchProductEdit/', views.searchProductEdit, name='searchProductEdit'),
    path('editProduct/', views.editProduct, name='editProduct'),
    path('editProductConfirmed/', views.editProductConfirmed, name='editProductConfirmed'),

    path('searchEmployeeToEdit/', views.searchEmployeeToEdit, name='searchEmployeeToEdit'),
    path('editEmployee/', views.editEmployee, name='editEmployee'),
    path('editEmployeeConfirmed/', views.editEmployeeConfirmed, name='editEmployeeConfirmed'),

    path('deleteProduct/', views.deleteProduct, name='deleteProduct'),
    path('deleteProductConfirm/', views.deleteProductConfirm, name='deleteProductConfirm'),

    path('deleteEmployee/', views.deleteEmployee, name='deleteEmployee'),
    path('deleteEmployeeConfirmed/', views.deleteEmployeeConfirmed, name='deleteEmployeeConfirmed'),
    
    path('addLocation/', views.addLocation, name='addLocation'),
    path('addLocationConfirmed/', views.addLocationConfirmed, name='addLocationConfirmed'),
    
    path('deleteLocation/', views.deleteLocation, name='deleteLocation'),
    path('deleteLocationConfirmed/', views.deleteLocationConfirmed, name='deleteLocationConfirmed'),
    
    path('login/', LoginView.as_view(template_name='BN_App/login.html'), name='Login'),
]