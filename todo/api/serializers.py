from rest_framework import serializers
from todo.models import TodoList
from django.contrib.auth.models import User

from datetime import datetime 
from django.utils.timesince import timesince

#THIS IS MODEL SERIALIZERS
class TodoListSerializers(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    todo_user = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = TodoList
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def get_time_since_pub(self, object):
        now = datetime.now().astimezone()
        pub_date = object.created_at
        time_delta = timesince(pub_date, now)
        return time_delta


class UserSerializers(serializers.ModelSerializer):
    # todolist = TodoListSerializers(many=True, read_only = True)
    todolist = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='todolist_detail',
    )
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password', 'groups', 'user_permissions', 'is_superuser', 'date_joined', 'is_staff']
        read_only_fields = ['id']


## THIS IS DEFAULT SERIALIZERS
class TodoListDefaultSerializers(serializers.Serializer):
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
