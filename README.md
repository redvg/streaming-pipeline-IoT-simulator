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
sensors publish speeds of cars in a particular lane

### sensors.py
`publish()` publishes messages
see commit a8b30485f6ec4f834efd30a1b69155daf530d74d for obsolete batch msging \
note `TOPIC` const \
`simulate()` simulates sensors data \
-`compute_sleep_secs()` determines how long to wait based on  `speedFactor`
-when time passes `publish()` is called

### init.sh
fetches sensors data
