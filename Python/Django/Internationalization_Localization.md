# :earth_africa: Internationalization and localization :world_map:
https://docs.djangoproject.com/en/4.2/topics/i18n/

## Setting the project :hammer:
Activate translation in `settings.py`
```
MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]

# Numbers and dates using the format of the current locale
USE_L10N = True
# Datetimes will be timezone-aware
USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
LANGUAGES = [
    ['en', 'English'],
    ['cs', 'Čeština']
]
```
Language prefix in URL patterns:
https://docs.djangoproject.com/en/4.2/topics/i18n/translation/#module-django.conf.urls.i18n

```
# Example of <project_name>/urls.py

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
)

```

## Usage :magic_wand:
:warning: **Note:** I should almost always use `gettext_lazy` when I'm in the global scope.
### Python code
```
from django.http import HttpResponse
from django.utils.translation import gettext as _


def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
```
### Template code
`{% load i18n %}` needs to be loaded in all templates (at the top of a file) which use translations,
even those templates that extend from other templates which have already loaded the **i18n** tag.
```
<title>{% translate "This is the title." %}</title>
<title>{% translate myvar %}</title>
```

## Message files :scroll:
### Creating
```
django-admin makemessages -l cs
```
…where `cs` is the locale name for the message file I want to create.
### Compiling
```
django-admin compilemessages
```
## Comments for translators :speech_balloon:
```
def my_view(request):
    # Translators: This message appears on the home page only
    output = gettext("Welcome to my site.")
```
and in template
```
{% comment %}Translators: View verb{% endcomment %}
{% translate "View" %}

# or

{# Translators: Label of a button that triggers search #}
<button type="submit">{% translate "Go" %}</button>
```

## Contextual markers :information_source:
```
from django.utils.translation import pgettext

month = pgettext("month name", "May")
```
and in template
```
{% translate "May" context "month name" %}
```

## Lazy translation
https://docs.djangoproject.com/en/4.2/topics/i18n/translation/#lazy-translation

