import click
from feedreader import analizza_feed
from feedreader import stampa_feed

# Prepara la lista di URL conosciute per cui basta solo indicare
# il nome della chiave (Es: altroconsumo.it => https://www.altroconsumo.it/rss)
canali = dict()
canali["altroconsumo.it"] = "https://www.altroconsumo.it/rss"
canali["ilfattoquotidiano.it"] = "https://www.ilfattoquotidiano.it/feed/"
canali["it.ign.com"] = "https://it.ign.com/feed.xml"
canali["corriere.it"] = "http://xml2.corriereobjects.it/rss/homepage.xml"
canali["gazzetta.it"] = "https://www.gazzetta.it/rss/home.xml"
canali["repubblica.it"] = "http://www.repubblica.it/rss/homepage/rss2.0.xml"
canali["wired.com"] = "https://www.wired.com/feed"
canali["wired.it"] = "https://www.wired.it/feed/"
canali["kodi.tv"] = "http://feeds.kodi.tv/xbmc"
canali["libreelec.tv"] = "https://libreelec.tv/feed/"


@click.command()
@click.option("--limit", "-l", default=3, help='Numero massimo di elementi da visualizzare')
@click.argument('url', nargs=1, default="https://www.altroconsumo.it/rss")
def main(limit, url):
    if url in canali:
        url = canali[url]
    elenco = analizza_feed(url=url)
    print()
    stampa_feed(elenco, elementi=limit)

if __name__ == "__main__":
    main()