from rest_framework import serializers
from .models import Detail

class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'regNO', 'post', 'department', 'period', 'salary')
        model = Detail