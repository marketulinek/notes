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

# Update it to a generic name, English (en)
LANGUAGE_CODE = 'en'

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
Language prefix in URL patterns in `<project_name>/urls.py`
([documentation](https://docs.djangoproject.com/en/4.2/topics/i18n/translation/#module-django.conf.urls.i18n))

```
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
django-admin makemessages [--ignore=venv / -i "venv"] -l cs
```
…where `cs` is the locale name for the message file I want to create.
### Compiling
```
django-admin compilemessages [-i "venv"]
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

## Miscellaneous
### The set_language redirect view
Activate by adding `path("i18n/", include("django.conf.urls.i18n"))` to URLconf in `<project_name>/urls.py`.

:warning: **Warning:** don’t include the above URL within **i18n_patterns()** - it needs to be language-independent itself to work correctly.
```
{% load i18n %}

<form action="{% url 'set_language' %}" method="post">{% csrf_token %}
    <input name="next" type="hidden" value="{{ redirect_to }}">
    <select name="language">
        {% get_current_language as LANGUAGE_CODE %}
        {% get_available_languages as LANGUAGES %}
        {% get_language_info_list for LANGUAGES as languages %}
        {% for language in languages %}
            <option value="{{ language.code }}"{% if language.code == LANGUAGE_CODE %} selected{% endif %}>
                {{ language.name_local }} ({{ language.code }})
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="Go">
</form>
```
