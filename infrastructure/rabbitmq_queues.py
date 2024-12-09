from enum import Enum


"""
Queue names for RabbitMQ (created at the start of the application)
"""
class RabbitMQQueueEnum(Enum):
    YT_DL_QUEUE = "yt_dl_queue"
     # TODO => add more queues here

queues_to_create: list[str] = [RabbitMQQueueEnum.YT_DL_QUEUE.value]