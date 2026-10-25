from django.shortcuts import render
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from django.contrib.auth.models import User
from complaints.serializers import UserSerializer,ComplaintSerializer
from complaints.models import Complaint
from complaints.permissions import IsOwner

class SignUpView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        return Response( data=serializer_instance.errors)


class ComplaintListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instance = Complaint.objects.filter(user=request.user)

        serializer_instance = ComplaintSerializer(instance,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = ComplaintSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(user=request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class ComplaintRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[IsOwner]

    serializer_class=ComplaintSerializer

    queryset=Complaint.objects.all()


class ComplaintSummaryView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        response_data = {
            "total_complaints": 0
        }

        complaints = Complaint.objects.filter(user=request.user)

        # 20. Unresolved complaints
        unresolved_complaints = complaints.exclude(status="resolved")

        serializer_instance = ComplaintSerializer(unresolved_complaints,many=True)

        response_data["unresolved_complaints"] = serializer_instance.data

        # 21. Total complaints
        total_complaints = complaints.count()

        response_data["total_complaints"] = total_complaints

        # 22. Complaint counts grouped by status
        status_summary = complaints.values("status").annotate(count=Count("id"))

        response_data["status_summary"] = status_summary

        return Response(data=response_data)