from django.db import models

# Create your models here.
class Article(models.Model):
    '''Encapsulates the data of a blog Article by an author'''

    #define the data attributes (fields) of the Article object:
    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a String Representation of this model instance (row)'''
        return f'{self.title} by {self.author}'