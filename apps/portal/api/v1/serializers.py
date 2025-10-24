from rest_framework import serializers
from apps.portal import models



class MilitarySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Military
        fields = ('id', 'rank', 'name', 'nickname', 'admission_date', 'birthdate', 'register', 'activity_status', 'cpf', 'genre', 'email',
                    'father', 'mather', 'place_of_birth', 'phone', 'address', 'number', 'city', 'state', 'office', 'rg', 'entity', )


class MilitaryImageSerializer(serializers.ModelSerializer):
    path_image = serializers.SerializerMethodField(
        '_get_image_path', read_only=True)

    def _get_image_path(self, object):
        return object.image.url

    class Meta:
        model = models.Military
        fields = ('path_image',)