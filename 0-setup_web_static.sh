#!usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

#Install Nginx if it not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get  -y update
    sudo apt-get install nginx -y
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

cat <<EOF > /data/web_static/releases/test/index.html








sudo service nginx start


