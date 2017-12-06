#!/usr/bin/python
#Server Monitoring script to alert in slack by by DevOpsRob
#Download the slacker python module by running wget https://pypi.python.org/packages/42/f9/3f3bcbe13b8c3aa4a134136cbbaa94beb1c5781f5a33b9317b45c699d453/slacker-0.9.60.tar.gz
#Untar the file by running tar -xzvf slacker-0.9.60.tar.gz
#Install the psutil module by yum install python-psutil -y
#Enter the alert thresholds you would like to set in the variables section
#For each alert, enter the slack channel name that you would like to notify in place of <slack-channel-name>
#Install a crontab for this script to run at whatever poll interval you require for your monitoring

#Import python libraries
import psutil
import os
from slacker import Slacker

#Variables
cpu_threshold=<insert cpu usage %>
mem_threshold=<insert memory usage %>
disk_threshold=<insert disk space usage %>
slack = Slacker('insert your slack api token in here')

#CPU Alerting
if psutil.cpu_percent() > cpu_threshold:
    slack.chat.post_message('#<slack-channel-name>', 'CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
else:
    print ('cpu is below %s percent' % cpu_threshold)

#Memory Alerting
if psutil.virtual_memory().percent > mem_threshold:
    slack.chat.post_message('#<slack-channel-name>', 'MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
else:
    print('Memory usage is below %s percent' % mem_threshold)

#Disk Usuage Alerting
if psutil.disk_usage('/').percent > disk_threshold:
    slack.chat.post_message('#<slack-channel-name>', 'DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
else:
    print('disk space usage is below %s percent' % disk_threshold)

#Network Packet loss alerting
if psutil.net_io_counters().dropout > 0:
    slack.chat.post_message('#<slack-channel-name>', 'PACKET LOSS ALERT - The system is currently experiencing packet loss')
else:
    Print('No packets have been lost')