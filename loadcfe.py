import os
import shutil
import subprocess
import time

VER = "8.3.23.2040"
CF_FILES = "C:/TEMP/CF"
SRV = "localhost"
BASE = "utdemo"
DB_PASS = "cnhtkjr"
DB_USER = "postgres"
USER = "Администратор (ОрловАВ)"
PASS = ""
EXT_NAME = "НовогоднееОформление"

if os.path.exists(CF_FILES):
    shutil.rmtree(CF_FILES)

ProgramFiles = os.environ["ProgramFiles"]

ibcmd = f'"{ProgramFiles}/1cv8/{VER}/bin/ibcmd.exe"'
c1cmd = f'"{ProgramFiles}/1cv8/{VER}/bin/1cv8.exe"'

print("Загрузка конфигурации")
Command = "export"
args = f'infobase config {Command} {CF_FILES} --extension={EXT_NAME} --dbms=postgresql --db-server={SRV} --db-name={BASE} --db-user={DB_USER} --db-pwd={DB_PASS} --user="{USER}" --password={PASS}'
start_command = f"{ibcmd} {args}"

try:
    procc = subprocess.check_output(start_command, shell=True)
except:
    print("Ошибка загрузки конфигурации")

print("Обновление базы данных")
Command = "apply"
args = f'infobase config {Command} --extension={EXT_NAME} --dbms=postgresql --db-server={SRV} --db-name={BASE} --db-user={DB_USER} --db-pwd={DB_PASS} --user="{USER}" --password={PASS} --force'
start_command = f"{ibcmd} {args}"
try:
    procc = subprocess.check_output(start_command, shell=True)
except:
    print("Ошибка обновления базы данных")

print("Запуск 1С")
args = f'ENTERPRISE /S{SRV}\\{BASE} /N"{USER}" /P{PASS}'
start_command = f"{c1cmd} {args}"
try:
    procc = subprocess.check_output(start_command, shell=True)
except:
    print("Ошибка запуска 1С")    

