import graphene
from .input import ProjectInput
from .type import ProjectType
from .. import models


class createProject(graphene.Mutation):
    class Arguments:
        input = ProjectInput(required=True)

    ok = graphene.Boolean()
    project = graphene.Field(lambda: ProjectType)

    # project = graphene.String()

    def mutate(root, info, input):
        try:
            project = models.ProjectModel.objects.create(**input)
            return createProject(ok=True, project=project)
        except Exception as e:
            print(e)
            return createProject(ok=False)


class Mutation(graphene.ObjectType):
    create_project = createProject.Field()