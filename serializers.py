from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializers):
    password = serializers,CharField(write_omly=True, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password"
        )