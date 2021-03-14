from rest_framework import serializers
from . models import session, event

class sessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = session
        fields = ('__all__')


class eventSerializer(serializers.ModelSerializer):
    # sessions = serializers(many=True, queryset=sessions.objects.all())
    sessions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )

    sessions = serializers.StringRelatedField(many=True)

    class Meta:
        model = event
        fields = ('__all__')