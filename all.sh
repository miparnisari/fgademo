#!/bin/bash
set -o pipefail
docker-compose up --detach
FGA_STORE_ID=$(fga store create --model model.fga | jq -r .store.id)
export FGA_STORE_ID
fga model write --file model.fga
fga tuple write --file tuples.yaml
fga model test --tests demo.fga.yaml