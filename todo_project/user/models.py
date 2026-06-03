from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
class MyUserManager(BaseUserManager):
    def create_user(self, user_name,user_email, profilephoto, password=None):
        if not user_email:
            raise ValueError("Users must have an email address")
        user = self.model(
            user_email=self.normalize_email(user_email),
            user_name = user_name,
            profilephoto = profilephoto
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
class MyUser(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=250,null=False)
    user_email = models.EmailField(max_length=250,unique=True,null=False)
    profilephoto = models.ImageField(upload_to='userphoto')
    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_name", "user_email","profilephoto"]
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = MyUserManager()
    
    def __str__(self):
        return self.user_email