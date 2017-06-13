#!/bin/bash
#installer script to install packages using yum for MySQL server

repo=http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
apps=(
      	'epel-release'
        'nano'
	    'net-tools'
        'wget'
	    'vim'
	    'phpmyadmin'
        

    )
#the below separates the list entry above to allo for loop to work
app=$( IFS=$'\n'; echo "${apps[*]}" )

for a in $app
do
    yum install $app -y

done

#install repository for mysql-server
wget $repo
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm

#update system with new repo
yum update
#install MySQL Server
yum install mysql-server

#start SQL daemon
sudo systemctl start mysqld
#harden SQL
sudo mysql_secure_installation -y

