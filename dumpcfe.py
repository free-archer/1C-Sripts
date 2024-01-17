import os
import shutil
import subprocess

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

args = f'infobase config export {CF_FILES} --extension={EXT_NAME} --dbms=postgresql --db-server={SRV} --db-name={BASE} --db-user={DB_USER} --db-pwd={DB_PASS} --user="{USER}" --password={PASS}'

start_command = f"{ibcmd} {args}"

print(start_command)

try:
    procc = subprocess.check_output(start_command, shell=True)
except:
    print("error")


