ETL Pipeline on GCP. PubSub publisher which simualates IoT sensors streaming data. PubSub subscriber as an ingress. DataFlow as data transform. BigQuery as a sink.

![Screenshot](1.png)

as per https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/streaming \
and per https://www.udemy.com/gcp-data-engineer-and-cloud-architect/learn/v4/t/lecture/7598768?start=0 \
and per https://www.udemy.com/gcp-data-engineer-and-cloud-architect/learn/v4/t/lecture/7598772?start=0 \
and per https://www.udemy.com/gcp-data-engineer-and-cloud-architect/learn/v4/t/lecture/7598774?start=0 \

## prereqs
`gcloud pubsub topics create sensors` though py handles too \
`pip install google-cloud-pubsub`

## publish
holds sensors simulator publisher \
data is from sensors along San Diego highway \
sensors publish speeds of cars in a particular lane \
run: `python sensors.py --speedFactor=60 --project=$DEVSHELL_PROJECT_ID` \
`speedFactor` 60 sends roughly 477 events every 5 seconds \
nb: deeper dive at  https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/pubsub/cloud-client/subscriber.py \
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/pubsub/cloud-client/publisher.py \

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
