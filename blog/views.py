from django.shortcuts import render_to_response

# Create your views here.

from django.http import HttpResponse

from django.template import loader, Context

from blog.models import BlogPost

def archive(request):
         posts = BlogPost.objects.all()
         return render_to_response('archive.html',{'posts':posts})
