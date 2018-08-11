#!/bin/bash

echo 'launching pubsub publisheer'

python sensors.py --speedFactor=60 --project=$DEVSHELL_PROJECT_ID

echo '+'
