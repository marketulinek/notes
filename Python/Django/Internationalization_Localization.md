# :earth_africa: Internationalization and localization :world_map:
https://docs.djangoproject.com/en/4.2/topics/i18n/

## Setting the project :hammer:
Activate translation in `settings.py`
```
MIDDLEWARE = [
    ...
    "django.middleware.locale.LocaleMiddleware",
    ...
]

LOCALE_PATHS = ['locale']
LANGUAGES = [
    ['en', 'English'],
    ['cs', 'Čeština']
]
```
## Usage :magic_wand:
### Python code
```
from django.http import HttpResponse
from django.utils.translation import gettext as _


def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
```
### Template code
`{% load i18n %}` needs to be loaded in all templates (at the top of a file) which use translations, even those templates that extend from other templates which have already loaded the **i18n** tag.
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
## Contextual markers
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

## Translating URL patterns
https://docs.djangoproject.com/en/4.2/topics/i18n/translation/#translating-url-patterns

