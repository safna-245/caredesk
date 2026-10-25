from rest_framework import serializers
from complaints.models import Complaint
from django.contrib.auth.models import User

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:

        model = Complaint
        fields="__all__"
        read_only_fields = ["id","reported_date","user"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ["id","username","first_name","last_name","email","password"]
        read_only_fields = ["id"]



