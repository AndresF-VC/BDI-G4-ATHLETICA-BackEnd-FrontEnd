"""
    This module provides the serializers for the Core API:

* Serializes and deserializes user data (CustomUser), handling secure password creation.
* Serializes athlete participations in events, including event and discipline names.
* Serializes athlete data, mixing read-only fields (related names) and write fields (foreign keys).
* Includes a custom serializer to issue JWT tokens with additional information (username and role).
* Adds read-only serializers for nationalities, categories, and clubs, as well as an extended athlete detail serializer.

"""

from rest_framework import serializers
from users.models import CustomUser 
from .models import Athletes, Participations, Nationalities, Categories, Clubs, Disciplines
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# --- SERIALIZER DE USUARIO ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            role=validated_data.get('role', 'guest')
        )
        return user

# --- SERIALIZER DE PARTICIPACIONES ---
class ParticipationSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name', read_only=True)
    discipline_name = serializers.CharField(source='discipline.name', read_only=True)

    class Meta:
        model = Participations
        fields = ['participation_id', 'event_name', 'discipline_name', 'position', 'result']

# --- SERIALIZER DE ATLETAS ---
class AthleteSerializer(serializers.ModelSerializer):
    nationality_name = serializers.CharField(source='nationality.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    club_name = serializers.CharField(source='club.name', read_only=True)
    participations = ParticipationSerializer(many=True, read_only=True)

    # Campos para escribir (sin el 'source' redundante)
    nationality = serializers.PrimaryKeyRelatedField(queryset=Nationalities.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())
    club = serializers.PrimaryKeyRelatedField(queryset=Clubs.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Athletes
        fields = [
            'athlete_id', 'name', 'birth_date', 'gender',
            'nationality_name', 'category_name', 'club_name', 'participations',
            'nationality', 'category', 'club', 
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        user = request.user if request else None
        
        if not user or not user.is_authenticated:
            representation.pop('participations', None)
            
        return representation
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = user.role
        return token
    
class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationalities
        fields = ['nationality_id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_id', 'name']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['club_id', 'name']

class AthleteDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the athlete detail view.
    """
    nationality_name = serializers.CharField(source='nationality.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    club_name = serializers.CharField(source='club.name', read_only=True)
    participations = ParticipationSerializer(many=True, read_only=True)

    class Meta:
        model = Athletes
        fields = [
            'athlete_id', 'name', 'birth_date', 'gender',
            'nationality_name', 'category_name', 'club_name',
            'participations',
            'nationality', 'category', 'club'
        ]
