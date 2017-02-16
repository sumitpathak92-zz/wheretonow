from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from views import GetCategoriesAPIView

urlpatterns = [
    url(r'^$', views.GetCategoriesAPIView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)