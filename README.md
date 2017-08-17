# Shopping List Application
[![Build Status](https://travis-ci.org/Sekams/shopping_list.svg?branch=master)](https://travis-ci.org/Sekams/shopping_list)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/11fc4593f01d42d9af9fd30b8670ebcc)](https://www.codacy.com/app/Sekams/shopping_list?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sekams/shopping_list&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/Sekams/shopping_list/badge.svg?branch=master)](https://coveralls.io/github/Sekams/shopping_list?branch=master)
[![Code Climate](https://codeclimate.com/github/Sekams/shopping_list/badges/gpa.svg)](https://codeclimate.com/github/Sekams/shopping_list)

**The Shopping List Application** is a web-based application whose purpose is to help its users to create, manage, share and delete their shopping lists for the things they would like to do buy.

## Technologies
1. Python==3.6.1
2. astroid==1.5.3
3. click==6.7
4. colorama==0.3.9
5. Flask==0.12.2
6. isort==4.2.15
7. itsdangerous==0.24
8. Jinja2==2.9.6
9. lazy-object-proxy==1.3.1
10. MarkupSafe==1.0
11. mccabe==0.6.1
12. nose==1.3.7
13. pylint==1.7.2
14. six==1.10.0
15. Werkzeug==0.12.2
16. wrapt==1.10.11
17. coverage==4.4.1

## Getting Started
To be able to use the application locally, one should follow the guidelines highlighted below.

1. Clone/download the application Github repository by running the command below in a git shell
```
git clone https://github.com/Sekams/shopping_list.git
```
2. Set up a virtual environment (follow instructions at: http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

3. Install the application requirements by running the code below in the virtual environment:
```
pip install -r requirements.txt
```
4. After all the requirements are installed on the local virtual environment, run the application by running the following code in the virtual environment:
```
python run.py
```
5. After successfully running the application, one can explore the features of the BucketList app by navigation to the address: http://127.0.0.1:5000 in any web browser of choice

## Features
* Account creation
* User session manegement (Login and Logout)
* Shopping list creation, management and delete
* Shopping list item creation, management and delete
* Shopping list sharing

## Testing
The application's tests can be executed by running the code below within the virtual environment:
```
python test_script.py
```