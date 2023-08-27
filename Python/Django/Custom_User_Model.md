# Custom User Model 🧙‍♀️
**Note:** The official Django documentation *higly recommends* [Custom User Model](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project).

## 📃 List of Steps for fresh new project
❗ **NOTE:** Do not make migration or migrate yet ❗
1. The most common way is to start with creating a new app such as users/customers/accounts/...
2. Create new custom user model in `users/models.py`
```
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
```
3. Add new config at the bottom of the `settings.py` which will cause the project to use `CustomUser` instead of the deafult `User` model.
4. Create migration with command `makemigrations` and then `migrate`.
5. User model can be created and edited in Django admin. it is necessary to update the built-in forms to point to new `CustomUser` model in new file `users/forms.py`. The `password` field is implicitly included by default and so does not need to be explicitly named here.
```
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username'
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username'
        )
```
6. Update `users/admin.py` for manipulating user data
```
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'is_superuser'
    ]


admin.site.register(CustomUser, CustomUserAdmin)
```
7. Create `superuser` and check if everything is working fine.
8. Add some tests
```
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser', email='test@user.cz', password='testuser123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@user.cz')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='testadmin', email='test@admin.cz', password='testadmin123'
        )
        self.assertEqual(admin_user.username, 'testadmin')
        self.assertEqual(admin_user.email, 'test@admin.cz')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
```
