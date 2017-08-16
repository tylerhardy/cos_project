#! bash
sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl daemon-reload