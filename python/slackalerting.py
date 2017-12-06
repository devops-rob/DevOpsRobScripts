#!/usr/bin/python
'''
Server Monitoring script to alert in slack by by DevOpsRob
Download the slacker python module by running wget https://pypi.python.org/packages/42/f9/3f3bcbe13b8c3aa4a134136cbbaa94beb1c5781f5a33b9317b45c699d453/slacker-0.9.60.tar.gz
Untar the file by running tar -xzvf slacker-0.9.60.tar.gz
Install the psutil module by yum install python-psutil -y
Enter the alert thresholds you would like to set in the variables section
For each alert, enter the slack channel name that you would like to notify in place of <slack-channel-name>
Install a crontab for this script to run at whatever poll interval you require for your monitoring eg * * * * * /usr/bin/python /root/monitoring/slack_alerting.py >> /var/log/monitoring.log
I highly recommend installing and configuring logrotate on this file
The below is an example configuration for logrotate
/var/log/monitoring.log {
    create 0644 root root
    daily
    rotate 10
    missingok
    notifempty
    compress
    sharedscripts
    postrotate
        /bin/kill -USR1 `cat /run/nginx.pid 2>/dev/null` 2>/dev/null || true
    endscript
}
'''

#Import python libraries
import psutil
import os
from slacker import Slacker
import datetime
import time

#Variables
cpu_threshold=<insert-cpu-threshold-%>
mem_threshold=<insert-memory-threshold-%>
disk_threshold=<insert-diskspace-threshold-%>
slack = Slacker('<insert-your-slack-api-token-here>')

#CPU Alerting
if psutil.cpu_percent() > cpu_threshold:
    slack.chat.post_message('#<insert-slack-channel-name-here>', 'CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
    print (time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
else:
    print (time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)

#Memory Alerting
if psutil.virtual_memory().percent > mem_threshold:
    slack.chat.post_message('#<insert-slack-channel-name-here>', 'MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
    print(time.strftime("%c") + ' - MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
else:
    print(time.strftime("%c") + ' - Memory usage is below %s percent' % mem_threshold)

#Disk Usuage Alerting
if psutil.disk_usage('/').percent > disk_threshold:
    slack.chat.post_message('#<insert-slack-channel-name-here>', 'DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
    print(time.strftime("%c") + ' - DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
else:
    print(time.strftime("%c") + ' - disk space usage is below %s percent' % disk_threshold)

#Network Packet loss alerting
if psutil.net_io_counters().dropout > 0:
    slack.chat.post_message('#<insert-slack-channel-name-here>', 'PACKET LOSS ALERT - The system is currently experiencing packet loss')
    print(time.strftime("%c") + ' - PACKET LOSS ALERT - The system is currently experiencing packet loss')
else:
    print(time.strftime("%c") + ' - No packets have been lost')