<h2>To create a custom user model with name 'CustomUser' add following  lines:</h2>



<h3>Within app named 'api'</h3>

<ul>
<h4>models.py</h4>

 ```
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
 ```


<h4>admin.py</h4>

 ```
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class MyUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('phone_number',)}),)

admin.site.register(CustomUser, MyUserAdmin)
 ```
</ul>



<h3>Within main project app folder</h3>

<ul>
<h4>settings.py</h4>

 ```
AUTH_USER_MODEL = 'api.CustomUser'
 ```
</ul>