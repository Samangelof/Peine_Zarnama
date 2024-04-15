from rest_framework import serializers
from apps.auths.models import CustomUser
from .models import Message

class UserSerializer(serializers.ModelSerializer):
	_id = serializers.IntegerField(source='id')
	
	class Meta:
		model = CustomUser
		fields = ['username','_id']

class MessageSerializer(serializers.ModelSerializer):
	_id = serializers.IntegerField(source='id')
	is_me = serializers.SerializerMethodField()
	user = UserSerializer()

	class Meta:
		model = Message
		fields = [
			'_id',
			'is_me',
			'text',
			'created',
			'user'
		]

	def get_is_me(self, obj):
		return self.context['user'] == obj.user