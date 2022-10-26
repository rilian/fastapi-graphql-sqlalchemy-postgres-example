import logging

logger = logging.getLogger()

def can_create_task(current_user):
    logger.warn(f"\can_create_task: current_user = {current_user}")

    if current_user.id == 1:
        return {
          'authorized': True,
        }

    return {
      'authorized': False,
      'message': 'Only user with id=1 can create tasks',
    }
