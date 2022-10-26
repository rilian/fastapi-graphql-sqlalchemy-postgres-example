import logging
from models.user import User
from utils import NotFoundException

logger = logging.getLogger()

def get_current_user(request, db_session):
    logger.warn(f"\nget_current_user: request = {request}")
    logger.warn(f"\nget_current_user: request scope = {request.scope}")

    # This is example specific to Cognito:
    if ('aws.event' in request.scope
        and 'requestContext' in request.scope['aws.event']
        and 'authorizer' in request.scope['aws.event']['requestContext']
        and 'claims' in request.scope['aws.event']['requestContext']['authorizer']
        and 'email' in request.scope['aws.event']['requestContext']['authorizer']['claims']
    ):
        email = request.scope['aws.event']['requestContext']['authorizer']['claims']['email']
        user = db_session.query(User).filter(User.email==email).first()

        if not user:
            raise NotFoundException('User not found by email')
        logger.warn(f"\nget_current_user: user = {user}")
        return user

    logger.warn(f"\nget_current_user: request does not contain authentication info")
    return None
