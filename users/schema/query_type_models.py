from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


USER = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = USER
        fields = '__all__'
        # exclude = 'password',
