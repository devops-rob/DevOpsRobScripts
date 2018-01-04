#!/usr/bin/python
'''
Server Monitoring script to alert in slack by by DevOpsRob
Download the slacker python module by running wget https://pypi.python.org/packages/42/f9/3f3bcbe13b8c3aa4a134136cbbaa94beb1c5781f5a33b9317b45c699d453/slacker-0.9.60.tar.gz
Untar the file by running tar -xzvf slacker-0.9.60.tar.gz
run pip install slacker
Install the psutil module by yum install python-psutil -y
Enter the alert thresholds you would like to set in the variables section
For each alert, enter the slack channel name that you would like to notify in place of <slack-channel-name>
Install a crontab for this script to run at whatever poll interval you require for your monitoring. e.g. * * * * * /usr/bin/python /root/monitoring/slack_alerting.py
This script will also create a log file (/var/log/monitor.log) if it doesn't already exist and write the output of the server checks to it.
I highly recommend installing and configuring logrotate on this file
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
logfile='/var/log/monitor.log'

#CPU Alerting
def cpu():
    if psutil.cpu_percent() > cpu_threshold:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
        print (time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
    else:
        print (time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)
    return

#Memory Alerting
def memory():
    if psutil.virtual_memory().percent > mem_threshold:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
        print(time.strftime("%c") + ' - MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
    else:
        print(time.strftime("%c") + ' - Memory usage is below %s percent' % mem_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - Memory usage is below %s percent' % mem_threshold)
    
    return

#Disk Usuage Alerting
def disk():
    if psutil.disk_usage('/').percent > disk_threshold:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
        print(time.strftime("%c") + ' - DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
    
    else:
        print(time.strftime("%c") + ' - disk space usage is below %s percent' % disk_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - disk space usage is below %s percent' % disk_threshold)

    return

#Network Packet loss alerting
def netmon():
    if psutil.net_io_counters().dropout > 0:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'PACKET LOSS ALERT - The system is currently experiencing packet loss')
        print(time.strftime("%c") + ' - PACKET LOSS ALERT - The system is currently experiencing packet loss')
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - PACKET LOSS ALERT - The system is currently experiencing packet loss')
    else:
        print(time.strftime("%c") + ' - No packets have been lost')
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - No packets have been lost')

    return

cpu()
memory()
disk()
netmon()