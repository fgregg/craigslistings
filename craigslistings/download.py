import requests
import logging

def save_rss(feed, city, cursor):        
    section, url = feed 
    url = url % city

    logging.info('%s', city)
    logging.info('%s', section)
    logging.info('%s', url)

    listing = requests.get(url).text

    cursor.execute("""INSERT INTO rss (section, url, raw, city) """
                   """VALUES (%s, %s, %s, %s) """
                   """RETURNING rss_id""",
                   (section, url, listing, city))


if __name__ == '__main__':
    import psycopg2
    import urllib.error
    import time

    try:
        from raven import Client
        from .sentry import DSN
        client = Client(DSN)
    except ImportError:
        pass

    from . import config

    logging.basicConfig(level=logging.INFO)
    
    db = psycopg2.connect(database="neighborhood")
    c = db.cursor()

    for city in config.cities :
        if city == "newyork" :
            feeds = config.ny_feeds
        else :
            feeds = config.std_feeds
        for feed in feeds:
            try:
                save_rss(feed, city, c)
            except requests.HTTPError as e:
                logging.info(e)
                logging.info(url)
            except:
                client.captureException()
                raise

            db.commit()
            time.sleep(1)

    c.close()
    db.close()

