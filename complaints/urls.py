from django.urls import path
from complaints.views import SignUpView
from rest_framework.authtoken.views import ObtainAuthToken
from complaints.views import ComplaintListCreateView,ComplaintRetrieveUpdateDeleteView
from complaints.views import ComplaintSummaryView

urlpatterns=[
    path("signup/",SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("complaint/",ComplaintListCreateView.as_view()),
    path("<int:pk>/",ComplaintRetrieveUpdateDeleteView.as_view()),
    path("summary/",ComplaintSummaryView.as_view())
]