python3 -m venv env
git pull
source env/bin/activate
cd backend
pip install -r requirements.txt
cd ..
sudo cp setup/demo1_screen_gunicorn.conf /etc/supervisor/conf.d/betaful_screen_gunicorn.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart betaful_screen_gunicorn

cd frontend
npm install
npm run build
sudo cp setup/screen_demo1_nginx_django.conf /etc/nginx/conf.d/betaful_screen_nginx_django.conf
sudo cp setup/screen_demo1_nginx_svelte.conf /etc/nginx/conf.d/betaful_screen_nginx_svelte.conf
sudo service nginx restart
