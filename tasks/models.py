from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Task(models.Model): 
    #title = models.CharField(max_length=250)
    title = RichTextField(max_length=255)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.title
