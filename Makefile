PG_DB=neighborhood
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
				  city TEXT)"
