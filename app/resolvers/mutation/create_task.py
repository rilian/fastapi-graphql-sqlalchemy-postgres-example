import time
import logging
from models.task import Task

logger = logging.getLogger()

async def resolve_create_task(_, info, params):
    start_time = time.monotonic()
    body = await info.context['request'].body()
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_create_task: request body = {body}")
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_create_task: params = {params}")

    task = Task()

    if 'description' in params:
        task.description = params['description']

    info.context['db'].add(task)
    info.context['db'].commit()
    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_create_task: task = {task}")

    logger.warn(f"\n[{round(time.monotonic() - start_time, 3)}] resolve_create_task: done")

    return task
