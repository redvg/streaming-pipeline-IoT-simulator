ETL Pipeline on GCP. PubSub publisher which simualates IoT sensors streaming data. PubSub subscriber as an ingress. DataFlow as data transform. BigQuery as a sink.

![Screenshot](1.png)
(created with https://online.visual-paradigm.com)

as per https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/streaming \
and per https://www.udemy.com/gcp-data-engineer-and-cloud-architect/learn/v4/t/lecture/7598768?start=0 \
and per https://www.udemy.com/gcp-data-engineer-and-cloud-architect/learn/v4/t/lecture/7598772?start=0 \
and per https://www.udemy.com/gcp-data-engineer-and-cloud-architect/learn/v4/t/lecture/7598774?start=0 \

## publish
`./init.sh` \
`./run.sh` \
chmod u+x ... \
holds sensors simulator publisher \
data is from sensors along San Diego highway \
sensors publish speeds of cars in a particular lane \
`speedFactor` 60 sends roughly 477 events every 5 seconds \
nb: deeper dive at  https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/pubsub/cloud-client/subscriber.py \
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/pubsub/cloud-client/publisher.py \
\
sensors' data format: \
TIMESTAMP,LATITUDE,LONGITUDE,FREEWAY_ID,FREEWAY_DIR,LANE,SPEED \
2008-11-01 00:00:00,32.749679,-117.155519,163,S,1,71.2

### sensors.py
`publish()` publishes messages \
see commit a8b30485f6ec4f834efd30a1b69155daf530d74d for obsolete batch msging \
note `TOPIC` const \
`simulate()` simulates sensors data \
-`compute_sleep_secs()` determines how long to wait based on  `speedFactor` \
-when time passes `publish()` is called

### init.sh
fetches sensors data

### subscribe.py
an illustration of how the stream could be consumed \
consumes msgs from pull sub \
effectively acts as push sub \
run: `python subscribe.py --project=$DEVSHELL_PROJECT_ID --topic=sensors --name=sensorsSub` \

pub
 ![Screenshot](publish_pub.png)
sub
 ![Screenshot](publish_sub.png)

## process
`./init.sh` \
`./run.sh $DEVSHELL_PROJECT_ID iot.sensors sensors` \
chmod u+x ... \
consumes PubSub topic stream in DataFlow
calculates average speed on each highway \
sinks to BigQuery \

### init.sh
creates BigQuery dataset \
creates BigQuery table \
pips \

### run.sh
runs Apache Beam pipeline on Cloud DataFlow backend \

### pipeline.py


NOTE: py streaming is in beta
see
https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/windowed_wordcount.py \
https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/streaming_wordcount.py \
https://beam.apache.org/documentation/sdks/pydoc/2.6.0/apache_beam.io.gcp.bigquery.html \
https://beam.apache.org/documentation/sdks/python-streaming/ \
https://beam.apache.org/get-started/mobile-gaming-example/#leaderboard-streaming-processing-with-real-time-game-data \
https://cloud.google.com/dataflow/pipelines/specifying-exec-params#streaming-execution \
https://cloud.google.com/blog/products/data-analytics/dataflow-stream-processing-now-supports-python \
https://cloud.google.com/blog/products/data-analytics/review-of-input-streaming-connectors-for-apache-beam-and-apache-spark \
https://cloud.google.com/dataflow/release-notes/release-notes-python \
https://beam.apache.org/blog/2018/06/26/beam-2.5.0.html \












 create bq dataset
 bq mk --iot



 GetMessages
 ExtractData
 TimeWindow
 AvgBySensor
 -groupbykey
 -combine.groupedvalues
 ToBQRow
 BigQueryIO.Write
