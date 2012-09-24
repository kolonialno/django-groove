from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator


class LimitedTemplateView(TemplateView):
    """
    Wrapper around TemplateView generic view with a login required decorator.

    Example usage in URL config:
        url(r'^secret/$', LimitedTemplateView.as_view(template_name='secret.html'), name='secret'),
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LimitedTemplateView, self).dispatch(*args, **kwargs)
