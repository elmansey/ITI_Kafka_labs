#!/bin/bash 
# update and install java 
sudo apt-get update -y 
sudo apt-get install openjdk-8-jdk -y 

#install kafka 
wget https://dlcdn.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz

tar -xzf kafka_2.13-3.4.0.tgz
cd kafka_2.13-3.4.0

# https://kafka.apache.org/quickstart

# /kafka_2.13-3.4.0/config/server.properties
# /kafka_2.13-3.4.0/config/zookeeper.properties
# to start zookeeper
# /kafka_2.13-3.4.0/bin/zookeeper-server-start.sh
# to stop zookeeper
# /kafka_2.13-3.4.0/bin/zookeeper-server-stop.sh
# test zookeeper 
# /kafka_2.13-3.4.0/bin/zookeeper-shell.sh

# start kafka 
# /kafka_2.13-3.4.0/bin/kafka-server-start.sh
# stop kafka 
# /kafka_2.13-3.4.0/bin/kafka-server-stop.sh 

# kafka create topic 
# /kafka_2.13-3.4.0/bin/kafka-topics.sh


# to send messages 
# /kafka_2.13-3.4.0/bin/kafka-console-producer.sh
# to receive messages 
# /kafka_2.13-3.4.0/bin/kafka-console-consumer.sh

# start zookeeper 
cd /kafka_2.13-3.4.0/bin/
./zookeeper-server-start.sh -daemon  ../config/zookeeper.properties

# test 
./zookeeper-shell.sh localhost:2181
create /iti

# start kafka 
./kafka-server-start.sh -daemon  ../config/server.properties

# create topic 
./kafka-topics.sh --create --topic iti --bootstrap-server  localhost:9092

# create producer 
./kafka-console-producer.sh --topic iti --bootstrap-server  localhost:9092

./kafka-console-consumer.sh --topic iti  --from-beginning --bootstrap-server  localhost:9092


# stop kafka 
./kafka-server-stop.sh  -daemon  ../config/server.properties

# stop zookeeper
./zookeeper-server-stop.sh  -daemon  ../config/zookeeper.properties




# cluster 
mkdir -p /data/zookeeper
chown ubuntu:ubuntu  -r /data/zookeeper

# EDIT IN ZOOKEEPER.PROPERTIRES 
# datadir=/data/zookeeper
# add servers 
# server.1= ip:2888:3888
# server.2= ip:2888:3888
# server.3= ip:2888:3888
# tickTime=2000
# initLimit=10
# syncLimit=5
echo "1" > /data/zookeeper/myid


# kafka 
mkdir -p /data/kafka
chown ubuntu:ubuntu  -r /data/kafka
# zookeeper.connect=ip,ip/kafka
# zookeeper.connection.timeout.ms=18000