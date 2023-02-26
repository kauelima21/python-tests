import json
import pandas as pd
import boto3


def load_s3_file():
    pla = pd.read_excel('planilha.xlsx')
    return pla['nome']


def lambda_handler(event, context):
    names = load_s3_file()
    names_str = ''
    for name in names:
        names_str += f'{name}, '

    return names_str


if __name__ == '__main__':
    print(lambda_handler(None, None))

