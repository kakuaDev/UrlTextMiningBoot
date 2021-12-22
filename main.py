from flask import Flask, request
from lib.lib import conteo_palabras

app = Flask(__name__)


@app.route("/conteo_palabras")
def count_words():
    """
    API que retorna el conteo de palabras de una URL determinada.
    EJ:
    .../count_words?url=http://kite.com

    :return: Lista de objetos (palabra, # de ocurrencias)
    """
    url = request.args.get('url')
    words_count = conteo_palabras(url)
    if words_count is None:
        return {
            "error": "No se pudo acceder al dominio: {url}. URL inválida".format(url=url)
        }
    return {"conteo": words_count}


@app.route("/pretty/conteo_palabras")
def count_words_pretty():
    """
    API que retorna el conteo de palabras de una URL determinada.
    EJ:
    .../pretty/count_words?url=http://kite.com

    :return: Lista de objetos (palabra, # de ocurrencias)
    """
    url = request.args.get('url')
    _n = request.args.get('n')
    n = int(_n) if _n.isnumeric() else None
    words_count = conteo_palabras(url)
    if words_count is None:
        return "No se pudo acceder al dominio: {url}. URL inválida".format(url=url)
    disp = len(words_count) if n is None or n > len(words_count) else n
    pretty = [
        "<b>{word}:</b> {count}".format(word=i, count=j)
        for i, j in words_count[:disp]
    ]
    return "<br>".join(pretty)


if __name__ == "__main__":
    app.run()
