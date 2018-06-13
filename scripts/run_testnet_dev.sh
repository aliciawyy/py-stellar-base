#!/usr/bin/env bash

CODE_DIR=${HOME}/Codes/py-stellar-base
DOCKER_CODE_DIR=/work/py-stellar-base
STELLAR_DIR=${HOME}/stellar

docker run --rm -it \
    -p "8000:8000" \
    --name stellar \
    -v ${STELLAR_DIR}:/opt/stellar \
    -v ${CODE_DIR}:${DOCKER_CODE_DIR} \
    -e PYTHONPATH=${DOCKER_CODE_DIR} \
    pystellar \
    --testnet
