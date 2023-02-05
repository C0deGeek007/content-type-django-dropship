from django.urls import path

from . import views
from graphene_django.views import GraphQLView
# from .schema import schema
from django.views.decorators.csrf import csrf_exempt
from .graphql.schema import schema

urlpatterns = [
    path("gql", csrf_exempt(views.PrivateGraphQLView.as_view(graphiql=True, schema = schema ))),
]