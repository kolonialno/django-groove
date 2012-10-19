from django.contrib.sites.models import Site, RequestSite


def current_site(request):
    """
    A context processor to add the current Django Site object to the Context,
    with RequestSite fallback.
    """

    context = {}

    try:
        context['site'] = Site.objects.get_current()

    except Site.DoesNotExist:
        context['site'] = RequestSite(request)

    return context
