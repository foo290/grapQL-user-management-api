import graphene
from django.contrib.auth import get_user_model

from graphql_auth import mutations

USER = get_user_model()


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    update_user = mutations.UpdateAccount.Field()
    delete_user = mutations.DeleteAccount.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_pw_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    """
    This is the root of mutation schema, This class is used in main_query for exposing mutable endpoints.

    # Creating a User:
    ------------------------------------------------
        mutation{
          register(
            email:"myEmail@gmail.com"
            username:"myUsername"
            password1:"testing321"
            password2:"testing321"
          )
          {
            success
            errors
            token
            refreshToken
          }
        }

    # Reading data:
    ------------------------------------------------
        query{
            users(username:"admin"){
            edges{
              node{
                username
                lastName
                firstName
                lastLogin
              }
            }
          }
        }

        query{
          me{
            lastName
            firstName
            verified
            isActive
          }
        }

    # Updating user
    -------------------------------------------------
        ##Needs JWT token as authentication header for unauthenticated accounts
        mutation{
          updateUser(firstName:"new name")
          {
            success
            errors
          }
        }

    #Delete User
    --------------------------------------------------
        ##Will delete the current logged in account
        mutation{
          deleteUser(password:"mypw"){
            success
            errors
          }
        }

    """
    pass
