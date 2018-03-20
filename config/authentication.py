# CLASSE COM TODOS OS DADOS DE AUTENTICACAO DO SISTEMA

import os

class Authentication:

    # DEV: 0 - PROD: 1
    AMBIENTE = 1

    VERIFY_TOKEN = os.environ["VERIFY_TOKEN"] if AMBIENTE else "Robo de Auxilio Virtual ao Aprendizado"

    PAGE_ACCESS_TOKEN = os.environ["PAGE_ACCESS_TOKEN"] if AMBIENTE else "EAAHwwukij0sBAJusB57jWvWZAmwzC1IQcuTypgkyDXqSeSfInbZBBpBfoysTx8OstqZCiLnB5JoeUW9rTLADtKyGW06qc2iB9S1xodhZCKLxJACfXTjJOtZCw0cFZAVN0d41CHVfvzhYFGxORIz5d6ZBSA8yQDfz7yFtSXWIfaYe51sJY6haET5"

    ZONE = "America/Sao_Paulo"

    WIT_TOKEN = os.environ["WIT_TOKEN"] if AMBIENTE else "L7HSK2267XRKO3LIV74ZMIP7RHA7QXBP"

    DATABASE_URL = os.environ['DATABASE_URL'] if AMBIENTE else "postgres://rqgfhrkhkdoilb:9340a3429174c2ee3d47da003de88cf40882c5cb4626c612f83617d0d868433b@ec2-54-83-35-31.compute-1.amazonaws.com:5432/d4jc8iv6u03o2v"