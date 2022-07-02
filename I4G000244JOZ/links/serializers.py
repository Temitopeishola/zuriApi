#from apischema import serializer
from rest_framework import serializers
from links.models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('target_url','description','identifier','author','created_date','active')

