import re
import pandas as pd
import PyPDF2

pdf = open("pdf/Ebook-WTICIFES2019.pdf","rb")
reader = PyPDF2.PdfReader(pdf)
pages = reader.pages
pages_to_extract = [ # useless by now
    9,15,22,28,
    35,41,47,53,
    59,65,71,76,
    82,87,93,99,
    105,110,116,122,
    128,133,140,145,
    151,157,164,170,
    176,182,188,194,
    200,206,212,218,
    224,230,236,245,
    251,257,263,269,
    275,281,287,293,
    299,305,311,318,
    324,330,336,342,
    348,352,360,366,
    372,378,384
]


def pdf_to_text():
    """Transforma o PDF do wticifes em um arquivo txt"""
    
    with open("text/full.txt","w") as file:
        for page in pages:
            file.write(page.extract_text())
    print("Arquivo full.txt gerado")


def get_resume():
    """Pega todos os resumos e retorna um objeto Series"""

    query = r"Resumo([\w\W]*?)(1. I)"
    pattern = re.compile(query)
    text = ''


    with open("text/full.txt", "r") as arquivo:
        text = arquivo.read()

    list_items = []

    for i in pattern.findall(text):
        list_items.append(i[0])

    return pd.Series(list_items).to_csv()


def authors_and_titles(): # not working yet
    """cria arquivos txt dos autores e títulos"""

    pdf = open("pdf/Ebook-WTICIFES2019.pdf","rb")
    pages = PyPDF2.PdfReader(pdf).pages
    summary = ''

    for page in pages[4:8]:
        summary += page.extract_text()
    
    query = r"\n([\W\w]*?)(\.\.)" 
    pattern = re.compile(query)

    list_all = [item[0].replace("\n","") for item in pattern.findall(summary) ] # if len(item[0]) > 0]

    # list_all = [i.replace("\n","") for i in list_all if len(i) > 0]

    pattern_titles = r"(?<=[a-z])[A-Z].*"

    return [el for el in list_all if len(el) > 0]

def get_topics():
    """retorna todos os títulos dos capítulos em formato csv"""
    output_list = []
    for p in pages[4:10]:
        pattern = r"[A-Z].*?\..*\d"
        try:
            topic_list = re.findall(pattern,p.extract_text())
            for topic in topic_list:
                out = str(topic).replace(".","").strip()
                output_list.append(re.sub(pattern=r"[0-9]+",string=out,repl=""))
        except Exception as e:
            print("Erro:\n", e)
            break
    return pd.Series(output_list)