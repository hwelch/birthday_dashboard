from django.shortcuts import render
from rest_framework import generics
from .serializers import PersonSerializer, RelationSerializer
from .models import Person, Relation
# Create your views here.

# creating a sample view to test with
class PersonView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RelationView(generics.CreateAPIView):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
