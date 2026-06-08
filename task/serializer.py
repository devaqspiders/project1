from rest_framework.serializers import ModelSerializer
from task.models import Task
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['t_id','t_name', 't_desc', 'priority', 'user_data']
    def create(self, validate_data):
        return Task.objects.create(**validate_data)