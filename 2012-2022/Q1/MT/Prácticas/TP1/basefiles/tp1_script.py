import spacy, os
from spacy.tokenizer import Tokenizer



def get_raw_text(filename):
    # Leemos el fichero de prueba
    raw_text = open(filename, 'r')

    plain_text = ''  # Texto Puro
    all_words_tags = []  # Lista de Listas [palabra, categoría]
    for i, line in enumerate(raw_text):

        if not (line == '\n'):
            # Separamos el contenido de la linea y nos aseguramos
            # de quitar de los espacios extras
            word, tag = line.strip().split()

            plain_text += word + ' '
            all_words_tags.append([word, tag])
        else:
            # Omitiremos añadir a la lista los casos que son '\n'
            plain_text += line

    # Nos aseguramos que el texto completo no tenga espacios demás
    plain_text = plain_text

    # Cerramos el fichero
    raw_text.close()

    return plain_text, all_words_tags


def spacy_tokenizer(nlp):
    return Tokenizer(nlp.vocab)


"""Evaluamos el texto con el etiquetador de entidades Spacy.
Obtemos tambien un diccionario con el mismo formato"""
def get_spacy_tag(text):
    all_words_tags = []  # Diccionario de linea (palabra, categoría)

    # Cargamos el Modelo de Spacy en Español
    nlp = spacy.load("es_core_news_lg")
    nlp.tokenizer = spacy_tokenizer(nlp)

    # Aplicamos nuestro texto al Spacy
    doc = nlp(text)
    tag = ""

    for i, word in enumerate(doc):
        if not (word.text == '\n'):
            if (word.ent_iob_ == 'O'):
                tag = word.ent_iob_
            else:
                tag = word.ent_iob_ + '-' + word.ent_type_
            all_words_tags.append([word.text, tag])

    return all_words_tags


"""Comparamos las lineas generadas por Spacy con las del Test.
En caso de que no coincidan escribimos un fichero de error  que nos diga la linea 
que esparaba (Spacy) y que ha recibido (Test). En caso contrario,
lo almacenamos en un fichero  de salida """


def write_output_error_files(test_dict, spacy_dict):
    i = 0
    output_file = open('output', 'w')

    for token in test_dict:
        word, tag = token
        word_, pred = spacy_dict[i]

        if word.strip() == word_.strip():
            output_file.write(word + ' ' + tag + ' ' + pred + ' \n')

        i += 1
    output_file.close()


if __name__ == '__main__':
