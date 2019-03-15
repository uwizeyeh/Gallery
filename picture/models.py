from django.db import models

# Create your models here.
class Location(models.Model):
    country_name = models.CharField(max_length =30)
    city_name = models.CharField(max_length =30)

    def __str__(self):
        return self.country_name

    class Meta:
        ordering = ['country_name']
    
class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    title = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def filter_category(cls,query):
        images = cls.objects.filter(category=query)
        return images    

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(category__category__icontains = search_term)
        return images
