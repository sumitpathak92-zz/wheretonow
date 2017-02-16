from django.http import HttpResponse
from serializers import CategoriesSerializers
from models import Categories
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.template import RequestContext


class IndexView(TemplateView):
    template_name = 'first_maps.html'

    def home_page(request):
        return render_to_response('first_maps.html', {}, context_instance=RequestContext(request))

class GetCategoriesAPIView(APIView):
    """
    Returns all the Categories of places listed in the Google Map API
    """
    def get(self, request):
        print "get called"
        categories = Categories.objects.all()
        category_serializer = CategoriesSerializers(categories, many=True)
        return Response(category_serializer.data)