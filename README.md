# Shopping List Application

**The Shopping List Application** is a web-based application whose purpose is to help its users to create, manage, share and delete their shopping lists for the things they would like to do buy.

## Technologies
1. Python==3.6.1
2. click==6.7
3. Flask==0.12.2
4. itsdangerous==0.24
5. Jinja2==2.9.6
6. MarkupSafe==1.0
7. nose==1.3.7
8. Werkzeug==0.12.2

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