import graphene
from .input import ProjectInput, CommentInput
from .type import ProjectType, CommentType
from .. import models


class createProject(graphene.Mutation):
    class Arguments:
        input = ProjectInput(required=True)

    ok = graphene.Boolean()
    project = graphene.Field(lambda: ProjectType)

    def mutate(root, info, input):
        try:
            commentInput = input["comment"]
            del input["comment"]
            project = models.ProjectModel.objects.create(**input)
            comment = models.Comment(content_object=project, body=commentInput)
            comment.save()
            print(comment)
            # response = {}
            return createProject(ok=True, project=project)
        except Exception as e:
            print(e)
            return createProject(ok=False)

class createComment(graphene.Mutation):
    class Arguments:
        input = CommentInput(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(lambda:CommentType )

    def mutate(root, info, input):
        project = models.ProjectModel.objects.get(pk=input["projectId"])
        del input["projectId"]
        comment = models.Comment(content_object=project, body=input["body"])
        comment.save()
        return createComment(ok=True, comment=comment )


class Mutation(graphene.ObjectType):
    create_project = createProject.Field()
    create_comment = createComment.Field()