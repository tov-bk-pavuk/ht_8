from django.utils import timezone

from ..models import Logs


timestamp = timezone.now()


def wrap_log(get_response):
    # One-time configuration and initialization.

    def logging(request):
        if request.path.startswith('/admin') is False:
            if request.method == 'GET':
                Logs.objects.create(path=request.path,
                                    timestamp=timestamp, method='GT')
            elif request.method == 'POST':
                Logs.objects.create(path=request.path,
                                    timestamp=timestamp, method='PS')
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    return logging
