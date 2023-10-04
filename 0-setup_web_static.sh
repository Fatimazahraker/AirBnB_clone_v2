#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

#Install Nginx if it not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get  -y update
	sudo apt-get install nginx -y
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

cat <<EOF > /data/web_static/releases/test/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>Welcome to test page</h1>
    <p>Hello, world! You are here now</p>
</body>
</html>
EOF

#Create a symbolic link 
if [ -L /data/web_static/current ]; then
	rm -f /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart


