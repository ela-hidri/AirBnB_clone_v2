#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo bash -c "echo \"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>\" > /data/web_static/releases/test/index.html"

rm -f /data/web_static/current
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "\t location /hbnb_static/ {\n\talias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart
