from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from siteapp.models import Page

def page(request, slug='home'):
    p = get_object_or_404(Page, slug=slug)
    return render_to_response('page.html', {'page': p,})