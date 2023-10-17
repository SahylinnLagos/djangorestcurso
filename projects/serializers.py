from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        field=('id','title','description','technology','created_at')
        read_only_fields=('created_at',)
        fields = '__all__'