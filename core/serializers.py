# from core.models import Person
# from django.contrib.auth.models import User, Group
# from rest_framework import serializers
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
#
#
# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = Person
#         fields = ['email', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def save(self):
#         person = Person(
#             email=self.validated_data['email'])
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match'})
#         person.save()
#         return person
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password1 = serializers.CharField(write_only=True)
#
#     class Meta:
#       model = User
#       fields = ('first_name', 'last_name', 'email', 'password','password1',  'user_type',)
#
#     def validate(self, attr):
#        validate_password(attr['password'])
#        return attr
#
#     def create(self, validated_data):
#           user = User.objects.create(
#                 username=validated_data['email'],
#                 user_type=validated_data['user_type'],
#                 email=validated_data['email'],
#                 first_name=validated_data['first_name'],
#                 last_name=validated_data['last_name'],
#
#                 )
#         user.set_password(validated_data['password'])
#         user.save()
#
#
#
#        return user