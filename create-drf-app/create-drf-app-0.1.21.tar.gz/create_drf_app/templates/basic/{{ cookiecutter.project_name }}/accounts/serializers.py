from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers


Account = get_user_model()


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name',)


class CreateAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('email', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        account = Account.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
                
        return account