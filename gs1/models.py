from django.db import models

# Create your models here.

class parts(models.Model):

    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    oprice = models.IntegerField()

    objects = [name, image, price, oprice]

    def __str__(self):
        return self.name

class Contact(models.Model):
    cname = models.CharField(max_length=120)
    cemail = models.CharField(max_length=120)
    cphone = models.CharField(max_length=20)
    cmsg = models.TextField()
    timeStamp =models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from : ' + self.cname + ' - ' + self.cemail

