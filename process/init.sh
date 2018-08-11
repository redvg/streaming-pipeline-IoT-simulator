#!/bin/bash

bq mk iot
bq mk -t iot.foo lane:STRING,avgspeed:FLOAT
