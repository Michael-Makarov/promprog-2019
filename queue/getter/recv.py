#!/usr/bin/env python
import pika
from time import sleep

import logging

logger = logging.getLogger("getter")
logger.setLevel(logging.INFO)

credentials = pika.PlainCredentials('myuser', 'mypass')
con_params = pika.ConnectionParameters('rabbitmq', 5672,   credentials=credentials)

def on_open(connection):
    connection.channel(on_channel_open)

sleep(5)
logger.warning("Hi!")

connection = pika.SelectConnection(parameters=con_params, on_open_callback=on_open)

def on_channel_open(channel):
    def pub(method):
        channel.basic_consume(callback,
                      queue='numbers',
                      no_ack=True)
        
    channel.queue_declare(pub, queue='numbers')

def callback(ch, method, properties, body):
    logger.warning(" [x] Received %r" % body)    

logger.warning(' [*] Waiting for messages. To exit press CTRL+C')

try:
    connection.ioloop.start()

except KeyboardInterrupt:
    
    connection.close()
    connection.ioloop.start()
