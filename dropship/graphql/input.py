import graphene

class ProjectInput(graphene.InputObjectType):
    description = graphene.String()
    creator_id = graphene.ID()