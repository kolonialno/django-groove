from django.contrib.sites.models import Site, RequestSite


def current_site(request):
    """
    A template context processor that adds the current Django Site object to the 
    template context. Uses RequestSite as fallback.
    """

    context = {}

    try:
        context['site'] = Site.objects.get_current()

    except Site.DoesNotExist:
        context['site'] = RequestSite(request)

    return context
