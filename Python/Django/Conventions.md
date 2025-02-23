# Import order

*Source:* Two Scoops of Django book

- Standard library imports

- Imports from core Django

- Imports from third-party apps including those unrelated to Django

- Imports from the apps that I created as part of my Django project


# Model style

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style

The order of model inner classes and standard methods:

- All database fields

- Custom manager attributes

- `class Meta`

- `def __str__()` and other Python magic methods

- `def save()`

- `def get_absolute_url()`

- Any custom methods
