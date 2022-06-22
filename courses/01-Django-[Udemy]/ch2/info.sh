# Course: Python Django - The Practical Guide 2022 June
# Setting and config django
# Install Djngo (Globally)
$ python3 -m pip install Django
# update pip
$ python3 -m pip install --upgrade pip
# run
$ django-admin
# create new project
$ django-admin startproject [project_name]
# run project
$ python3 manage.py runserver
# create new app
$ python3 manage.py startapp [app_name]
# Setting pre-commit
1. pip install pre-commit
2. pre-commit --version
3. pre-commit install
# if you got this erro: [ERROR] Cowardly refusing to install hooks with core.hooksPath
# run this cmd 
4. git config --global --unset-all core.hooksPath
