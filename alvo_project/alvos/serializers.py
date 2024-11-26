from rest_framework import serializers
from .models import Alvo

class AlvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alvo
        fields = '__all__'
