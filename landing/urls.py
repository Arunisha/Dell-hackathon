from django.urls import path,reverse
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
	path('', login_required(views.HomeView.as_view(),login_url='/auth/login'), name='home'),
	path('product/<int:pk>', login_required(views.SpecificView.as_view(),login_url='/auth/login'),name='specific'),
	path('cart',login_required(views.CartView.as_view(),login_url='/auth/login'),name='cart'),
	path('searching',login_required(views.SearchView.as_view(),login_url='/auth/login'),name='searching'),
	path('checkout',login_required(views.CheckoutView.as_view(),login_url='/auth/login'),name='checkout'),
	path('checkout/<int:pk>',login_required(views.SpecificCheckoutView.as_view(),login_url='/auth/login'),
		name='single_checkout'),

]