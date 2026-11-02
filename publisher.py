import time
import redis

client = redis.Redis(host='localhost', port=6379, decode_responses=True)

for i in range(10):
    message = f"Hello Redis! Message #{i}"
    client.publish('python_channel', message)
    print(f"відправлено: {message}")
    time.sleep(0.5)