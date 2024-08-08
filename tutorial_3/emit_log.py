import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

# result = channel.queue_declare(queue='', exclusive=True)
# channel.queue_bind(exchange="logs", queue=result.method.queue)

message = " ".join(sys.argv[1:]) or "Hello world!"
channel.basic_publish(exchange="logs", routing_key="", body=message)
print(f" [x] Sent {message}")
connection.close()
