from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import JsonResponse
import json
from textblob import TextBlob
from django.contrib import messages

from .models import Product,Comments
from .forms import CommentForm, CheckoutForm

class HomeView(View):
	def get(self,request):
		products = Product.objects.all()
		return render(request,'landing/home.html',{'products':products})


class SpecificView(View):
	def get(self,request, pk):
		if request.is_ajax():
			return self.ajax_response(request,pk)
		form = CommentForm()
		product = get_object_or_404(Product,pk=pk)
		comments = Comments.objects.filter(product=product).order_by('-sentiment').all()
		return render(request,'landing/specific.html',{'product':product,'comments':comments,'form':form})

	def ajax_response(self,request,pk):
		try:
			request.user.cart_set.add(get_object_or_404(Product,pk=pk))
			request.user.num_added += 1
			request.user.save()
			response = {"success": True}
			return JsonResponse(response)
		except:
			return JsonResponse({'success':False})

	def post(self,request,pk):
		form = CommentForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			senti = TextBlob(text).sentiment.polarity
			prod = get_object_or_404(Product,pk=pk)
			c = Comments(text=text,sentiment=senti,user=request.user,product=prod)
			c.save()
		messages.success(request,"Your comment has been added")
		return redirect('specific',pk=pk)



class CartView(View):
	def get(self,request):
		if request.is_ajax():
			return self.ajax_response(request)
		products = request.user.cart_set.all()
		return render(request,'landing/cart.html',{'products':products})

	def ajax_response(self,request):
		data = request.GET
		product = get_object_or_404(Product,pk=data['pk'])
		if data['type'] == 'buy':
			request.user.num_bought += 1
			request.user.bought_set.add(product)
		elif data['type'] == 'remove':
			request.user.num_discarded += 1
		request.user.cart_set.remove(product)
		request.user.save()
		self.update_user_score(request)
		# self.update_product_score()
		return JsonResponse({})

	def update_user_score(self,request):
		u = request.user
		s = 0
		s += u.num_bought*0.2
		s -= u.num_discarded*0.1
		total_price = 0
		for product in u.bought_set.all():
			total_price += product.price
		s += total_price*0.001
		if u.age:
			s += u.age*0.01
		u.score = s
		u.save()


class CheckoutView(View):
	def get(self,request):
		form = CheckoutForm()
		products = request.user.cart_set.all()
		total = 0
		shipping = 0 
		for product in products:
			total += product.price
			shipping += product.shipping_cost
		context = {
			'form': form,
			'total': total,
			'shipping':shipping,
			'products' : products

		}
		return render(request,'landing/checkout.html',context)

	def post(self,request):
		form = CheckoutForm(request.POST)
		if form.is_valid():
			messages.success(request,"This product will be shipped as soon as possible")
			for product in request.user.cart_set.all():
				request.user.cart_set.remove(product)
			return redirect('home')
		messages.warning("Invalid submission of form")
		return redirect('checkout')


class SpecificCheckoutView(View):
	def get(self,request,pk):
		form = CheckoutForm()
		products = get_object_or_404(Product,pk=pk)
		total = products.price
		shipping = products.shipping_cost
		context = {
			'form': form,
			'total': total,
			'shipping':shipping,
			'products' : [products]
		}
		return render(request,'landing/checkout.html',context)

	def post(self,request,pk):
		form = CheckoutForm(request.POST)
		if form.is_valid():
			messages.success(request,"This product will be shipped as soon as possible")
			request.user.cart_set.remove(get_object_or_404(Product,pk=pk))
			return redirect('home')
		messages.warning("Invalid submission of form")
		return redirect('checkout')



class SearchView(View):
	def get(self,request):
		print(request.GET['text'])
		products = Product.objects.filter(name__contains=request.GET['text']).all()
		return render(request,'landing/home.html',{'products':products})



