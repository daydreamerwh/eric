#urls.py
from django.conf.urls import include,url
import blog.views

urlpatterns = [
    
    url(r'^$',blog.views.archive),
#    url(r'foo/',foo),
#    url(r'bar/',bar),
]
