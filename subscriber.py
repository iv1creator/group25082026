import redis

client = redis.Redis(host='localhost', port=6379, decode_responses=True)

pubsub = client.pubsub()
pubsub.subscribe('python_channel')

print("очікування повідомлень з каналу 'python_channel'...")

for message in pubsub.listen():
    if message['type'] == 'message':
        print(message['data'])