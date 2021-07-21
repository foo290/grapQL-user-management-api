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
    pass
