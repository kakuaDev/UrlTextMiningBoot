from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def conteo_palabras(url):
    """
    Método para la obtención del número de ocurrencias por palabra de una URL

    :param url: URL
    :return: Lista de objetos (palabra, # de ocurrencias)
    """
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    raw_text = soup.text

    # Eliminar caracteres especiales
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', raw_text)
    words = text.split()
    words_count = []
    _words = []
    for word in words:
        if word not in _words:
            _words.append(word)
            words_count.append([word, text.count(word)])
    words_count = sorted(words_count, key=lambda x: x[1], reverse=True)
    return words_count


if __name__ == "__main__":
    pass
