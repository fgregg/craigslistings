include config.mk

define check_relation
 psql -d $(PG_DB) -c "\d $@" > /dev/null 2>&1 ||
endef

rss:
	$(check_relation) psql -d $(PG_DB) -c \
		"CREATE TABLE $@ (rss_id SERIAL PRIMARY KEY, \
				  section TEXT, \
				  url TEXT, \
				  added TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
				  raw TEXT, \
				  city TEXT, \
                                  processed BOOLEAN DEFAULT FALSE)"

listing:
	$(check_relation) psql -d $(PG_db) -c \
		"CREATE TABLE $@ (url TEXT, html TEXT)"

ocd_ctrl_socket :
	ssh -M -S $@ -fnNT -L $(PG_PORT):$(PG_HOST):5432 ubuntu@ocd.datamade.us

.PHONY : clean
clean : ocd_ctrl_socket
	ssh -S $^ -O exit ubuntu@ocd.datamade.us

.PHONY : interactive
interactive : ocd_ctrl_socket
	psql -h $(PG_HOST) -p $(PG_PORT) -d $(PG_DB) -U $(PG_USER)
	ssh -S $^ -O exit ubuntu@ocd.datamade.us
