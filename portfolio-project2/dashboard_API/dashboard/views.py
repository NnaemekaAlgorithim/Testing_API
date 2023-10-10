from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer

class TeamListView(generics.ListCreateAPIView):
    """
    View for listing and creating Team members.

    Attributes:
        queryset (QuerySet): The queryset containing Team members.
        serializer_class (Serializer): The serializer class to use for Team members.

    Example Usage:
        To list Team members, make a GET request to this view.
        To create a new Team member, make a POST request with the required data.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer  # Use the GenericModelSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a Team member.

    Attributes:
        queryset (QuerySet): The queryset containing Team members.
        serializer_class (Serializer): The serializer class to use for Team members.

    Example Usage:
        To retrieve a Team member, make a GET request to this view with the Team's ID.
        To update a Team member, make a PUT or PATCH request with the updated data.
        To delete a Team member, make a DELETE request with the Team's ID.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer  # Use the GenericModelSerializer
