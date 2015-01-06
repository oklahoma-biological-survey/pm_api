
from rest_framework import serializers

from models import Roosts, LuSource

class LuSourceSerializer(serializers.HyperlinkedModelSerializer):
    #code = serializers.HyperlinkedIdentityField()
    class Meta:
        model = LuSource
        fields = ('url','cource', 'comments')


class RoostSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer(required=True)
    class Meta:
        model = Roosts
        fields = ('url', 'name', 'soar_no', 'latitude', 'source','longitude', 'nex2004', 'loc_source_comment')
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)