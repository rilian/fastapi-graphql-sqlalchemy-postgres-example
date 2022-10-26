from models.task import Task
from utils import NotFoundException
import logging

logger = logging.getLogger()

async def resolve_get_task(_, info, uuid):
    body = await info.context['request'].body()
    logger.warn(f"\nresolve_get_task: request body = {body}")
    logger.warn(f"\nresolve_get_task: uuid = {uuid}")

    task = info.context['db'].query(Task).filter(Task.id==id).first()
    if not task:
        raise NotFoundException

    return task
