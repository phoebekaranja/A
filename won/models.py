from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    design=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    usability=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    content=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    comment =models.TextField(max_length=50,null=True)
class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profile/')
    profile = models.ForeignKey(User, null=True)
    bio = models.TextField(max_length = 100)
    contact = models.IntegerField(null=True)
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Comment(models.Model):
    comment = models.CharField(max_length = 400)            