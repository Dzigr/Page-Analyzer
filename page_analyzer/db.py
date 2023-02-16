"""Module for working with database."""

import os
from contextlib import contextmanager

import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


@contextmanager
def get_connection():
    """Connect with database generator.

    Yields:
        connection with database
    """
    connection = None
    try:
        connection = psycopg2.connect(DATABASE_URL)
        yield connection
    finally:
        if connection:
            connection.close()
