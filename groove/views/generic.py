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


class ExtraContextTemplateView(TemplateView):
    """
    Extends TemplateView to accept a dictionary of additional context.

    Example usage in URL config:
        url(r'^foo/$', ExtraContextTemplateView.as_view(
            template_name='foo.html', extra_context={'foo': 'bar'})),
    """

    extra_context = None

    def get_context_data(self, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(**kwargs)

        if self.extra_context is not None:
            context.update(self.extra_context)

        return context
