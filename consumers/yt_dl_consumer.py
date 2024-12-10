import os
import logging
import time
from dotenv import load_dotenv

from infrastructure.rabbitmq_conn import RabbitMqClient
from infrastructure.rabbitmq_queues import RabbitMQQueueEnum


"""
TODO : flow expected 

 - no auto ack 
 - thread pool 
 - new msg ? start a new thread and download video + ACK
 - error ? nack
 - thread pool is full ? no ack, message stay in queue

"""


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')
load_dotenv()

MAX_RETRIES = 5 
RETRY_DELAY = 5 


def cb(ch, method, properties, body):
    try:
        logging.info(f"Received message from {RabbitMQQueueEnum.YT_DL_QUEUE.value}")
        logging.info(f"Message: {body}")
        logging.info(f"Properties: {properties}")
        logging.info(f"Method: {method}")
    except Exception as e:
        logging.error(f"Error while processing message: {e}")


def yt_dl_consumer():
    channel = RabbitMqClient().get_conn().channel()

    try:
        channel.basic_consume(
            queue=RabbitMQQueueEnum.YT_DL_QUEUE.value,
            on_message_callback=cb,
            auto_ack=True
        )
        logging.info("Starting consumption...")
        channel.start_consuming()
    except Exception as e:
        logging.error(f"Error in consumer loop: {e}")
    finally:
        channel.close()


def start_consumer():
    retries = 0

    while retries < MAX_RETRIES:
        try:
            yt_dl_consumer()
            break 
        except Exception as e:
            retries += 1
            logging.error(f"Error encountered, retrying ({retries}/{MAX_RETRIES}): {e}")
            if retries < MAX_RETRIES:
                logging.info(f"Waiting {RETRY_DELAY} seconds before retrying...")
                time.sleep(RETRY_DELAY)
            else:
                logging.error("Max retries reached. Consumer will not restart.")
                break


if __name__ == "__main__":
    start_consumer()
