from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'age')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'profile',
                  'is_active',
                  'is_staff',
                  'password',
                  'last_login',
                  'created_at',
                  'updated_at'
                  )
        read_only_fields = ('id', 'is_active', 'is_staff', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True,}
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(username=None, **validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
