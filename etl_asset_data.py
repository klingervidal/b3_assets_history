import sys
import pandas as pd

class EtlAssetData(object):
    def validate_file_content(self, path):
        file = open(path,'r')

        header = file.readline()

        validantion_1 = header[0:2]
        validantion_2 = header[2:6]
        validantion_3 = header[6:10]
        validantion_4 = header[10:11]
        validantion_5 = header[15:22]

        return validantion_1 == '00' and validantion_2 == 'COTA' and validantion_3 == 'HIST' and validantion_4 == '.' and validantion_5 == 'BOVESPA'
            

    def etl(self, path):
        ## History series available at
        ## http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/
        bovespa_file = path

        ## Structure file available at
        ## http://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf
        # Matriz pharse structure 
        size_files = [2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,13,5,18,18,13,1,8,7,13,12,3]

        asset_data = pd.read_fwf(bovespa_file, widths=size_files, header=0)

        # Change columns name
        asset_data.columns = [
                                "tipo_registro","data_pregao","cod_bdi","cod_negociacao",
                                "tipo_mercado","nome_empresa","especificacao_papel",
                                "prazo_dias_merc_termo","moeda_referencia","preco_abertura",
                                "preco_maximo","preco_minimo","preco_medio","preco_ultimo_negocio",
                                "preco_melhor_oferta_compra","preco_melhor_oferta_venda","numero_negocios",
                                "quantidade_papeis_negociados","volume_total_negociado","preco_exercicio",
                                "indicador_correcao_precos","data_vencimento","fator_cotacao",
                                "preco_exercicio_pontos","codigo_isin","num_distribuicao_papel"
                            ]

        # Removing the last line
        line = len(asset_data["data_pregao"])
        asset_data = asset_data.drop(line-1)

        # Formating columns date
        asset_data['data_pregao'] = asset_data['data_pregao'][0][0:4] + '-' + asset_data['data_pregao'][0][4:6] + '-' + asset_data['data_pregao'][0][6:8]
        asset_data['data_vencimento'] = str(asset_data['data_vencimento'][0])[0:4] + '-' + str(asset_data['data_vencimento'][0])[4:6] + '-' + str(asset_data['data_vencimento'][0])[6:8]
        
        # Formating columns price
        # It's necessary to adjust monetary values (splitting by 100)
        monetaryColumnsList = [
                        "preco_abertura","preco_maximo","preco_minimo",
                        "preco_medio","preco_ultimo_negocio","preco_melhor_oferta_compra",
                        "preco_melhor_oferta_venda","volume_total_negociado",
                        "preco_exercicio","preco_exercicio_pontos"
                    ]

        for column in monetaryColumnsList:
            asset_data[column]=[i/100. for i in asset_data[column]]
        
        # asset_data = asset_data.to_dict()
        return asset_data


    def convert_to_list(self, original_data):
        data_list = []
        for data in original_data:
            data_list.append([
                                data['id_asset_data_history'],
                                data['tipo_registro'],
                                data['data_pregao'],
                                data['cod_bdi'],
                                data['cod_negociacao'],
                                data['tipo_mercado'],
                                data['nome_empresa'],
                                data['especificacao_papel'],
                                data['prazo_dias_merc_termo'],
                                data['moeda_referencia'],
                                data['preco_abertura'],
                                data['preco_maximo'],
                                data['preco_minimo'],
                                data['preco_medio'],
                                data['preco_ultimo_negocio'],
                                data['preco_melhor_oferta_compra'],
                                data['preco_melhor_oferta_venda'],
                                data['numero_negocios'],
                                data['quantidade_papeis_negociados'],
                                data['volume_total_negociado'],
                                data['preco_exercicio'],
                                data['indicador_correcao_precos'],
                                data['data_vencimento'],
                                data['fator_cotacao'],
                                data['preco_exercicio_pontos'],
                                data['codigo_isin'],
                                data['num_distribuicao_papel'],
                                data['server_date']
                            ])

        return data_list