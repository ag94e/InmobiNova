from django.db import models

# Create your models here.


class usuarios(models.Model):
    name = models.CharField(max_length=30, blank=True, default='unnamed')
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=60, blank=True, null=True)
    address2 = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=10, null=True, blank=True, default="93822")

    def __str__(self):

        return f'Email: {self.email} password: {self.password} address: {self.address} address2: {self.address2} ' \
               f'city: {self.city} country: {self.country} zip: {self.zip}'


class houses(models.Model):
    city = models.CharField(max_length=50, blank=True, default="Sin especificar")
    description = models.CharField(max_length=150, blank=True, default="Sin especificar")
    price = models.FloatField(max_length=20, blank=True, default=0)
    image = models.ImageField(upload_to='gestionpedidos/photos')
    # image = models.CharField(max_length=600, blank=True, default="https://imgurl.me/images/2020/10/28/NOIMAGEabcdc93a3d26c769.png")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
