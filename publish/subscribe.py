from google.cloud import pubsub_v1
import argparse

def callback(message):

  print('Received message: {}'.format(message))

  message.ack()

if __name__ == '__main__':

   parser = argparse.ArgumentParser(description='Creates subscrition')
   parser.add_argument('--project',
                       help='Example: --project $DEVSHELL_PROJECT_ID',
                       required=True)
   parser.add_argument('--topic',
                       help='topic name',
                       required=True)
   parser.add_argument('--name',
                       help='subscription name',
                       required=True)

   args = parser.parse_args()

   subscriber = pubsub_v1.SubscriberClient()

   topic_path = subscriber.topic_path(args.project, args.topic)

   subscription_path = subscriber.subscription_path(args.project, args.name)

   subscription = subscriber.create_subscription(subscription_path,
                                                 topic_path)

   print('Subscription created: {}'.format(subscription))

   subscriber.subscribe(subscription_path, callback=callback)

   print('Listening for messages on {}'.format(subscription_path))

# just go to https://console.cloud.google.com/cloudpubsub/subscriptions/cpsubs
# and publish some messages. You will see the payload inmediately on cloudshell
#
# note even if we are pulling behind the scenes, the client libraries are designed so from the developer's point of view
# it works like a push. You just register a callback and forget. No need to keep looping and pulling and sleeping
