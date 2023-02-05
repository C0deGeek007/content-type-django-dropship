import graphene

class Query(graphene.ObjectType):
    allProject = graphene.String()
    def resolve_allProject(root,info):
        print("inside all project query")
        return "all projects"