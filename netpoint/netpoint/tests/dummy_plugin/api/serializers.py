from rest_framework.serializers import ModelSerializer
from netpoint.tests.dummy_plugin.models import DummyModel


class DummySerializer(ModelSerializer):

    class Meta:
        model = DummyModel
        fields = ('id', 'name', 'number')
