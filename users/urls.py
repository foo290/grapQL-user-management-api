from django.urls import path
from graphene_django.views import GraphQLView
from users import schema

urlpatterns = [
    path('gql-rest/', GraphQLView.as_view(graphiql=True))
]
