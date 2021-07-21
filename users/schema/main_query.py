import graphene
from .query_type_models import UserType, USER
from .query_mutations import Mutation


class QueryType(graphene.ObjectType):
    """
    This is what read query looks like:
        query {
              user(username or id like-> username:"boopDog") {
                firstName
                lastName
                ... -> fetch fields
              }
            }
    """
    user = graphene.Field(
        UserType,
        id=graphene.String(),
        username=graphene.String()
    )

    @staticmethod
    def resolve_user(*args, **kwargs):
        return USER.objects.filter(**kwargs).first()


schema = graphene.Schema(
    query=QueryType,
    mutation=Mutation
)
