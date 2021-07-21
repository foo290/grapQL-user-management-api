import graphene
from django.contrib.auth import get_user_model

USER = get_user_model()


class CreateUserDataInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class UpdateUserDataInput(graphene.InputObjectType):
    first_name = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String(required=True)
