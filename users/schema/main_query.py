import graphene
from .query_mutations import Mutation

from graphql_auth.schema import UserQuery, MeQuery


class QueryType(UserQuery, MeQuery, graphene.ObjectType):
    """
    This is the schema root, everything here is handled in parent classes.
    """
    pass


schema = graphene.Schema(
    query=QueryType,
    mutation=Mutation
)
