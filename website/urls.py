from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),

    path('product/',views.product, name='product'),
    path('viewProduct/',views.viewProduct, name='viewProduct'),

    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/',views.contactus, name='contactus'),




    path('orders/',views.orders, name='orders'),
    path('checkout/',views.checkout, name='checkout'),
    path('signIn',views.signIn, name='signIn'),
    path('signUp',views.signUp, name='signUp'),
    path('base/',views.base,name='base'),
]
