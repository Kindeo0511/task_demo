from rest_framework import serializers
from tasks.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required = True,
        allow_blank = False,
        error_messages = {
            'required': 'Title is required.',
            'blank': 'Title cannot be blank.'
        }
    )
    description = serializers.CharField(
        required = True,
        allow_blank=False,
        error_messages = {
            'required': 'Description is required.',
            'blank': 'Description cannot be blank'
        }
    )

    
    class Meta:
        model = Tasks
        fields = '__all__'