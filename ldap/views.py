from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the news index.")
    latest_question_list = []
    template = loader.get_template('ldap/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def added(request):
    return HttpResponse("added.")
