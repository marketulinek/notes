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
