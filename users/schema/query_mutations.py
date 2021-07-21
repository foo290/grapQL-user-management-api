import graphene
from .query_input_type import CreateUserDataInput, UpdateUserDataInput
from .query_type_models import UserType
from django.contrib.auth import get_user_model

USER = get_user_model()


class CreateUser(graphene.Mutation):
    """
    Create query will look like:

        mutation first{
          createUser(userData:{
            username:"someusername",
            email:"piglet22@dumdum.com",
            password:"sleep",
            name:"foomi"
            ...
          }) {
            user{
              username
              firstName
              password
              email
              ...
            }
          }
        }

    """

    class Arguments:
        user_data = CreateUserDataInput()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, user_data=None):
        user = USER(
            first_name=user_data.first_name,
            username=user_data.username,
            email=user_data.email,
        )
        user.set_password(user_data.password)
        user.save()
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        update_data = UpdateUserDataInput()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, update_data, id):
        user = USER.objects.filter(id=id)
        if user:
            params = vars(update_data)
            user.update(**{k: v for k, v in params.items() if params[k]})

            return UpdateUser(user=user.first())
        else:
            print('error')
            pass


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        user = USER.objects.get(id=id)
        user.delete()
        return


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
