from django.db import models
# import models from django

# model imports from django 

from django.db.models import Model, CharField, ForeignKey, TextField

# Create your models here.






















class City (Model):
    name = CharField(max_length=250)
    country = CharField(max_length=250)
    picture = CharField(max_length = 1000)
    user = ForeignKey(User, on_delete=models.CASCADE,related_name="cities")



class Post (Model): 
    title = CharField(max_length = 500)
    content = TextField(max_length=10000)
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    city = ForeignKey(City, on_delete=models.CASCADE, related_name="posts")
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['created_at']



