from django.http import HttpResponse

from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def hello(request):
    return HttpResponse('Hello World!')


@csrf_exempt
def page_not_found(request):
    return render_to_response('blog/404.html')


@csrf_exempt
def page_error(request):
    return render_to_response('blog/500.html')