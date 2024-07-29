import json
import boto3

def lambda_handler(event, context):
    year = int(event['queryStringParameters']['year'])
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('year').eq(year)
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
