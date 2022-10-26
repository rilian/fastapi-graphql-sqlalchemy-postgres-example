import time
import logging
from models.task import Task
from utils import NotAuthorizedException, NotAuthenticatedException
from services.platform.get_current_user import get_current_user
from services.platform.authorization.task import can_create_task

logger = logging.getLogger()

async def resolve_auth_create_task(_, info, params):
    start_time = time.monotonic()
    body = await info.context['request'].body()
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_auth_create_task: request body = {body}")
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_auth_create_task: params = {params}")

    current_user = get_current_user(info.context['request'], info.context['db'])
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_auth_create_task: current_user = {current_user}")
    if not current_user:
        raise NotAuthenticatedException

    auth = can_create_task(current_user)
    if not auth['authorized']:
        raise NotAuthorizedException(auth['message'])

    task = Task(
        user_id = current_user.id,
    )

    if 'description' in params:
        task.description = params['description']

    info.context['db'].add(task)
    info.context['db'].commit()
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_auth_create_task: task = {task}")

    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_auth_create_task: done")

    return task
