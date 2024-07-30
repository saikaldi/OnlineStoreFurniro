from django.db import models
from goods.models import Products
from users.models import User
# Create your models here.

class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created Timestamp')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    objects=CartQuerySet.as_manager()

    def product_price(self):
        return round(self.product.price*self.quantity, 2)

    def __str__(self):
        return f'Cart: {self.user.username} | Products: {self.product.name} | Quantity: {self.quantity}'

