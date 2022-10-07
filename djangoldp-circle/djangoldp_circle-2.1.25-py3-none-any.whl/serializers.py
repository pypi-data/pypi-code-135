from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from djangoldp.serializers import LDPSerializer
from djangoldp_circle.models import Circle, CircleAccessRequest


class CircleAccessRequestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleAccessRequest
        fields = '__all__'


class CircleModelSerializer(LDPSerializer):
    class Meta:
        model = Circle
        fields = '__all__'

    # _status = serializers.SerializerMethodField('get_status_transalted')

    def get_status_translated(self, obj):
        return _(obj.status)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['_status'] = self.get_status_translated(instance)
        return rep
