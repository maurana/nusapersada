from rest_framework import serializers
from v1.models.profiles import Profiles

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'