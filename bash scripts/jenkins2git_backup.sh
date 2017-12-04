#!/bin/bash
#Jenkins backup script by DevOpsRob
#This script requires a git repo called jenkins_backup to be created
#You will need to add your ssh public key to the deploy keys of this newly created repo and allow read/write permissions
#Clone the repo into /var/lib/ folder
#Save this script to the /root/ folder
#Setup a crontab to run this script as per your requirement

#install git command line tools
yum install git -y

#Variables
backupdate=$(date +"%m-%d-%y")

#Copy Jenkins configuration files to the git repo clone folder
cp -frv /var/lib/jenkins/ /var/lib/jenkins_backup

#Add the config files to the index
cd /var/lib/jenkins_backup
git add /var/lib/jenkins_backup/jenkins/

#Commit the back up
git commit -m "backup-$backupdate"

#Push the backup to git
git push -u origin master

#Delete the local backup files
rm -rfv /var/lib/jenkins_backup/jenkins
