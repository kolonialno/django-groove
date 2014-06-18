# Django Groove

django-groove is a Django app with various utilities, such as a template
context processor that adds the current Django Site object and an utility
method for sending HTML mail.


## Installation

Install `django-groove` (available on PyPi):

	pip install django-groove


## Components

### `groove.auth.decorators`

Two decorators that limits a view with Django User permissions, includes checks
for staff or super users. Raises a 404 if user does not have sufficient
permission, security through obscurity.

Available decorators: `staff_required` and `superuser_required`.

Example usage in views:

    @superuser_required
    def index(request):
        ...

Example usage in URL config:

    url(r'^$', superuser_required('views.index'), name='index'),


### `groove.context_processors.site.current_site`

A template context processor that adds the current Django Site object to the
template context. Uses `RequestSite` as fallback.

Add this to your settings.py:

    from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
    TEMPLATE_CONTEXT_PROCESSORS += (
        'groove.context_processors.site.current_site',
    )

You can now use `{{ site.name }}` and `{{ site.domain }}` in all your templates.


### `groove.email.html.send_html_email`

A shortcut to ease sending of HTML enabled email. Adds current site, media and
static URLs to template context, if not present.

Usage:

    from groove.email.html import send_html_email
    email_sent = send_html_email('foo@example.com', 'account/welcome', {'user': user})

With `template_prefix` as `'account/welcome'`, the following templates
are rendered with `user` variable available:
* account/welcome.txt (plain text version)
* account/welcome.html (HTML version)
* account/welcome_subject.txt (plain text subject, one line only)


### `groove.http.JsonResponse`

An HTTP response class with JSON mime type, optionally dumps given object
to JSON. Also converts datetime and Decimal objects properly.


### `groove.models.abstract.TimestampedModel`

Abstract Django class that automatically timestamps object instances upon
creation and modification.

Inherit from `TimestampedModel` instead of `models.Model` to automatically add
`creation_time` and `modification_time` fields to model.


### `groove.storage.s3`

Defines two `s3boto` storage classes to ease the separation of static and
media files when using Amazon S3.


### `groove.views.generic.LimitedTemplateView`

Wrapper around TemplateView generic view with a login required decorator.

Example usage in URL config:

    url(r'^secret/$', LimitedTemplateView.as_view(
		template_name='secret.html'), name='secret'),


### `groove.views.generic.ExtraContextTemplateView`

Extends TemplateView to accept a dictionary of additional context.

Example usage in URL config:

	url(r'^foo/$', ExtraContextTemplateView.as_view(
		template_name='foo.html', extra_context={'foo': 'bar'})),
