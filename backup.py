import pandas as pd
import mysql.connector
import os
from mysql.connector import errorcode
from datetime import datetime

import config_example


file_name = f'backup_{datetime.now()}.csv'


def establish_connection():
    return mysql.connector.connect(
        host=config_example.host,
        user=config_example.user,
        password=config_example.password,
    )


def main(path_to_file = "./"):
    try:
        connection = establish_connection()
        df = pd.read_sql('select * from db_django.app_solutions', con=connection)
        path = os.join(path_to_file, file_name)
        df.to_csv(path)
        print(f'Saved backup to {path}')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    except:
        print("Unknown error")
    finally:
        connection.close()


if __name__ == '__main__':
    main()
