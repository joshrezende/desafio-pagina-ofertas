venv: venv/bin/activate
venv/bin/activate: requirements.txt
		test -d venv || virtualenv venv
		venv/bin/pip install -Ur requirements.txt
		touch venv/bin/activate

run:
		venv/bin/python manage.py runserver 0:8000
