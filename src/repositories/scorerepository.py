from database_connection import get_database_connection


class ScoreRepository:
    """Tietokantaan kirjoittamisesta ja tietokannasta hakemisesta
    vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection (obj): Tietokantayhteyden Connection -olio
        """
        self._connection = connection

    def add_score_to_db(self, player, cur_score):
        """ Lisää pistemäärän tietokantaan.

        Args:
            score (int): pistemäärä
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Scores (player, score) VALUES (?, ?)", (player, cur_score))
        self._connection.commit()

    def get_top_five(self):
        """ Palauttaa viisi korkeinta pistemäärää.

        Returns:
            [lista]: [description]
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT player, score FROM Scores ORDER BY score DESC LIMIT 5")
        rows = cursor.fetchall()

        return [(row["player"], row["score"]) for row in rows]

    def delete_all(self):
        """ Poistaa kaikki pisteet tietokannasta.
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Scores")
        self._connection.commit()


score_repository = ScoreRepository(get_database_connection())
