from conection.conexao_mongo import DBMongoManager
from typing import Dict,List
    #iniciando a conexao

class Coletion:
    
    def __init__(self,db_colletion,db_connection) -> None:
        self.__name_colletion = db_colletion
        self.__db_connection = db_connection

   
    def insert_document(self,document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__name_colletion)
        result = collection.insert_one(document)
        document['_id'] = result.inserted_id
        return document 
    
    def insert_document_may(self,document_list: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__name_colletion)
        result = collection.insert_many(document_list)
        # document_list['_id'] = result.inserted_id
        return result

