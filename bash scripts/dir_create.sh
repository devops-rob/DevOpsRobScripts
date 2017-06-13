#!/bin/bash
#script to create folders for letsencrypt ssl certs

directories=" web_logs ssl_certs csr account_key "

cd /africamunity

for directory in directories
do
    if
        [[$directories=$false]]
    
    then
        echo "$directories has already been created"
    else
        mkdir $directories
        chmod 744 $directories
    fi
done