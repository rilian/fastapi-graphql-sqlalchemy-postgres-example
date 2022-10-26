import os
import logging
from json.decoder import JSONDecodeError
from mangum import Mangum
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from ariadne import graphql, make_executable_schema, gql, load_schema_from_path, format_error
from ariadne.constants import PLAYGROUND_HTML
from graphql import GraphQLError
from database import SessionLocal
from resolvers.index import mutation, query
from services.send_error import send_error

logger = logging.getLogger()
type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: check if this is helpful https://spectrum.chat/ariadne/general/error-handling-questions~ca23d96d-9c02-45b3-8028-761396b933ed
def custom_error_formatter(error: GraphQLError, debug: bool = False) -> dict:
    logger.warn(f"\ncustom_error_formatter: debug={debug}")
    logger.warn(f"\ncustom_error_formatter: error={error}")

    error_with_context = format_error(error, True)
    send_error(error_with_context, error)

    if debug:
        # If debug is enabled, reuse Ariadne's formatting logic
        return error_with_context

    # Create formatted error data
    formatted_error = error.formatted

    # Replace original error message with custom one
    # formatted_error["message"] = "Internal Server Error. Engineering team has been notified. Please try again later or contact Support"

    return formatted_error

@app.get("/", response_class=HTMLResponse)
async def graphql_playground():
    return PLAYGROUND_HTML

@app.post("/auth")
@app.post("/")
async def graphql_server(request: Request, response: Response):
    # logger.warn(f"\ngraphql_server: request = {request.__dict__}")

    try:
        data = await request.json()
    except JSONDecodeError:
        return { "message": "Received data is not a valid JSON" }

    logger.warn(f"\ngraphql_server: data={data}")

    success, result = await graphql(
        schema,
        data,
        # NOTE: any exception raised in "request" wont be caught by Ariadne, and should be processed separately
        context_value={
            'request': request,
            'db': SessionLocal(),
        },
        error_formatter=custom_error_formatter,
        debug=(os.getenv("STAGE") != "prod")
    )

    if not success:
        response.status_code = 400

    # logger.warn(f"\ngraphql_server: result={result}")
    return result

handler = Mangum(app, enable_lifespan=False)
