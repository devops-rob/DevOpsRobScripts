#!/bin/bash
#installer script to install packages using yum for Jenkins server

apps=(
      	'epel-release'
        'nano'
	    'net-tools'
        'wget'
	    'vim'
        'java-1.8.0-openjdk.x86_64'
        'nginx'

    )
#the below separates the list entry above to allo for loop to work
app=$( IFS=$'\n'; echo "${apps[*]}" )

for a in $app
do
    yum install $app -y

done

sudo cp /etc/profile /etc/profile_backup
echo 'export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk' | sudo tee -a /etc/profile
echo 'export JRE_HOME=/usr/lib/jvm/jre' | sudo tee -a /etc/profile
source /etc/profile

echo $JAVA_HOME
echo $JRE_HOME


#install repository for Jenkins
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
sudo rpm --import http://pkg.jenkins-ci.org/redhat-stable/jenkins-ci.org.key
yum install jenkins

#update system with new repo
yum update

#Start and enable jenkins service
sudo systemctl start jenkins.service
sudo systemctl enable jenkins.service

#Firewall config
sudo firewall-cmd --zone=public --permanent --add-port=8080/tcp
sudo firewall-cmd --zone=public --permanent --add-port=443/tcp
sudo firewall-cmd --zone=public --permanent --add-service=http
sudo firewall-cmd --zone=public --permanent --add-service=https

sudo firewall-cmd --reload

#SELinux disable
setenforce 0

#edit nginx config files

sed -i 'location / {/a \ proxy_pass http://127.0.0.1:8080;' /etc/nginx/nginx.conf
sed -i 'proxy_pass http://127.0.0.1:8080;/a \ proxy_redirect off;' /etc/nginx/nginx.conf
sed -i 'proxy_redirect off;/a \ proxy_set_header Host $host;' /etc/nginx/nginx.conf
sed -i 'proxy_set_header Host $host;/a \ proxy_set_header X-Real-IP $remote_addr;' /etc/nginx/nginx.conf
sed -i 'proxy_set_header X-Real-IP $remote_addr;/a \ proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;' /etc/nginx/nginx.conf
sed -i 'proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;/a \ proxy_set_header X-Forwarded-Proto $scheme;' /etc/nginx/nginx.conf

#start nginx service
sudo systemctl start nginx.service
sudo systemctl enable nginx.service