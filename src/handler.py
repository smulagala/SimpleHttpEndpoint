import json
import datetime
# import requests

# def hello(event, context):
#     body = {
#         "message": "The current date and time is: "+ str(datetime.datetime.now())
#     }

#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }

#     return response

#     # Use this code if you don't use the http event with the LAMBDA-PROXY
#     # integration
#     """
#     return {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "event": event
#     }
#     """

# def hello2(event, context):
#     body = {
#         "message": "The current date and time is from second func: "+ str(datetime.datetime.now())
#     }

#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }

#     return response

#     # Use this code if you don't use the http event with the LAMBDA-PROXY
#     # integration
#     """
#     return {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "event": event
#     }
#     """


def greet_me(event, context):
    # name = event['name']
    body = json.loads(event['body'])
    # data = {"name": name}
    response = {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*",
            # 'Content-Type': 'application/json'
        },
        "body": json.dumps(body)
    }
    
    return response

def get_method(event, context):
    body = json.loads(event['body'])
    query_params = event['queryStringParameters']
    message = {'body': body, 'params': query_params}
    response = make_response(message)
    return response

def post_method(event, context):
    body = json.loads(event['body'])
    response = make_response(body)
    return response

def put_method(event, context):
    body = json.loads(event['body'])
    response = make_response(body)
    return response

def delete_method(event, context):
    body = json.loads(event['body'])
    query_params = event['queryStringParameters']
    message = {'body': body, 'params': query_params}
    response = make_response(message)
    return response

def make_response(message):
    response = {
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(message)
    }
    return response
