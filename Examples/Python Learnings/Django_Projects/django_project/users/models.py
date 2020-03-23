from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return "{0} Profile".format(self.user.username)

    '''
    #Below function is for resizing the image on the file system , if the uploaded image is of higher resolution
    #Currently it is commented as we are using S3 for storage now (earlier it was local file system), and there are 
    #some changes required in the code
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''
