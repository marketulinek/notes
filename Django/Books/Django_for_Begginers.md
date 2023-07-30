# DJANGO FOR BEGGINERS

## Page: 58 - Tests
- SimpleTestCase - database not necessary
- TestCase - test with database
- TransactionTestCase - test database transactions
- LiveServerTestCase - launches a live server thread for test with tools like Selenium

## Page: 78 - Migrations
```
python manage.py makemigrations
```
This will create migration file for **ALL** available changes throughout the Django projects (and all apps in it)
Migration file should be as small and concise as possible as this makes it easier to debug in the future or even rollback changes as needed.

**Better approach:**
```
python manage.py makemigrations <app_name>
```

## Page: 82 - Tips & Tricks
```
class Post(models.Model):
  def __str__(self):
    return self.text[:50]
```

## Page: 87 - Setting up DB for testing
`setUpTestData()` is much faster than using the `setUp()` because it creates the test data only once per test case rather than per test.

## Page: 119
```
def ...(self):
  no_response = self.client.get('/post/10000/')
  self.assertEqual(no_response.status_code, 404)
```

## Page: 163 - Custom user model
Look in the book...

## Page: 166 - Char/Text File and NULL, BLANK
`CharField` or `TextField` - setting both null and blank will result in two possible values for "no data" in the database.
Which is a bad idea. The Django convention is instead to use the empty string `""`, not `NULL`.

## Page: 212 - Password Reset
*settings.py*
```
EMAIL_BACKEDN = "django.core.mail.backends.console.EmailBackend"
```

## Page: 228 - Custom Emails
```
django/contrib/admin/templates/registration/password_reset_email.html
+ templates/registration/password_reset_email.html
+ templates/registration/password_reset_subject.txt
```

## Page: 252 - Automatically set current logged-in user as author
```
class ArticleCreateView(CreateView):
  ...
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
```

## Page: 282 - Wrapper View
Single URL must behave differently based on the user request (GET, POST, etc) or even the format (returning HTML vs JSON).

## Page: 283 - SingleObjectMixin
Look in the book...
