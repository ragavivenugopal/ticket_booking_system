# Database Connectivity - Task 11
import psycopg2
from util.db_property_util import DBPropertyUtil


class DBConnUtil:
    @staticmethod
    def get_connection(connection_string=None, property_file_name=None):
        try:
            if property_file_name:
                connection_string = DBPropertyUtil.get_connection_string(property_file_name)

            if not connection_string:
                raise ValueError("Either connection_string or property_file_name must be provided")

            connection = psycopg2.connect(connection_string)
            print("Database connection established successfully!")
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise