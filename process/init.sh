#!/bin/bash

bq mk iot
bq mk -t iot.sensors freeway:STRING,speed:FLOAT

sudo pip install --upgrade google-cloud-dataflow
