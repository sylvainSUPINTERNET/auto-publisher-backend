import os
import pika
import logging

from infrastructure.rabbitmq_queues import queues_to_create

class RabbitMqClient(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logging.info("Creating RabbitMqClient instance")
            cls._instance = super().__new__(cls)
            logging.info(f"Connecting to RabbitMQ at {os.getenv('RABBIT_MQ_URL', '')}")
            cls._instance.connection = pika.BlockingConnection(pika.URLParameters(os.getenv('RABBIT_MQ_URL', '')))

            chann = cls._instance.connection.channel()
            for queue in queues_to_create:
                chann.queue_declare(queue=queue, durable=True)
                logging.info(f"  Queue {queue} declared (durable=True)")
            chann.close()
        else:
            logging.info("RabbitMqClient instance already created, reuse connection")

        return cls._instance

    def get_conn(self)->pika.BlockingConnection:
        return self.connection
    
    def close_conn(self):
        if self.connection is not None :
            logging.info("Closing rabbitmq connection")
            self.connection.close()

