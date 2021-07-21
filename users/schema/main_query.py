import graphene
from .query_mutations import Mutation

from graphql_auth.schema import UserQuery, MeQuery


class QueryType(UserQuery, MeQuery, graphene.ObjectType):
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


schema = graphene.Schema(
    query=QueryType,
    mutation=Mutation
)
