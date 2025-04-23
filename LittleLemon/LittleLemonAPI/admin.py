from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Cart, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'featured']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'category__title']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'menuitem', 'quantity', 'unit_price', 'price']
    list_filter = ['user']
    search_fields = ['user__username', 'menuitem__title']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'delivery_crew', 'status', 'total', 'date']
    list_filter = ['status', 'date']
    search_fields = ['user__username', 'delivery_crew__username']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menuitem', 'quantity', 'unit_price', 'price']
    list_filter = ['order']
    search_fields = ['order__id', 'menuitem__title']