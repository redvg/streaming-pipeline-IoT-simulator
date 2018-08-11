#!/usr/bin/env python

import apache_beam as beam
import argparse

BUCKET_ID = 'udemy-data-engineer-210920'
BUCKET_FOLDER = 'iot-stream'


def resolve_average_speed(record):

    (freeway, speed) = record

    return (freeway, sum(speed) / len(speed))

def run():

    parser = argparse.ArgumentParser()

    parser.add_argument('--pubsub',
                        required=True,
                        help='PubSub topic')
    parser.add_argument('--bq',
                        required=True,
                        help='BigQuery table')
    parser.add_argument('--project',
                        required=True,
                        help='Project ID')

    args = parser.parse_args()

    argv = [
      '--project={0}'.format(args.project),
      '--job_name=IoTStream',
      '--save_main_session',
      '--staging_location=gs://{0}/{1}/staging/'.format(BUCKET_ID, BUCKET_FOLDER),
      '--temp_location=gs://{0}/{1}/staging/'.format(BUCKET_ID, BUCKET_FOLDER),
      '--runner=DataflowRunner']

    with pipeline = beam.Pipeline(argv=argv):

        stream = pipeline | beam.io.ReadFromPubSub(args.pubsub)

        transformed = (stream
            |  'SpeedOnLane' >> beam.Map(lambda x: (x[3], x[6]))
            |   beam.WindowInto(beam.transforms.window.FixedWindows(10, 0))
            |   'Group' >> beam.GroupByKey()
            |   'Average' >> beam.Map(resolve_average_speed)
        )

        transformed | 'SinkToBQ' >> beam.io.WriteToBigQuery(args.bq)

if __name__ == '__main__':

    run()
