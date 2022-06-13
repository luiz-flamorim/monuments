from rest_framework import serializers
from spmap.models import Monument

class MonumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monument
        fields = ['data','data_more_info','nome','genero','etinia','endereco','lat','long','tombado','link','iphan','fonte','tipo','material','condeph','conpres','autor','endereco_original']