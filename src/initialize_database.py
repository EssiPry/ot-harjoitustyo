from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulun.

    Args:
        connection: Connection-olio
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Scores;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo uuden tietokantataulun.

    Args:
        connection: Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Scores (id INTEGER PRIMARY KEY, player TEXT, score INT
        );
    ''')

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut.
    """

    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
