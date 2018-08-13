#!/bin/bash

bq mk iot
bq mk -t iot.sensors freeway:STRING,speed:FLOAT,window_start:TIMESTAMP,window_end:TIMESTAMP

sudo pip install --upgrade google-cloud-dataflow
