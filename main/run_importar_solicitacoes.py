from config.mysql import MySqlConfig
from util.mysql import MySqlConnection
import csv

# instanciando configurações
mysql_config = MySqlConfig('mysql-pacient_analysis')


def retornar_dados_arquivo_as_list():
    arr_retorno = []

    input_file = csv.reader(
        open("../arquivos/gerint_solicitacoes_mod.csv", encoding='utf-8'),
        delimiter=';',
    )

    next(input_file)

    for row in input_file:
        # print(row)
        arr_retorno.append(row)

    return arr_retorno


def importar_dados():
    # configurar consulta insert
    str_insert = "insert into pacientes (data_extracao, id_usuario, situacao, central_regulacao_origem, data_solicitacao, sexo, idade, municipio_residencia, solicitante, municipio_solicitante, codigo_cid, carater, tipo_internacao, tipo_leito, data_autorizacao, data_internacao, data_alta, executante, horas_na_fila) \
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # retornar os dados do arquivo em lista
    arr_dados = retornar_dados_arquivo_as_list()

    # inserir os dados
    conn = MySqlConnection(mysql_config)
    conn.truncate_table('pacientes')
    conn.insert_list(str_insert, arr_dados)


if __name__ == '__main__':
    importar_dados()
