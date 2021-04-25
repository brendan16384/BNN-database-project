# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    product_prod = models.OneToOneField('Product', models.DO_NOTHING, db_column='PRODUCT_PROD_ID', primary_key=True)  # Field name made lowercase.
    book_cover = models.CharField(db_column='BOOK_COVER', max_length=45)  # Field name made lowercase.
    book_author = models.CharField(db_column='BOOK_AUTHOR', max_length=45)  # Field name made lowercase.
    book_genre = models.CharField(db_column='BOOK_GENRE', max_length=45)  # Field name made lowercase.
    book_pages = models.IntegerField(db_column='BOOK_PAGES')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employee_id = models.IntegerField(db_column='EMPLOYEE_ID', primary_key=True)  # Field name made lowercase.
    location_loc = models.ForeignKey('Location', models.DO_NOTHING, db_column='LOCATION_LOC_ID')  # Field name made lowercase.
    employee_fname = models.CharField(db_column='EMPLOYEE_FNAME', max_length=45)  # Field name made lowercase.
    employee_lname = models.CharField(db_column='EMPLOYEE_LNAME', max_length=45)  # Field name made lowercase.
    employee_position = models.CharField(db_column='EMPLOYEE_POSITION', max_length=45)  # Field name made lowercase.
    employee_address = models.CharField(db_column='EMPLOYEE_ADDRESS', max_length=45)  # Field name made lowercase.
    employee_phone = models.CharField(db_column='EMPLOYEE_PHONE', max_length=10)  # Field name made lowercase.
    employee_email = models.CharField(db_column='EMPLOYEE_EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    employee_username = models.CharField(db_column='EMPLOYEE_USERNAME', max_length=45)  # Field name made lowercase.
    employee_password = models.CharField(db_column='EMPLOYEE_PASSWORD', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Game(models.Model):
    product_prod = models.OneToOneField('Product', models.DO_NOTHING, db_column='PRODUCT_PROD_ID', primary_key=True)  # Field name made lowercase.
    game_manufacturer = models.CharField(db_column='GAME_MANUFACTURER', max_length=45)  # Field name made lowercase.
    game_type = models.CharField(db_column='GAME_TYPE', max_length=45)  # Field name made lowercase.
    game_age = models.IntegerField(db_column='GAME_AGE', blank=True, null=True)  # Field name made lowercase.
    game_piece = models.IntegerField(db_column='GAME_PIECE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game'


class Inventory(models.Model):
    prod = models.OneToOneField('Product', models.DO_NOTHING, db_column='PROD_ID', primary_key=True)  # Field name made lowercase.
    location_loc = models.ForeignKey('Location', models.DO_NOTHING, db_column='LOCATION_LOC_ID')  # Field name made lowercase.
    inventory_quantity = models.IntegerField(db_column='INVENTORY_QUANTITY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'
        unique_together = (('prod', 'location_loc'),)


class Location(models.Model):
    loc_id = models.IntegerField(db_column='LOC_ID', primary_key=True)  # Field name made lowercase.
    loc_address = models.CharField(db_column='LOC_ADDRESS', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class Product(models.Model):
    prod_id = models.IntegerField(db_column='PROD_ID', primary_key=True)  # Field name made lowercase.
    prod_price = models.DecimalField(db_column='PROD_PRICE', max_digits=2, decimal_places=0)  # Field name made lowercase.
    prod_name = models.CharField(db_column='PROD_NAME', max_length=45)  # Field name made lowercase.
    prod_description = models.CharField(db_column='PROD_DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prod_returns = models.IntegerField(db_column='PROD_RETURNS')  # Field name made lowercase.
    prod_sales = models.IntegerField(db_column='PROD_SALES')  # Field name made lowercase.
    prod_department = models.CharField(db_column='PROD_DEPARTMENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prod_damaged = models.IntegerField(db_column='PROD_DAMAGED')  # Field name made lowercase.
    prod_thefts = models.IntegerField(db_column='PROD_THEFTS')  # Field name made lowercase.
    sale_sale = models.ForeignKey('Sale', models.DO_NOTHING, db_column='SALE_SALE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Sale(models.Model):
    sale_id = models.IntegerField(db_column='SALE_ID', primary_key=True)  # Field name made lowercase.
    sale_startdate = models.DateField(db_column='SALE_STARTDATE')  # Field name made lowercase.
    sale_enddate = models.DateField(db_column='SALE_ENDDATE', blank=True, null=True)  # Field name made lowercase.
    sale_percent = models.IntegerField(db_column='SALE_PERCENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sale'


class SalesAtLocation(models.Model):
    sale_sale = models.OneToOneField(Sale, models.DO_NOTHING, db_column='SALE_SALE_ID', primary_key=True)  # Field name made lowercase.
    location_loc = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_LOC_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales_at_location'
        unique_together = (('sale_sale', 'location_loc'),)
