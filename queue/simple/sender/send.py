#!/usr/bin/env python
import pika
import pika.exceptions
import socket
from time import sleep
import random

import logging

logger = logging.getLogger("sender")
logger.setLevel(logging.INFO)

credentials = pika.PlainCredentials('myuser', 'mypass')
con_params = pika.ConnectionParameters('rabbitmq', 5672,   credentials=credentials)

def on_open(connection):
    channel = None
    def spam():
        if connection.is_closed:
            return
        x = random.randint(0, 10)
        channel.basic_publish(exchange='',
                        routing_key='numbers',
                        mandatory=True,
                        body=str(x))
        logger.warning("send " + str(x))
        connection.add_timeout(random.random() * 4, spam)
    
    def on_channel_open(new_channel):
        nonlocal channel
        def pub(method):
            connection.add_timeout(0, spam)
        channel = new_channel
        channel.queue_declare(pub, queue='numbers')
        
    connection.channel(on_channel_open)

sleep(5)
logger.warning("Hi!")

connection = pika.SelectConnection(parameters=con_params, on_open_callback=on_open)

try:
    connection.ioloop.start()
except KeyboardInterrupt:
    
    connection.close()
    connection.ioloop.start()
