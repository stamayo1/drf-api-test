from rest_framework import serializers
from .models import Enterprise, Code

class EnterpriseSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Enterprise
        fields = '__all__'
        
class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Code
        fields = '__all__'
        

class EnterpriseNitSerializer(serializers.ModelSerializer):
    codes = serializers.SerializerMethodField('get_items')

    class Meta:
        model = Enterprise
        fields = ('id', 'name', 'nit', 'gln', 'codes') 

    def get_items(self, enterprise):
        items = Code.objects.filter(owner=enterprise)
        serializer = CodeSerializer(items, many=True)
        return serializer.data