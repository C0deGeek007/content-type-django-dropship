import graphene
from . import type
from .. import models


class Query(graphene.ObjectType):
    allProject = graphene.List(type.ProjectType)
    commentsOnProject = graphene.List(type.CommentType, projectId=graphene.ID())

    def resolve_allProject(root,info):
        allProject = models.ProjectModel.objects.all()
        return allProject

    def resolve_commentsOnProject(root, info, projectId):
        try:
            project = models.ProjectModel.objects.get(pk=projectId)
            commentsList = project.comments.all()
        except Exception as e:
            print("inside exception")
            print(e)
        return commentsList