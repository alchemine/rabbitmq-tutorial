#!/bin/bash
# https://www.rabbitmq.com/docs/download

docker run -it --name rabbitmq --restart always -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management