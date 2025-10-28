from conection.Conexao import mongoConect
from models.colletion_repository import Coletion
from request.request_url import request_all
import pandas as pd
   

conn = mongoConect()
print(f" minha conexao {conn}")


if conn:
    db = conn.get_db_connection()
    collection = db.get_collection(conn.get_db_colletion())
    connection = db
    print(f"Collection: {collection.name}")
    print(f"--"*20)
    print(f"Conexao: {db}")
    

    colletion_repository = Coletion(collection.name,db)
    

    order = {
           'estou aqui': 'inserindo',
           'Numero': [123,31231,5454,545,'121'],
           "dasata": "dsadas",
           "NEW TESTE": "dd"
    }
    arquivo_entrada = 'arquivos/poucas_linhas.csv'
    arquivo_saida = 'saida.csv'
    dados_ = pd.read_csv(arquivo_entrada, sep=';', header=None)


    #chamo a funcao request
    result_request = request_all(dados_,collection.name,db)



    # get_id = colletion_repository.insert_document_may(order)
    
    print(f"id de retorno  {result_request}")
# conn = db_handle.get_db_connection()

# db_handle.connect_to_db()
# conn1 = db_handle.get_db_connection()

# print(f"minha colecction {conn1}")


# print("---" *20)

# collection = conn1.get_collection(db_handle.get_db_colletion())

# print(f"meu nome da colletion {collection}")

# collection.insert_one({
#     'estou aqui': 'inserindo',
#     'Numero': [123,31231,5454,545,'121']
# })


