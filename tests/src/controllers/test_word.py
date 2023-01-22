from src.controllers.words import ControllerWords
from src.exceptions import ErrorNotListValid
from tests import BaseTestClass


class TestControllerWords(BaseTestClass):

    @property
    def _controller(self):
        return ControllerWords()

    def test_expected_success__wowels_count(self):
        list_words = ["batman", "robin", "coringa"]
        result = self._controller.wowels_count(list_words)
        self.assertEqual(result["batman"], 2)
        self.assertEqual(result["robin"], 2)
        self.assertEqual(result["coringa"], 3)

    def test_expected_error__wowels_count(self):
        list_words = "word"
        with self.assertRaises(ErrorNotListValid):
            self._controller.wowels_count(list_words)

    def test_expected_success_with_asc_sort_list(self):
        list_words = ["robin", "batman", "coringa"]
        order = "asc"
        result = self._controller.sort_list(list_words, order)

        self.assertEqual(result[0], "batman")
        self.assertEqual(result[1], "coringa")
        self.assertEqual(result[2], "robin")

    def test_expected_success_with_desc_sort_list(self):
        list_words = ["coringa", "batman", "robin"]
        order = "desc"
        result = self._controller.sort_list(list_words, order)

        self.assertEqual(result[0], "robin")
        self.assertEqual(result[1], "coringa")
        self.assertEqual(result[2], "batman")
