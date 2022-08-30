#!/bin/bash
# Renew Let's Encript SSL certificate 
# https://metablogue.com/enable-lets-encrypt-ssl-aws-lightsail/

sudo apt update 
sudo apt upgrade -y
sudo certbot renew
sudo /opt/bitnami/ctlscript.sh restart apache