#!/bin/bash

bq mk iot
bq mk -t iot.sensors lane:STRING,avgspeed:FLOAT

sudo pip install --upgrade google-cloud-dataflow
