#!/usr/bin/env bash
#script that sets up web servers for the deployment
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

FILE="<html>\n\t<head>\n\t\t<body>\n\t\t\tHolberton School\n\t\t</body>\n\t</head>\n</html>"
#sudo touch /data/web_static/releases/test/index.html 2>/dev/null
#sudo sed -i "1i $FILE" /data/web_static/releases/test/index.html
echo -e "$FILE" > /data/web_static/releases/test/index.html

sudo rm /data/web_static/current 2>/dev/null
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/ 2>/dev/null

ALIAS="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "39i $ALIAS" /etc/nginx/sites-available/default
sudo service nginx start
