from django.db import models

from logger.models import CustomUser

class Product(models.Model):
	image = models.ImageField(upload_to='products', null=True)
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	shipping_cost = models.IntegerField()
	description = models.TextField()
	score = models.DecimalField(decimal_places=4,max_digits=10,default=0.0)

	cart = models.ManyToManyField(CustomUser, related_name='cart_set', blank=True)
	bought = models.ManyToManyField(CustomUser, related_name='bought_set',blank=True)


	def __str__(self):
		return self.name+" "+str(self.price)



class Comments(models.Model):
	text = models.CharField(max_length=200)
	sentiment = models.DecimalField(decimal_places=4,max_digits=10)
	time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.text+" "+str(self.sentiment)
