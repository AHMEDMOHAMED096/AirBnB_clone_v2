#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment.

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
service nginx start

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data

echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location /hbnb_static {
        alias /data/web_static/current
    }
}" > /etc/nginx/sites-available/default

service nginx restart
sudo nginx -t
service nginx reload
