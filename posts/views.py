from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def posts(request):
    data = ["Iran Israel War",
            "Pak Afghan War",
            "Naseem Shah vs PMLN"]
    template = loader.get_template('list.html')
    context = {
        'news': data,
    }
    return HttpResponse(template.render(context, request))
