from argparse import ArgumentParser
import pandas as pd
import mysql.connector
import os
from mysql.connector import errorcode
from datetime import datetime

import config


file_name = f'backup_{datetime.now()}.csv'
default_path = './'


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', required=False,
                        type=str, help='path to directory where to save backup CSV')
    args = parser.parse_args()
    if args.path is None:
        args.path = default_path
    return args.path


def establish_connection():
    return mysql.connector.connect(
        host=config.host,
        user=config.user,
        password=config.password,
    )


def main(path_to_file = default_path):
    try:
        connection = establish_connection()
        df = pd.read_sql(f'select * from {config.db_name}', con=connection)
        path = os.path.join(path_to_file, file_name)
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
    path = parse_args()
    if os.path.isdir(path):
        main(path)
    else:
        print(f'ERROR: Directory {path} not found')
