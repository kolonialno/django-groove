from django.conf import settings
from django.utils import translation
from haystack.indexes import SearchField


class L10NCharField(SearchField):
    """
    Translatable CharField for django-haystack.

    Since the building of search indexes is triggered by management commands,
    and they are in the en_US locale by default, we need to explicitly activate
    the current translation to have translated URLs in the search results.

    More information:
    https://github.com/toastdriven/django-haystack/issues/609
    """

    def prepare_template(self, obj):
        translation.activate(settings.LANGUAGE_CODE)
        return super(L10NCharField, self).prepare_template(obj)
