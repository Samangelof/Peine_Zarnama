from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def to_representation(self, instance):
        return {
            'status': status.HTTP_201_CREATED,
            'message': 'Пользователь успешно зарегистрирован.'
        }


class TokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = CustomUser.objects.filter(email=email).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return {
                    'email': email,
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }
            else:
                raise serializers.ValidationError("Неверные учетные данные")
        else:
            raise serializers.ValidationError("Должны быть указаны 'email' и 'password'")
