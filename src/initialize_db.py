from db_connection import get_db_connection


def drop_tables(connection):
    """Poistaa tietokantataulut.

    Args:
        connection: Connection-olio
    """
    cursor = connection.cursor()

    cursor.execute('''
        DRROP TABLE IF EXISTS Scores;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.

    Args:
        connection: Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Scores (id INTEGER PRIMARY KEY, user TEXT, score INT
        );
    ''')

    connection.commit()


def initialize_db():
    """Alustaa tietokantataulut.
    """

    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_db()
