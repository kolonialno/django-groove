import json

from django.conf import settings
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    """
    Provides a JSON response, performing automatic serialization.
    """

    def __init__(self, object=None, **kwargs):

        # Perform JSON serialization
        if object:
            indent_level = 4 if settings.DEBUG else 0
            content = json.dumps(object, indent=indent_level)
        else:
            content = ''

        # Content type and status code for the response
        content_type = 'application/json; charset=%s' % settings.DEFAULT_CHARSET
        status_code = kwargs.get('status', 200)

        # Return response with correct payload/type
        super(JsonResponse, self).__init__(
            content,
            content_type=content_type,
            status=status_code
        )
