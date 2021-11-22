import sys
import PySimpleGUI as sg
import etl_asset_data as etl
import data_base
from datetime import datetime as dt


sg.theme("DarkTeal10")


def create_main_window():
    layout = [
        [   
            sg.Text("Selecione o seu arquivo TXT"),
            sg.In(key="-FILE-"),
            sg.FileBrowse("Selecionar", file_types=(("ALL files", "*.txt"),))
        ],
        [
            sg.Text("Aguarde a importação dos dados", text_color='orange')
        ],
        [
            sg.Button("Importar para o MySQL", key="-START-", size=(20,1), button_color=('white', 'SeaGreen4')),
            sg.Button("Finalizar Programa", key="-FINISH-", size=(20,1), button_color=('white', 'firebrick4'))
        ]
    ]

    window = sg.Window("Importação dados B3", layout)

    return window


def create_second_window():
    today = dt.now().strftime("%d/%m/%Y")

    # Instantiating Data Base
    data_obj = data_base.DataBase()    
    data_inserted = data_obj.get_data_inserted()

    # Instantiating ETL Object with
    etl_obj = etl.EtlAssetData()
    data_inserted_list = etl_obj.convert_to_list(data_inserted)

    layout = [
        [   
            sg.Text(f"Dados Importados em {today}")
        ],
        [   
            sg.Table(values=data_inserted_list, headings=[  'IdData', 'Tipo de Registro', 'Data do Pregão',
                                                            'Cód. BDI', 'Cód. Negociação', 'Tipo de Mercado',
                                                            'Nome Empresa', 'Especificação do Papel', 'Prazo Dias Mercado a Termo',
                                                            'Moeda Refrência', 'Preço de Abertura', 'Preço Máximo', 'Preço Mínimo',
                                                            'Preço Médio', 'Preço Último Negócio', 'Preço Melhor Oferta de Compra',
                                                            'Preço Melhor Oferta de Venda', 'Número de Negócios', 'Quantidade de Papéis Negociados',
                                                            'Volume Total Negociado', 'Preço Exercício', 'Indicador de Correção de Preços',
                                                            'Data Vencimento', 'Fator Cotação', 'Preço Exercício Pontos',
                                                            'Cód. ISIN', 'Número Distribuição Papel', 'Data da Importação'
                                                        ], num_rows=min(30, len(data_inserted_list)))
        ],
        [
            sg.Text("")
        ],
        [
            sg.Text("")
        ],
        [   
            sg.Button("Voltar", key="-BACK-", button_color=('white', 'orange')),
            sg.Button("Finalizar Programa", key="-FINISH-", button_color=('white', 'firebrick4'))
        ]
    ]

    window = sg.Window(f"Dados Importados em {today}", layout, location=(55,0), size=(1300,790), resizable = True)

    return window


main_window = create_main_window()
active_window = main_window


# Managing windows
while True:
    event, values = active_window.read()

    if event == "-START-":
        if values['-FILE-'] != '':
            
            # Instantiating ETL Object with
            etl_obj = etl.EtlAssetData()

            valid_file_format = etl_obj.validate_file_content(values['-FILE-'])

            if not valid_file_format:
                sg.Popup('Conteúdo do arquivo com formato fora do padrão. Favor verificar o cabeçalho.', keep_on_top=True)
            else:

                # Getting transformed data
                asset_data = etl_obj.etl(values['-FILE-'])

                # Instantiating Data Base
                data_obj = data_base.DataBase()

                # Seting data to MySql Data Base
                insert_finish = data_obj.insert_data_mysql(asset_data)

                if insert_finish:
                    main_window.hide()
                    active_window = create_second_window()
        else:
            sg.Popup('Favor selecionar o arquivo a ser carregado no campo "Selecione o seu arquivo TXT"', keep_on_top=True)
    
    elif event == "-BACK-":
        active_window.hide()
        active_window = create_main_window()
    
    elif event == "-FINISH-":
        break

    # Closes if the user requires the window to close
    if event == sg.WIN_CLOSED:
        break