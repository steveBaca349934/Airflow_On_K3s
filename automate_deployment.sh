#!/bin/bash
docker rmi $(docker images --filter=reference="1.0.0" -q)