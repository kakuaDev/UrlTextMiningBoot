from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def conteo_palabras(raw_text):
    """
    Método para la obtención del número de ocurrencias por palabra

    :param raw_text: Texto
    :return: Lista de objetos (palabra, # de ocurrencias)
    """
    # Eliminar caracteres especiales
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', raw_text)
    words = text.split()
    words_count = []
    _words = []
    for word in ords:
        if word not in _words:
            _words.append(word)
            words_count.append((word, text.count(word)))
    words_count = sorted(words_count, key=lambda x: x[1], reverse=True)
    return words_count


if __name__ == "__main__":
    url = "http://kite.com"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    urlText = soup.text
    print(conteo_palabras(urlText))
