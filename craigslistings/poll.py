if __name__ == '__main__':
    import psycopg2
    import requests
    import feedparser
    import logging
    import time
    import dateutil.parser

    logging.basicConfig(level=logging.INFO)

    try:
        from raven import Client
        from .sentry import DSN
        client = Client(DSN)
    except ImportError:
        pass
    
    con = psycopg2.connect(database="neighborhood")
    c = con.cursor()

    while True:
        c.execute("SELECT rss_id, raw, city, section FROM rss")
        for rss_id, rss, city, section in c:
            feed = feedparser.parse(rss)
            logging.info("rss id: %s", rss_id)
            for entry in feed.entries :
                c.execute("SELECT * FROM listing WHERE url = %s",
                          (entry.id, ))
                if c.fetchone() is None:
                    try:
                        result = requests.get(entry.id, timeout=60)
                        c.execute("INSERT INTO listing VALUES (%s, %s, %s, %s, %s)",
                                  (entry.id, result.text, entry.updated, city, section))
                    except:
                        client.captureException()
                        raise
                else:
                    c.execute("SELECT updated FROM listing WHERE url = %s",
                              (entry.id, ))
                    last_updated = c.fetchone()[0]
                    updated = dateutil.parser.parse(entry.updated)

                    if updated > last_updated :
                        try:
                            result = requests.get(entry.id, timeout=60)
                            c.execute("UPDATE listing "
                                      "SET html = %s, "
                                      "    updated = %s "
                                      "WHERE url = %s",
                                      (result.text, entry.updated, entry.id))
                        except:
                            client.captureException()
                            raise
                        
                        

            c.execute("DELETE from rss WHERE rss_id = %s",
                      (rss_id, ))
            con.commit()
        logging.info('waiting')
        time.sleep(600)
