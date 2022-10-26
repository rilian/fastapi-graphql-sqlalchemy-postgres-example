from ariadne import MutationType, QueryType

from .mutation.auth_create_task import resolve_auth_create_task
from .mutation.create_task import resolve_create_task

from .query.get_task import resolve_get_task

mutation = MutationType()
mutation.field("auth_create_task")(resolve_auth_create_task)
mutation.field("create_task")(resolve_create_task)

query = QueryType()
query.field("get_task")(resolve_get_task)
