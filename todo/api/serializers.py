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
        pass

    def update(self, instance, validated_data):
        pass
