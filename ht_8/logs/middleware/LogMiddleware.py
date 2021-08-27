from ..models import Logs
import time

timestamp = time.monotonic()


def wrap_log(get_response):
    # One-time configuration and initialization.

    def logging(request):
        if request.method == 'GET':
            Logs.objects.create(path=request.path,
                                timestamp=timestamp, method='GT')
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    return logging
