from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulates the data of a mini_insta profile'''

    #Define the fields under profile:
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Returns a string representation of the a certain row/model instance'''
        return f'{self.username} A.K.A {self.display_name}'