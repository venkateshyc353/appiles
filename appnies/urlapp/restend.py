from rest_framework import serializers
from . models import url_model

class rest_api(serializers.ModelSerializer):
    class Meta:
        model=url_model
        fields='__all__'
