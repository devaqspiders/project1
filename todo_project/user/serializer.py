from rest_framework.serializers import ModelSerializer
from user.models import MyUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['user_name', 'user_email', 'profilephoto', 'password']
    
    def create(self,validate_data):
        return MyUser.objects.create_user(**validate_data)