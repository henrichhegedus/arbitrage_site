import psycopg2
import yaml
stream = open("config/db_config.yaml", 'r')
config = yaml.load(stream,Loader=yaml.FullLoader)
connection = psycopg2.connect(user=config["user"],
                                   password=config["password"],
                                   host=config["host"],
                                   port=config["port"],
                                   database=config["database"])
cursor = connection.cursor()

query = """
            delete from public.scrape where event_date < CURRENT_DATE; 
            delete from public.arbs where date < CURRENT_DATE;
        """

cursor.execute(query)
cursor.close()
connection.close()