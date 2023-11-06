## tl;dr

Start an OpenFGA server, simulate some traffic, check the metrics and traces.

## Pre-requisites

- Docker: https://docs.docker.com/engine/install/
- FGA CLI: https://github.com/openfga/cli#installation

## Demo

1. Start OpenFGA with tracing and metrics enabled:
    `docker-compose up --detach`
1. Create a store: 
    `export FGA_STORE_ID=$(fga store create --model model.fga | jq -r .store.id)`
1. Write the authorization model: 
    `fga model write --file model.fga`
1. Write tuples: 
    `fga tuple write --file tuples.yaml`
1. Make Check calls:
    `fga model test --tests demo.fga.yaml`
1. See metrics in Prometheus: http://localhost:9090/. E.g. `go_sql_open_connections`
1. See metrics in Grafana: http://localhost:3001/
1. See traces in Jaeger: http://localhost:16686/search

## Cleanup

1. Stop OpenFGA and remove data: `docker-compose down --volumes`

## Resources

- Learn more about OpenFGA: https://openfga.dev / https://openfga.dev/blog.

- Engage with the OpenFGA community in [Discord](https://discord.gg/8naAwJfWN6) or [Github](https://github.com/openfga/community/tree/main).

- Follow us on Twitter: [@openfga](https://twitter.com/openfga)

And please, don't forget to [star our Github Repository](https://github.com/openfga/openfga)!




