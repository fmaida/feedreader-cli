#!./.venv/bin/python
# -*- coding: utf-8 -*-

import os
import textwrap

import feedparser
from html2text import HTML2Text


def analizza_feed(url):
    """
    Scarica da internet un feed RSS o ATOM e poi
    restituisce una lista di tuple (titolo, sommario, url)
    """
    
    feed = feedparser.parse(url)

    h = HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = True
    elenco = []
    for post in feed.entries:
        title = post["title"]
        summary = h.handle(post["summary"]).strip()
        url = post["link"]

        # A meno che non ne esista già un duplicato nella
        # lista, la aggiunge
        if (title, summary, url) not in elenco:
            elenco.append((title, summary, url))

    return elenco

# ------------------------------------------------------------
    
def stampa_feed(feed, elementi):
    """
    Formatta il feed restituendo una stringa
    """
    
    # Ottiene dal sistema il numero di righe e colonne
    # visualizzabili sullo schermo
    righe, colonne = os.popen('stty size', 'r').read().split()

    # In base al numero di righe e colonne visualizzabili,
    # prepara la spaziatura per scrivere titolo e corpo 
    # dell'articolo
    wrapper = textwrap.TextWrapper(width=int(colonne)-1,
                                initial_indent="",
                                subsequent_indent="")
    wrapper_titolo = textwrap.TextWrapper(width=int(colonne)-5,
                                initial_indent="",
                                subsequent_indent=" "*4)
    wrapper_corpo = textwrap.TextWrapper(width=int(colonne)-5, 
                                initial_indent=" "*4, 
                                subsequent_indent=" "*4)

    # Prepara gli articoli formattandoli in una stringa
    out_list = []
    for indice, post in enumerate(feed[:elementi]):
        out = "{}. {}".format(
            str(indice+1).rjust(2), 
            post[0])

        out_list += wrapper_titolo.wrap(out)

        out = "{}\n{}\n{}".format(
        "-"*(int(colonne)-9),
        post[1],
        "="*(int(colonne)-9))

        out_list += wrapper_corpo.wrap(out)
        
        # Se non è l'ultimo articolo,
        # va a capo di un'altra riga
        if indice < (len(feed[:elementi]) - 1):
            out += "\n"

        out_list += [""]
    
    conto = 0
    for riga in out_list:
        print(riga)
        conto = conto + 1
        if conto >= (int(righe)-1):
            scelta = input("(MORE..) ")
            if scelta.lower() in ["n", "no", "q", "quit", "exit"]:
                quit()
            conto = 0

# ------------------------------------------------------------
