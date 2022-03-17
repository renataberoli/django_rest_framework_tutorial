import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpResponse -> Django
    # request.body
    print(request.GET) # url query params

    body = request.body #byte string of Json data
    data = {}
    try:
        data = json.loads(body) # string of Json data -> Python Dict
    except:
        pass

    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    print(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)