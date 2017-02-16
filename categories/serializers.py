from rest_framework import serializers
from models import Categories

class CategoriesSerializers(serializers.Serializer):
    category_type = serializers.CharField(required=False)
    brief_desc = serializers.CharField(required=False)
    google_category_code = serializers.CharField(required=False)
    
    class Meta:
        model = Categories
        fields = ('category_type', 'brief_desc', 'google_category_code')