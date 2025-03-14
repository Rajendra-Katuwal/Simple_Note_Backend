from rest_framework import serializers
from .models import NoteModel


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']


