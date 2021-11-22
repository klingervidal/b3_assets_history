import sys
import pymysql.cursors
from datetime import datetime as dt

class DataBase(object):
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.database = 'etl_b3_history'
        self.password = ''
        self.cursorclass = pymysql.cursors.DictCursor

    def conn(self):
        try:
            # Opening a conection
            conn = pymysql.connect(host = self.host, user = self.user, database = self.database, password = self.password, cursorclass = self.cursorclass)
            return conn
        except:
            return False


    def insert_data_mysql(self, asset_data):
        if asset_data is not None:
            conn = self.conn()
            if conn == False:
                sys.exit('Falha na conexão ao banco de dados')
            else:
                i = 0
                while i <= (len(asset_data) - 1):
                    tipo_registro = asset_data['tipo_registro'][i]
                    data_pregao = asset_data['data_pregao'][i]
                    cod_bdi = asset_data['cod_bdi'][i]
                    cod_negociacao = asset_data['cod_negociacao'][i]
                    tipo_mercado = asset_data['tipo_mercado'][i]
                    nome_empresa = asset_data['nome_empresa'][i]
                    especificacao_papel = asset_data['especificacao_papel'][i]
                    prazo_dias_merc_termo = asset_data['prazo_dias_merc_termo'][i]
                    moeda_referencia = asset_data['moeda_referencia'][i]
                    preco_abertura = asset_data['preco_abertura'][i]
                    preco_maximo = asset_data['preco_maximo'][i]
                    preco_minimo = asset_data['preco_minimo'][i]
                    preco_medio = asset_data['preco_medio'][i]
                    preco_ultimo_negocio = asset_data['preco_ultimo_negocio'][i]
                    preco_melhor_oferta_compra = asset_data['preco_melhor_oferta_compra'][i]
                    preco_melhor_oferta_venda = asset_data['preco_melhor_oferta_venda'][i]
                    numero_negocios = asset_data['numero_negocios'][i]
                    quantidade_papeis_negociados = asset_data['quantidade_papeis_negociados'][i]
                    volume_total_negociado = asset_data['volume_total_negociado'][i]
                    preco_exercicio = asset_data['preco_exercicio'][i]
                    indicador_correcao_precos = asset_data['indicador_correcao_precos'][i]
                    data_vencimento = asset_data['data_vencimento'][i]
                    fator_cotacao = asset_data['fator_cotacao'][i]
                    preco_exercicio_pontos = asset_data['preco_exercicio_pontos'][i]
                    codigo_isin = asset_data['codigo_isin'][i]
                    num_distribuicao_papel = asset_data['num_distribuicao_papel'][i]
                    num_distribuicao_papel = asset_data['num_distribuicao_papel'][i]
                    server_date = dt.now().strftime("%Y-%m-%d")

                    i+=1

                    with conn.cursor() as mysql:
                        sql = f"INSERT INTO asset_data_history (tipo_registro,data_pregao,cod_bdi,cod_negociacao,tipo_mercado,nome_empresa,especificacao_papel,prazo_dias_merc_termo,moeda_referencia,preco_abertura,preco_maximo,preco_minimo,preco_medio,preco_ultimo_negocio,preco_melhor_oferta_compra,preco_melhor_oferta_venda,numero_negocios,quantidade_papeis_negociados,volume_total_negociado,preco_exercicio,indicador_correcao_precos,data_vencimento,fator_cotacao,preco_exercicio_pontos,codigo_isin,num_distribuicao_papel,server_date) VALUES \
                                ({tipo_registro},'{data_pregao}',{cod_bdi},'{cod_negociacao}',{tipo_mercado},'{nome_empresa}','{especificacao_papel}','{prazo_dias_merc_termo}','{moeda_referencia}',{preco_abertura},{preco_maximo},{preco_minimo},{preco_medio},{preco_ultimo_negocio},{preco_melhor_oferta_compra},{preco_melhor_oferta_venda},{numero_negocios},{quantidade_papeis_negociados},{volume_total_negociado},{preco_exercicio},{indicador_correcao_precos},'{data_vencimento}',{fator_cotacao},{preco_exercicio_pontos},'{codigo_isin}',{num_distribuicao_papel},'{server_date}') \
                                ON DUPLICATE KEY UPDATE \
                                tipo_registro = {tipo_registro}, \
                                data_pregao = '{data_pregao}', \
                                cod_bdi = {cod_bdi}, \
                                cod_negociacao = '{cod_negociacao}', \
                                tipo_mercado = {tipo_mercado}, \
                                nome_empresa = '{nome_empresa}', \
                                especificacao_papel = '{especificacao_papel}', \
                                prazo_dias_merc_termo = '{prazo_dias_merc_termo}', \
                                moeda_referencia = '{moeda_referencia}', \
                                preco_abertura = {preco_abertura}, \
                                preco_maximo = {preco_maximo}, \
                                preco_minimo = {preco_minimo}, \
                                preco_medio = {preco_medio}, \
                                preco_ultimo_negocio = {preco_ultimo_negocio}, \
                                preco_melhor_oferta_compra = {preco_melhor_oferta_compra}, \
                                preco_melhor_oferta_venda = {preco_melhor_oferta_venda}, \
                                numero_negocios = {numero_negocios}, \
                                quantidade_papeis_negociados = {quantidade_papeis_negociados}, \
                                volume_total_negociado = {volume_total_negociado}, \
                                preco_exercicio = {preco_exercicio}, \
                                indicador_correcao_precos = {indicador_correcao_precos}, \
                                data_vencimento = '{data_vencimento}', \
                                fator_cotacao = {fator_cotacao}, \
                                preco_exercicio_pontos = {preco_exercicio_pontos}, \
                                codigo_isin = '{codigo_isin}', \
                                num_distribuicao_papel = {num_distribuicao_papel}, \
                                server_date = '{server_date}'"
                        
                        try:
                            mysql.execute(sql)
                        except:
                            print(sql)
                            sys.exit()

            conn.close()

            return True


    def get_data_inserted(self):
        today = dt.now().strftime("%Y-%m-%d")

        conn = self.conn()
        if conn == False:
            sys.exit('Falha na conexão ao banco de dados')
        else:
             with conn.cursor() as mysql:
                sql = f"SELECT \
                        A.id_asset_data_history as 'id_asset_data_history', \
                        A.tipo_registro as 'tipo_registro', \
                        A.data_pregao 'data_pregao', \
                        A.cod_bdi as 'cod_bdi', \
                        A.cod_negociacao as 'cod_negociacao', \
                        B.market_type_description as 'tipo_mercado', \
                        A.nome_empresa as 'nome_empresa', \
                        A.especificacao_papel as 'especificacao_papel', \
                        A.prazo_dias_merc_termo as 'prazo_dias_merc_termo', \
                        A.moeda_referencia as 'moeda_referencia', \
                        A.preco_abertura as 'preco_abertura', \
                        A.preco_maximo as 'preco_maximo', \
                        A.preco_minimo as 'preco_minimo', \
                        A.preco_medio as 'preco_medio', \
                        A.preco_ultimo_negocio as 'preco_ultimo_negocio', \
                        A.preco_melhor_oferta_compra as 'preco_melhor_oferta_compra', \
                        A.preco_melhor_oferta_venda as 'preco_melhor_oferta_venda', \
                        A.numero_negocios as 'numero_negocios', \
                        A.quantidade_papeis_negociados as 'quantidade_papeis_negociados', \
                        A.volume_total_negociado as 'volume_total_negociado', \
                        A.preco_exercicio as 'preco_exercicio', \
                        A.indicador_correcao_precos as 'indicador_correcao_precos', \
                        A.data_vencimento as 'data_vencimento', \
                        A.fator_cotacao as 'fator_cotacao', \
                        A.preco_exercicio_pontos as 'preco_exercicio_pontos', \
                        A.codigo_isin as 'codigo_isin', \
                        A.num_distribuicao_papel as 'num_distribuicao_papel', \
                        A.server_date as 'server_date' \
                    FROM \
                        asset_data_history A, \
                        market_type B \
                    WHERE \
                        A.tipo_mercado = B.id_market_type \
                    AND \
                        A.server_date = '{today}' \
                    ORDER BY A.id_asset_data_history DESC"

                try:
                    mysql.execute(sql)
                    data_inserted = mysql.fetchall()
                except:
                    data_inserted = None
                    
        return data_inserted


