# PyEditorial
## SonarQube Test Result
1. Initial Test Result
<img src="https://i.ibb.co/Cmg3TnF/Screen-Shot-2020-12-21-at-08-05-15.png" width="400">
there's 9 bugs and 7 security hotspot

2. 2nd Test Resutl. We did some improvement in security matter, and below is the test result
<img src="https://i.ibb.co/c6vCD44/Screen-Shot-2020-12-21-at-09-44-29.png" width="400">
We success eliminate security hotspot issue.

## Heroku Deployed
https://pyeditorial.herokuapp.com/

## Abstract

## Feature
Feature in this project.

Admin:
1. Login/Register as an admin.
2. Manage (add/delete/edit) blog page
3. Manage (add/delete/edit) Blog categorys 	
4. Manage (add/delete/edit) Faqs 	
5. Manage (add/delete/edit) Podcast categorys 	
6. Manage (add/delete/edit) Podcasts 	
7. Manage (add/delete/edit) Skills 	
8. Manage (add/delete/edit) Videocast categorys 	
9. Manage (add/delete/edit) Videocasts

User:
1. Look on a blogpage, and group by category
2. Look on a videocast page, and group by category
3. Look on a podcast page, and group by category
4. Look on a faq page

## Initialisation
After you clone this repository, let's make sure you installed all requirements, migrate, and collect static.
```bash
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
```

## Running Development Environment
To run the server:

```bash
python3 manage.py runserver
```

You can see the app running by going to `http://127.0.0.1:8000/` via your browser.

To run the test:
```bash
python3 functional_tests.py
```

## Making Changes
Please make sure your changes conform to [`Style Guide for Python Code`](https://python.org/dev/peps/pep-0008/) (PEP8)<br>
Check that it complies with pep8
```bash
autopep8 functional_tests.py
```
fixing code to complies with pep8
```bash
autopep8 functional_tests.py --in-place
```
