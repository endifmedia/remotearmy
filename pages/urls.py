from django.urls import path

from .views import MembershipPageView

urlpatterns = [
    path('membership/', MembershipPageView.as_view(), name='membership'),
]