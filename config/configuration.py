# CLASSE COM TODOS OS DADOS DE AUTENTICACAO DO SISTEMA

import os

class Configuration:

    # DEV: 0 - PROD: 1
    AMBIENTE = 1

    VERIFY_TOKEN = os.environ["VERIFY_TOKEN"] if AMBIENTE else "Robo de Auxilio Virtual ao Aprendizado"

    PAGE_ACCESS_TOKEN = os.environ["PAGE_ACCESS_TOKEN"] if AMBIENTE else "EAAHwwukij0sBAJusB57jWvWZAmwzC1IQcuTypgkyDXqSeSfInbZBBpBfoysTx8OstqZCiLnB5JoeUW9rTLADtKyGW06qc2iB9S1xodhZCKLxJACfXTjJOtZCw0cFZAVN0d41CHVfvzhYFGxORIz5d6ZBSA8yQDfz7yFtSXWIfaYe51sJY6haET5"

    ZONE = "America/Sao_Paulo"

    WIT_TOKEN = os.environ["WIT_TOKEN"] if AMBIENTE else "L7HSK2267XRKO3LIV74ZMIP7RHA7QXBP"

    DATABASE_URL = os.environ['DATABASE_URL'] if AMBIENTE else "postgres://iventorim:senhanti@localhost:5432/rava"

    db = None