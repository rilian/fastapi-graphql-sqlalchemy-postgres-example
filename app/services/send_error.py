import os
import json
import pydash
import logging

logger = logging.getLogger()
HANDLED_EXCEPTIONS = [
    'UnprocessableEntityException',
    'NotFoundException',
    'NotAuthenticatedException',
    'NotAuthorizedException'
]

def send_error(error, raw_error):
    error_class = raw_error.original_error.__class__.__name__
    logger.warn(f"\nsend_error: original error class = {error_class}")
    logger.warn(f"\nsend_error: ERROR: {json.dumps(error)}\n")

    # Skip handled errors
    if error_class in HANDLED_EXCEPTIONS:
        logger.warn(f"\nsend_error: skip sending handled exception")
        return True

    stack_trace = pydash.get(error, 'extensions.exception.stacktrace')
    stack_trace_formatted = json.dumps(stack_trace, indent=2)

    error_context = pydash.get(error, 'extensions.exception.context')

    # Hide sensitive information from exception emails or logs
    for key in ['headers']:
        if key in error_context:
            error_context[key] = '*******'

    error_context_formatted = json.dumps(error_context, indent=2)

    # TODO: send exception
    message=(f"""
        Error message: {error['message']}
        \n\nError path: {error['path']}
        \n\nError trace: {stack_trace_formatted}
        \n\nError context: {error_context_formatted}
    """).strip(),
