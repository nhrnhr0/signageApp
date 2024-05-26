git pull
source env/bin/activate
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
sudo supervisorctl restart demo1_screen_gunicorn

cd ..
cd frontend
npm install
npm run build
sudo service nginx restart

echo '====================='
echo 'done'
echo '====================='

