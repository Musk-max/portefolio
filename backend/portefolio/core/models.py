from django.db import models

class profiles(models.Model):
    name=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255,null=True)
    work=models.CharField(max_length=255,null=True)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='profiles_image',blank=True, null=True)
    class Meta:
               ordering = ('name',)
               verbose_name_plural = 'profiles' 
    def __str__(self):
        return self.name
