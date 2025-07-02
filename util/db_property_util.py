# Database Connectivity - Task 11
import configparser
import os


class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file_name):
        try:
            config = configparser.ConfigParser()

            # Get the absolute path to the property file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            property_file_path = os.path.join(current_dir, "..", "config", property_file_name)

            config.read(property_file_path)

            if 'database' not in config:
                raise ValueError("Invalid property file format. Missing 'database' section.")

            db_config = config['database']
            required_keys = ['host', 'database', 'user', 'password']

            if not all(key in db_config for key in required_keys):
                raise ValueError("Missing required database configuration keys.")

            connection_string = (
                f"host={db_config['host']} "
                f"dbname={db_config['database']} "
                f"user={db_config['user']} "
                f"password={db_config['password']}"
            )

            if 'port' in db_config:
                connection_string += f" port={db_config['port']}"

            return connection_string
        except Exception as e:
            print(f"Error reading property file: {e}")
            raise