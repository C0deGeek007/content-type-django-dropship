import graphene

class ProjectInput(graphene.InputObjectType):
    description = graphene.String()
    creator_id = graphene.ID()
    comment = graphene.String()

class CommentInput(graphene.InputObjectType):
    body = graphene.String()
    projectId = graphene.ID()