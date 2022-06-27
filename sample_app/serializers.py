from rest_framework.serializers import ModelSerializer
from .models import Student


class Student_serializer(ModelSerializer):
    class Meta:
        model = Student      # model class
        fields = '__all__'

        # def update(self, instance, validated_data):
        #     instance. first_name = validated_data.get('title', instance)
        #     instance.last_name = validated_data.get('title', instance)
        #     instance.message = validated_data.get('text', instance.description)
        #     instance.save()
        #     return instance
        #
