run:
	uvicorn main:app --reload

freeze:
	pip freeze > ./requirements.txt

docs:
	google-chrome http://127.0.0.1:8000/docs
