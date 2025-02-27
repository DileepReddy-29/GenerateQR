from django.urls import path
from . import views

urlpatterns = [
    path('qr_code_display/', views.qr_generator, name = 'qr_code_display'),
    path('qr_generator/', views.qr_generator, name = 'qr_generator'),

    path("", views.home, name = 'home'),
    # path('signup/', views.signup, name = 'signup'),
    # path('signin/', views.signin, name = 'signin'),
    # path('signout/', views.signout, name = 'signout'),

]
