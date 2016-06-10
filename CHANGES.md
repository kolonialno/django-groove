# Django Groove Changelog

## 0.4.6 (2016-06-10)
* Added new timezone utility method: `datetime_aware`.

## 0.4.5 (2015-05-28)
* Added new timezone utility method: `datetime_midnight_date`.

## 0.4.0 (2014-06-18)
* Added generic view: `ExtraContextTemplateView`.

## 0.3.5 (2014-03-18)
* Added two timezone related utility methods: `datetime_midnight` and `datetime_midnight_today`.

## 0.3.2 (2014-03-06)
* `JsonResponse`: Convert `Decimal` to `float`.

## 0.3.1 (2013-08-21)
* Moved `L10NCharField` from `groove.haystack` to `groove.haystack_fields` since it caused an import error.

## 0.3.0 (2013-08-21)
* Added `L10NCharField` for use with django-haystack.

## 0.2.6 (2013-01-30)
* Added `staff_required` decorator.

[..]
