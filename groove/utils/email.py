import logging

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_unicode

logger = logging.getLogger(__name__)


def send_html_email(recipients, template_prefix=None, context={}, from_address=None, headers={}):
    """
    Sends an email with text and HTML content.
    """

    # Ensure the recipients are a list
    if not type(recipients) == list:
        recipients = [recipients]

    # Set default from address
    if from_address is None:
        from_address = settings.DEFAULT_FROM_EMAIL

    # Add current site to context if not present
    if not 'site' in context:
        context['site'] = Site.objects.get_current()

    # Media and static URLs with or without domain prefix
    if not 'MEDIA_URL' in context:
        if settings.MEDIA_URL.startswith('http:'):
            context['MEDIA_URL'] = settings.MEDIA_URL
        else:
            context['MEDIA_URL'] = 'http://%s%s' % (Site.objects.get_current().domain, settings.MEDIA_URL)

    if not 'STATIC_URL' in context:
        if settings.STATIC_URL.startswith('http:'):
            context['STATIC_URL'] = settings.STATIC_URL
        else:
            context['STATIC_URL'] = 'http://%s%s' % (Site.objects.get_current().domain, settings.STATIC_URL)

    # Render templates
    subject = render_to_string(template_prefix + '_subject.txt', context).strip()
    text_content = render_to_string(template_prefix + '.txt', context)
    html_content = render_to_string(template_prefix + '.html', context)

    # Ensure there are no newlines in subject
    subject = ' '.join(subject.splitlines())

    # In case the text used lazy version of ugettext
    subject = force_unicode(subject)

    # Compose and send the email
    msg = EmailMultiAlternatives(subject, text_content, from_address, recipients, headers=headers)
    msg.attach_alternative(html_content, 'text/html')

    # Try to send mail, log exceptions
    try:
        msg.send(fail_silently=False)
    except Exception as ex:
        logger.exception('Sending email to %s with subject "%s" failed.' % (recipients, subject))
        return False

    return True
