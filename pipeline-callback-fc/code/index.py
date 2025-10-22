import json

def handler(event, context):
    print("Received event:", event)
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'message': 'Hello from Simple Python Function!',
            'success': True
        })
    }
