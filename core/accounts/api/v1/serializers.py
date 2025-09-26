from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ...models import User
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=30, write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError('Passwords did not match')
        try:
            validate_password(attrs.get('password'))
        except Exception.ValidationError as e:
            raise serializers.ValidationError({'email': list(e.messages)})
        return super().validate(attrs)
    def create(self, validated_data):
        validated_data.pop('password1', None)
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('email', 'password','password1')


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password
            )
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError({'non_field_errors': [msg]}, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError({'non_field_errors': [msg]}, code='authorization')

        attrs['user'] = user
        return attrs
