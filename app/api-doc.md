# Fastapi Graphql Postgres Example tasks service documentation

## auth_create_task

    mutation {
      auth_create_task(
        params: {
          description: "test"
        }
      ) {
        ... Task fields
      }
    }

    curl -v 'https://xxx/auth' \
    -H 'content-type: application/json' \
    -H 'authorization: Bearer xxx' \
    --data-raw '{"operationName":null,"variables":{},"query":"mutation {\n auth_create_task(params: {data: {}}) {\n created_at\n description\n id\n updated_at\n }\n}\n"}'

## create_task

    mutation {
      create_task(
        params: {
          description: "test"
        }
      ) {
        ... Task fields
      }
    }

    curl 'https://xxx/public' -X POST  --data-raw '{"operationName":null,"variables":{},"query":"mutation {\n  create_task(params: { description: \"test\" }) {\n description\n id\n }\n}\n"}'

## get_task

    query {
      get_task(
        id: 123
      ) {
        ... Task fields
      }
    }

    curl 'https://xxx/public' -X POST  --data-raw '{"operationName":null,"variables":{},"query":"{\n  get_task(id: 123) {\n description\n id\n }\n}\n"}'
