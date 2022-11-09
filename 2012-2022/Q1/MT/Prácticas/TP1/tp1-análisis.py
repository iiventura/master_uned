#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy, os 
from spacy.tokenizer import Tokenizer

""" Paso 1: 1.	Leer los datos del fichero esp.testb
 y transformar la información en estructura de datos"""
def get_raw_text(filename):
    # Leemos el fichero de prueba
    raw_text = open(filename, 'r')

    plain_text = '' #Texto Puro
    all_words_tags = [] # Lista de linea (palabra, categoría)
    
    for i,line in enumerate(raw_text):
        
        if not (line == '\n'):
            # Separamos el contenido de la linea y nos aseguramos de los espacios
            word, tag = line.strip().split()

            plain_text += word + ' '
            all_words_tags.append([word, tag])
        else:
            # Omitiremos en el diccionario los casos que son '\n'
            plain_text += line
    
    #Nos aseguramos que el texto completo no tenga espacios demás
    plain_text= plain_text
    
    # Cerramos el fichero
    raw_text.close()
            
    return plain_text, all_words_tags


""" Paso 2: Cargar el modelo Spacy, aplicarle el
texto plano y almacenar los resultados en una estructura de datos."""
def get_spacy_tag(text):
    all_words_tags = [] # Lista de linea (palabra, categoría)
    
    #Cargamos el Modelo de Spacy en Español 
    nlp = spacy.load("es_core_news_lg")
   
    # Aplicamos nuestro texto al Spacy
    doc = nlp(text)
    tag = ""
    
    for i, word in enumerate(doc):
        if not(word.text == '\n'):
            if (word.ent_iob_ == 'O'):
                tag = word.ent_iob_
            else:
                 tag = word.ent_iob_ + '-' + word.ent_type_
            all_words_tags.append([word.text, tag])
            
    return all_words_tags
     
""" Paso 3: """
def write_output_error_files(test_dict, spacy_dict):
    i = 0
    output_file = open('output', 'w')
    error_file = open('error', 'w')
    
    for token in test_dict:
        word, tag = token
        word_, pred = spacy_dict[i]
        
        if word.strip() == word_.strip():
            output_file.write(word + ' ' + tag + ' ' + pred + ' \n')
        else:
            error_file.write('Expected: '+ word +' Received:'+ word_ + '\n')
            i += 1
        
        i += 1
    error_file.close()
    output_file.close()
    
    
if __name__ == '__main__':
    text, test_lines  = get_raw_text('esp.testb')
    
    print("Characters from Plain Text:", len(text))
    print("Total Words from File:", len(test_lines))
    
    spacy_lines = get_spacy_tag(text)
    print("Total Words from Spacy:", len(spacy_lines))
    
    write_output_error_files(test_lines, spacy_lines )
    
   
    


# In[ ]:


#! python conlleval.py < output

