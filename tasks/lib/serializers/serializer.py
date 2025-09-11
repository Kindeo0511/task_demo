from rest_framework import serializers
from tasks.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required = True,
        error_messages = {
            'blank': 'Title is required.',
            'required': 'Please provide a title.'
        }
    )
    class Meta:
        model = Tasks
        fields = '__all__'