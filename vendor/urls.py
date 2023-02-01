from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),
    
    # Category CRUD
    path('menu-builder/category/add/', views.add_category, name='add_category'),
    path('menu-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
         
    # Fooditem CRUD
    path('menu-builder/fooditem/add/', views.add_fooditem, name='add_fooditem'),
    path('menu-builder/fooditem/edit/<int:pk>/', views.edit_fooditem, name='edit_fooditem'),
    path('menu-builder/fooditem/delete/<int:pk>/', views.delete_fooditem, name='delete_fooditem'),

    # Open Hours
    path('open-hours/', views.open_hours, name='open_hours'),
    path('open-hours/add/', views.add_open_hours, name='add_open_hours'),
    path('open-hours/remove/<int:pk>/', views.remove_open_hours, name='remove_open_hours'),
    path('my_orders/', views.my_orders, name='vendor_my_orders'),
]
