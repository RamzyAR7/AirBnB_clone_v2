#!/usr/bin/env bash

if ! command -v nginx &> /dec/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/{releases/test,shared}

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '26i\	location /hbnb_static {\n\t alias /data/web_static/current/;\n} ' /etc/nginx/sites-available/default
sudo service nginx restart

exit 0
