# Create Postgresql Database Function for the Database Module
def create_database(database_name):
    """
    Create a Postgresql Database
    """
    import psycopg2
    import os
    import sys

    # Connect to the default database
    conn = psycopg2.connect(
        "dbname=postgres user=postgres password=postgres")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
