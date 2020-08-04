import graphene

from gql_exa.schema import Query as MyQuery
from gql_exa.schema import Mutation as MyMutation


class Query(MyQuery, graphene.ObjectType):
    pass


class Mutation(MyMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)