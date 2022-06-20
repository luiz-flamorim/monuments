from rest_framework import serializers
from spmap.models import Monument
from django.contrib.auth.models import User

class MonumentSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Monument
        fields = ['id','data','data_more_info','nome','genero','etinia','endereco','lat','long','tombado','link','iphan','fonte','tipo','material','condeph','conpres','autor','endereco_original']

class UserSerializer(serializers.ModelSerializer):
    monuments = serializers.PrimaryKeyRelatedField(many=True, queryset=Monument.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'monuments']
        
        
class MonumentGeneric(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monument
        fields = ['id','data','nome','autor','genero','endereco','lat','long','tombado','tipo','material']

