from boto3 import resource
from os import getenv

dynamodb = resource("dynamodb")
tables = [
    {
        "TableName": "weather_history",
        "KeySchema": [
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
                        {
                'AttributeName': 'created_at',
                'KeyType': 'RANGE'
            }
        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'created_at',
                'AttributeType': 'S'
            }
        ]
    }
    ]

def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                 TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)