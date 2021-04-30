web: gunicorn djlibgen.wsgi
release: python manage.py migrate
worker: python manage.py rqworker default