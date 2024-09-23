import requests

def lambda_handler(event, context):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()  # Retorna los datos como un JSON
