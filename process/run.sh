#!/bin/bash

python pipeline.py --project=$DEVSHELL_PROJECT_ID --bq=iot.sensors --pubsub=sensors
