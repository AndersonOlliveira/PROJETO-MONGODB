import datetime
import requests
import pandas as pd
import time
from models.colletion_repository import Coletion

# Caminho do arquivo com os CPFs (sem cabeçalho)
arquivo_entrada = 'arquivos/poucas_linhas.csv'
arquivo_saida = 'arquivos/saida_request.csv'


# # Lê o CSV sem cabeçalho
# dados_ = pd.read_csv(arquivo_entrada, sep=';', header=None)


def request_all(dados_,name,db):
    resultados = []

    colletion_repository = Coletion(name,db)

    for index, row in dados_.iterrows():
        cpf = str(row[0]).strip()
        print(f" Consultando CPF {index+1}/{len(dados_)}: {cpf}")

        # Monta o dicionário base
        registro = {
            'processo_id': 309,
            'contrato': 417039,
            'rede': 2620,
            'codcns': 272020, #360 E CLONE
            # 'codcns': 270309,
            'nome_arquivo': arquivo_entrada,
            'aceite_execucao': True,
            'mensagem_alerta': None,
            'data_cadastro': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'configuracao_json': '[{"plugin":111,"separar":true,"ocorrencias":10,"campos":[1,2,3,4,5,6]},{"plugin":311,"separar":false,"ocorrencias":1,"campos":[1,2]}]',
            'campos_aquisicao': 'tcpfcnpj',
            'loja': 134387,
            'finalizado': False,
            'data_finalizacao': None,
            'pause': False,
            'transacao_id': 2997520,
            'id_processo': 309,
            'campo_aquisicao': cpf,
            'status': 0,
            'sucesso': False,
            'data_cadastro_transacao': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'parametros': f'&tcpfcnpj={cpf}',
            'erro': False
        }

    
        # Monta a URL da requisição
        servidor = "proscore.com.br" # link para do servidor
        url = (
            f"https://{servidor}/cns/json.chp?"
            f"progestor_prc={registro['processo_id']}"
            f"&rde={registro['rede']}"
            f"&rdelja={registro['loja']}"
            f"&ctr={registro['contrato']}"
            f"&srvcns=1"
            f"&tcnscod={registro['codcns']}{registro['parametros']}"
        )

        # registro["url"] = url
        erro = registro.get('erro', False)
        resposta = ""

        if not erro:
            try:
                response = requests.get(url, timeout=(300, 300))
                response.raise_for_status()
                resposta = response.text

                # classLogger.logger.info(f"Resposta: {resposta[:100]}...")
                erro = False
            except requests.exceptions.Timeout:
                resposta = "TIMEOUT: Requisição excedeu 5 minutos"
                erro = True
                # classLogger.logger.error(f"Timeout na requisição: {url}")

            except requests.exceptions.RequestException as e:
                resposta = f"ERRO: {str(e)}"
                erro = True
                # classLogger.logger.error(f"Erro na requisição: {str(e)}")

        if not resposta or resposta.strip() == "" or len(resposta) == 2:
            resposta = "RESPOSTA NAO OBTIDA"
            erro = True

        registro['url'] = url
        registro['resposta_json'] = resposta
        registro['erro'] = erro

        # Guarda o resultado
        # registro["resposta_json"] = resposta_texto

        if registro['erro']:
                #//* step 7
                registro['resposta_json'] = 'ERRO NO PROCESSAMENTO'
                registro['new_status'] = 7
                registro['sucesso'] = False
        else:
                
                registro['new_status'] = 2
                registro['sucesso'] = True
             
        
        
        order = {
            "id": registro['processo_id'],
            "resposta_json": registro['resposta_json'],
            "new_status": registro['new_status'],
            "sucesso":  registro['sucesso']
        }
        
        get_id = colletion_repository.insert_document(order)
        resultados.append(registro)

      
        time.sleep(0.3)

    # Salva o resultado em CSV
    df_saida = pd.DataFrame(resultados)
    df_saida.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')

    print(f"\n Arquivo '{arquivo_saida}' salvo com {len(df_saida)} registros!")
    return resultados


# if __name__ == "__main__":
#     request_all(dados_)
