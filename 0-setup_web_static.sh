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

config_block="
    location /hbnb_static {
        alias /data/web_static/current/;
    }
"
sudo sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
