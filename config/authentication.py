# CLASSE COM TODOS OS DADOS DE AUTENTICACAO DO SISTEMA

import os

class Authentication:

    # urlparse.uses_netloc.append("postgres")
    # __url = urlparse.urlparse(os.environ["DATABASE_URL"])

    # DATABASE_PS = __url.path[1:]

    # USER_PS = __url.username

    # PASSWORD_PS = __url.password

    # HOST_PS = __url.hostname

    # PORT_PS = __url.port

    # REDIS_URL = os.environ.get("REDIS_URL")

    VERIFY_TOKEN = os.environ["VERIFY_TOKEN"]

    PAGE_ACCESS_TOKEN = os.environ["PAGE_ACCESS_TOKEN"]

    ZONE = "America/Sao_Paulo"

    WIT_TOKEN = "L7HSK2267XRKO3LIV74ZMIP7RHA7QXBP"