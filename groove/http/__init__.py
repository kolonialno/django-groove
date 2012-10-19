import json

from django.conf import settings
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    """
    Returns a HTTP response with JSON content type. Performs automatic
    serialization if given an object.
    """

    def __init__(self, obj=None, **kwargs):

        # Perform JSON serialization
        if obj:
            # Pretty print in debug mode
            indent_level = 4 if settings.DEBUG else 0
            content = json.dumps(obj, indent=indent_level)
        else:
            content = ''

        # Content type and status code for the response
        content_type = 'application/json; charset=%s' % settings.DEFAULT_CHARSET
        status_code = kwargs.get('status', 200)

        # Return response as JSON
        super(JsonResponse, self).__init__(
            content,
            content_type=content_type,
            status=status_code
        )
