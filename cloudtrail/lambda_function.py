import boto3

print('Loading function')


def lambda_handler(event, context):
    """ Function to define Lambda Handler """
    try:
        client = boto3.client('cloudtrail')
        if event['detail']['eventName'] == 'StopLogging':
            client.start_logging(
                Name=event['detail']['requestParameters']['name'])

    except Exception as e:
        print(e)
