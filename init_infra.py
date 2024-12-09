
# run by Github Actions to initialize the infrastructure

import os
import pika
from dotenv import load_dotenv

load_dotenv()

connection = pika.BlockingConnection(pika.URLParameters(f"{os.getenv('RABBIT_MQ_URL', '')}"))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')



try:
    channel.basic_consume(queue='hello', on_message_callback=lambda ch, method, properties, body: print(body.decode()), auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()
except KeyboardInterrupt:
    connection.close()


