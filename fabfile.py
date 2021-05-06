from fabric.contrib.files import append, exists
from fabric.api import cd,env,local,run
import os
REPO_URL=r'https://github.com/oeawFebe/testtest'
SITE_FOLDER=r'C:\Users\Owner\Desktop\django_eth'

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
        current_commit=local('git log -n 1 --format=%H',capture=True)
    run(f'git reset --hard {current_commit}')

def _update_venv():
    path_=os.path.join(SITE_FOLDER,r'venv\Scripts\pip.exe')
    if not os.path.exists(path_):
        run('python -m venv venv')
    run(r'venv\Scripts\activate')
    run(r'pip install -r requirements.txt')

def _update_database():
    # apply SQLmigrations for auth, etc.
    run('python manage.py migrate --noinput')
    # create SQLmigrations for models.
    run('python manage.py makemigrations')
    # apply SQLmigrations for models.
    run('python manage.py migrate --noinput')

def deploy():
    if not os.path.exists(SITE_FOLDER):
        os.mkdir(SITE_FOLDER)

    with cd(SITE_FOLDER):
        _get_latest_source()
        _update_venv()
        _update_database()
    

# cd to C:\Users\Owner\Desktop\django_eth\django_eth
# type fab deploy:localhost ->ssh connection trouble

# 2nd option is use bash

if __name__=='__main__':
    deploy()




