from django.http import Http404


def superuser_required(function):
    """
    Limit a view to superusers. Raises a 404 if user is not a superuser, security
    through obscurity.

    Usage in views:
        @superuser_required
        def index(request):
            ...


    Usage in URL config:
        url(r'^$', superuser_required('views.index'), name='index'),
    """

    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404('Superusers only.')
        return function(request, *args, **kwargs)
    return _inner
