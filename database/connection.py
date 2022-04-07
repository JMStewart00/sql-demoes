from psycopg import OperationalError, connect
from psycopg.rows import dict_row

class Connection():
    def __init__(self):
        self.connection = None

    def create_connection(self, db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
        try:
            self.connection = connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
                row_factory=dict_row
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return self.connection

    def db_interact(self, query):
        # Connect to an existing database
        with self.create_connection("postgres", "postgres", "postgres") as conn:
            with conn.cursor() as cur:
                if ('SELECT' in query):
                    # Execute the query and fetch the results
                    return cur.execute(query).fetchall()
                else:
                    # Commit the query to the database for reals
                    conn.commit()
                    