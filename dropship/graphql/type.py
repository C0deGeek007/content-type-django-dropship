import graphene

from ..models import ProjectModel
from graphene_django import DjangoObjectType


class ProjectType(DjangoObjectType):
    class Meta:
        model = ProjectModel
        fields = "__all__"
