import unittest
from repositories.scorerepository import score_repository


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()
        self._name = 'TEST'
        self._name2 = 'tester'
        self.score_1 = 10
        self.score_2 = 150
        self.score_3 = 25
        self.score_4 = 99

    def test_add_score_to_db(self):
        score_repository.add_score_to_db(self._name, self.score_1)
        scores = score_repository.get_top_five()

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0][0], 'TEST')
        self.assertEqual(scores[0][1], 10)

    def test_get_top_five(self):
        score_repository.add_score_to_db(self._name, self.score_1)
        score_repository.add_score_to_db(self._name, self.score_2)
        score_repository.add_score_to_db(self._name2, self.score_3)
        score_repository.add_score_to_db(self._name2, self.score_4)

        scores = score_repository.get_top_five()
        self.assertEqual(len(scores), 4)

        self.assertEqual(scores[0][0], 'TEST')
        self.assertEqual(scores[0][1], 150)
        self.assertEqual(scores[3][0], 'TEST')
        self.assertEqual(scores[3][1], 10)

    def test_delete_all(self):
        score_repository.add_score_to_db(self._name, self.score_1)
        score_repository.delete_all()
        scores = score_repository.get_top_five()
        self.assertEqual(len(scores), 0)
