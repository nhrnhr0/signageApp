#python3 -m venv env
git pull
source env/bin/activate
cd backend
pip install -r requirements.txt
cd ..
sudo cp setup/screen_demo1_supervisor.conf /etc/supervisor/conf.d/demo1_screen_gunicorn.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart demo1_screen_gunicorn
