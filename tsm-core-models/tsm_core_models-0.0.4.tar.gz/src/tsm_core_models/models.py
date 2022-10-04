from py2neo.ogm import GraphObject, Property, Related, RelatedTo

class Neo4jUser(GraphObject):
    __primarykey__ = 'username'
    username = Property()

    befriended = RelatedTo('Neo4jUser', 'BEFRIENDED')
    blocked = RelatedTo('Neo4jUser', 'BLOCKED')

