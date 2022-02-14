from django.db import models


# Create your models here.

from djnago.contrib.auth import get_user_model
User = get_user_model()

class ContactUser(models.Model):
    user = models.ForeignKey(User,related_name='usernames',blank=False,null=False,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    comment = models.CharField(max_length=1028, blank=False, null=False)


    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('')
