from django.db import models
# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(('email address'), unique=True)
    user_password = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=12)
    USERNAME_FIELD = 'email'
    # def __str__(self):
    #     return "{}".format(self.user_name)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at', )
