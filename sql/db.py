import psycopg2
from settings.settings import host, user, password, db_name
from log_conf.log import BasicLog

b_log = BasicLog()
log = b_log.log_config()


class DataBase:
    def __init__(self):
        self.conection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.conection.autocommit = True

    def add_users_data(self, first_name, last_name, date):
        with self.conection.cursor() as curs:
            try:
                curs.execute(
                    f"""INSERT INTO users_data (first_name, last_name, date_of_birth) 
                    VALUES ('{first_name}', '{last_name}', '{date}');"""
                )
            except Exception as ex:
                print(f'not work: {ex}')
                log.info(ex)

        self.conection.close()
        print('Connection close')
        return self

    # def add_table(self):
    #     with self.conection.cursor() as curs:
    #         curs.execute(
    #                 '''CREATE TABLE users_data (
    #                 id serial PRIMARY KEY,
    #                 first_name VARCHAR (50) NOT NULL,
    #                 last_name VARCHAR (50) NOT NULL,
    #                 date_of_birth date);'''
    #             )
    #
    #     self.conection.close()
    #     print('Connection close')

# postgre = DataBase()
# postgre.add_users_data('Ira', 'Mospan', datetime.date(1993, 6, 22 ))
