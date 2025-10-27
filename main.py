# python -m venv .venv AMBIENTE VIRTUAL
#  pip freeze > requirements.txt

# pip install pymongo python-dotenv
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# # .\.venv\Scripts\Activate.ps1
# Bash

# .\.venv\Scripts\Activate.ps1\

from classLogger import logger_finalizar
import time
import datetime

def main():
     
    logger_finalizar.info(f"[{time.strftime('%H:%M:%S')}] Iniciando loop contínuo...")



if __name__ == "__main__":
     main()
