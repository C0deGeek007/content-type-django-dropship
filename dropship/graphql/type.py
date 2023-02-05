import graphene

from ..models import ProjectModel, Comment
from graphene_django import DjangoObjectType

class CommentType(graphene.ObjectType):
    body = graphene.String()

class ProjectType(DjangoObjectType):
    # comments = graphene.Field(CommentType)
    class Meta:
        model = ProjectModel
        fields = "__all__"

class CommentType(DjangoObjectType):

    class Meta:
        model = Comment
        fields = "__all__"
