from django.db import models
from .utils import code_generator,create_shortcode

class KirrURL(models.Model):
    url = models.CharField(max_length = 200)
    shortcode = models.CharField(max_length = 15, unique = True, blank  = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    Updated = models.DateTimeField(auto_now = True)
    
    
    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode  = code_generator()
        super(KirrURL, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.url)