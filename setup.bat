@ECHO
:: This batch file setup django and run dev server
:: Only works if git is installed and python3.9 is installed in windows
:: all string 'placeholder' should be replaced by django_eth
:: check IPv4 address in advance by ipconfig | grep IPv4
cd C:\Users\Owner\Desktop
IF EXIST "django_eth" (
  ECHO directory already exists
) ELSE (
  mkdir django_eth
)
cd C:\Users\Owner\Desktop\django_eth
IF EXIST ".git" (
  git fetch
) ELSE (
  git clone https://github.com/oeawFebe/testtest .
  set CURRENT_COMMIT=
  git log -n 1 --format="%%H">django_eth.txt
  set /P CURRENT_COMMIT=<%CD%\django_eth.txt
  git reset --hard %CURRENT_COMMIT%
  del %CD%\django_eth.txt
  set CURRENT_COMMIT=
)
IF EXIST "venv" (
  ECHO venv already exists
) ELSE (
  py -3.9 -m venv venv
)
cd C:\Users\Owner\Desktop\django_eth\django_eth
C:\Users\Owner\Desktop\django_eth\venv\Scripts\pip.exe install -r requirements.txt
C:\Users\Owner\Desktop\django_eth\venv\Scripts\python.exe manage.py migrate --noinput
C:\Users\Owner\Desktop\django_eth\venv\Scripts\python.exe manage.py makemigrations
C:\Users\Owner\Desktop\django_eth\venv\Scripts\python.exe manage.py migrate --noinput
C:\Users\Owner\Desktop\django_eth\venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000
PAUSE