from django.db import models
from django.contrib.auth.models import User

# Product class
class Product(models.Model):
# title
    title = models.CharField(max_length=30)
# url
    url = models.URLField(max_length=200)
# pub_date
    pub_date = models.DateTimeField()
# votes_total
    votes_total = models.IntegerField(default=1)
# image
    image = models.ImageField(upload_to='images/',height_field=None, width_field=None)
# icon
    icon = models.ImageField(upload_to='images/',height_field=None, width_field=None)
# body
    body = models.TextField(max_length=1000)

# pub_date_pretty
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]

# hunter
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
