import os
import pika

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


# import pika


# def on_open(connection):
#     # Invoked when the connection is open
#     print("connected")
#     pass

# def on_close(connection, exception):
#     # Invoked when the connection is closed
#     connection.ioloop.stop()

# credentials = pika.PlainCredentials('vdhqcsmo', 'ppC1XSCXfktAVzoPu88FpMQGdznQVj5t')
# connection = pika.SelectConnection(parameters=pika.ConnectionParameters(host='rat-01.rmq2.cloudamqp.com', port=5671, credentials=credentials), on_open_callback=on_open, on_close_callback=on_close)


# try:
#     connection.ioloop.start()
# except KeyboardInterrupt:
#     connection.close()

