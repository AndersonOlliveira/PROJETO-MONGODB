# python -m venv .venv AMBIENTE VIRTUAL
#  pip freeze > requirements.txt

# pip install pymongo python-dotenv
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# # .\.venv\Scripts\Activate.ps1
# Bash

# .\.venv\Scripts\Activate.ps1\

from logger.classLogger import logger_finalizar
import time
import datetime
import conection.conexao_mongo import 
def main():
    
     logger_finalizar.info(f"[{time.strftime('%H:%M:%S')}] Iniciando teste para inserir dados e conexao com o mongodb...")
     bd = Client.get_database('progesto_Colletion')
     print(f"meu data base{bd}")
     colecao = bd.get_collection('progestor_transaction')
     dado = {
    "nome": "anderson Oliveira araujo",
    "telefone":"19971101711"
    }
     colecao.insert_one(dado)


if __name__ == "__main__":
     main()
