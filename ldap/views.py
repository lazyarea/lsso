from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

import sys
#from ldap.management.commands.ldapcli import *


# Create your views here.
def index(request):
    #print(sys.path)
    #l = ldapcli()
    #sample()
    # return HttpResponse("Hello, world. You're at the news index.")
    latest_question_list = []
    template = loader.get_template('ldap/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def added(request):

    print(settings.LDAP_AUTH_SEARCH_BASE)
    return HttpResponse("added.")
