from rest_framework import serializers
from todo.models import TodoList

class TodoListSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    #user = serializers.ForeignKey()
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
    expected_end_date = serializers.DateTimeField()

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return TodoList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.user = validated_data.get('user', instance.user)
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.expected_end_date = validated_data.get('expected_end_date', instance.expected_end_date)
        instance.save()
        return instance
