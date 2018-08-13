#!/usr/bin/env python

import apache_beam as beam
import argparse

BUCKET_ID = 'udemy-data-engineer-210920'
BUCKET_FOLDER = 'iot-stream'

import logging

class SpeedOnFreewayFn(beam.DoFn):

    def process(self, el):

        logging.info(el)

        freeway_and_speed = (x[3], float(x[6]))

        logging.info(freeway_and_speed)

        yield freeway_and_speed

def resolve_average_speed(el):

    (freeway, speed) = el

    return (freeway, sum(speed)) #/len(speed)

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
      '--job_name=iotstream',
      '--save_main_session',
      '--staging_location=gs://{0}/{1}/staging/'.format(BUCKET_ID, BUCKET_FOLDER),
      '--temp_location=gs://{0}/{1}/staging/'.format(BUCKET_ID, BUCKET_FOLDER),
      '--runner=DataflowRunner',
      '--streaming']

    with beam.Pipeline(argv=argv) as pipeline:

        pubsub_topic_path = 'projects/{0}/topics/{1}'.format(args.project,
                                                             args.pubsub)

        stream = pipeline | beam.io.ReadFromPubSub(pubsub_topic_path)

        speeds = stream | 'SpeedOnFreeway' >> beam.ParDo(SpeedOnFreewayFn())
        #speeds = stream | 'SpeedOnHighway' >> beam.Map(lambda x: (x[3], float(x[6])))

        window = speeds | beam.WindowInto(beam.transforms.window.FixedWindows(1, 0))

        formatted = (window
            | 'Group' >> beam.GroupByKey()
            | 'Average' >> beam.Map(resolve_average_speed)
            | 'FormatForBQ' >> beam.Map(lambda x: {'freeway': str(x[0]), 'speed': x[1]})
        )

        formatted | 'SinkToBQ' >> beam.io.WriteToBigQuery(args.bq,
                schema='freeway:STRING, speed:FLOAT',
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)

if __name__ == '__main__':

    run()
