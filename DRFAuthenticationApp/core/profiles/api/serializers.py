from profiles.models import Profile, ProfileState
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """ Profile for Serializer """

    user = serializers.StringRelatedField(read_only=True)
    # profile = serializers.StringRelatedField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileImageSerializer(serializers.ModelSerializer):
    """ Profile Image for Serializer """

    class Meta:
        model = Profile
        fields = ('image',)


class ProfileStateSerializer(serializers.ModelSerializer):
    """ Profile State for Serializer """

    user_profile = serializers.StringRelatedField(read_only=True)
    # profile_state = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileState
        fields = '__all__'
