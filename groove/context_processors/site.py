from django.contrib.sites.models import Site, RequestSite


def current_site(request):
    """
    A context processor to add the current Django Site object to the Context,
    with RequestSite fallback.
    """

    context = {}

    try:
        current_site = Site.objects.get_current()
        context['site'] = current_site

    except Site.DoesNotExist:
        context['site'] = RequestSite(request)

    return context
