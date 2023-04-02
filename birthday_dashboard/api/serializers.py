from rest_framework import serializers
from .models import Relation, Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'birthday', 'gift_ideas', 'relation', 'notes', 'user')

class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ('id', 'name')
