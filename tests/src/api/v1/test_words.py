import mock

from tests import BaseTestClass


class WordsCountVowels(BaseTestClass):

    def test_expected_success_post(self):
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post("/vowel_count", json=body)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        result_json = response.json
        self.assertEqual(result_json["batman"], 2)
        self.assertEqual(result_json["coringa"], 3)
        self.assertEqual(result_json["robin"], 2)

    def test_expected_error_400_post(self):
        body = {}
        response = self._app.post("/vowel_count", json=body)
        self.assertEqual(response.status_code, 400)

    def test_expected_error_22_post(self):
        body = {"teste": "eresre"}
        response = self._app.post("/vowel_count", json=body)
        self.assertEqual(response.status_code, 422)
        self.assertIsInstance(response.json, dict)

    def test_expected_error_form_data_success_post(self):
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post("/vowel_count", data=body)
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)

    def test_expected_422_to_words_error_post(self):
        body = {"words": [134]}
        response = self._app.post("/vowel_count", json=body)
        self.assertEqual(response.status_code, 422)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_expected_error_500_post(self, mock_controller):
        mock_controller().wowels_count.side_effect = Exception("Error inespected!")
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post("/vowel_count", json=body)
        self.assertEqual(response.status_code, 500)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_put(self, mock_controller):
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.put("/vowel_count", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_get(self, mock_controller):
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.get("/vowel_count", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_patch(self, mock_controller):
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.patch("/vowel_count", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_delete(self, mock_controller):
        body = {"words": ["batman", "robin", "coringa"]}
        response = self._app.delete("/vowel_count", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)


class TestWordsSort(BaseTestClass):

    def test_expected_succes_sort_list(self):
        body = {"words": ["coringa", "batman", "robin"],
                "order": "asc"}
        response = self._app.post("/sort", json=body)
        result = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result[0], "batman")
        self.assertEqual(result[1], "coringa")
        self.assertEqual(result[2], "robin")

    def test_expected_error_order_invalid_list(self):
        body = {"words": ["coringa", "batman", "robin"],
                "order": "test"}
        response = self._app.post("/sort", json=body)
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_put(self, mock_controller):
        body = {"words": ["coringa", "batman", "robin"],
                "order": "asc"}
        response = self._app.put("/sort", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_get(self, mock_controller):
        body = {"words": ["coringa", "batman", "robin"],
                "order": "asc"}
        response = self._app.get("/sort", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_patch(self, mock_controller):
        body = {"words": ["coringa", "batman", "robin"],
                "order": "asc"}
        response = self._app.patch("/sort", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)

    @mock.patch("src.api.v1.words.ControllerWords")
    def test_method_not_allowed_delete(self, mock_controller):
        body = {"words": ["coringa", "batman", "robin"],
                "order": "asc"}
        response = self._app.delete("/sort", json=body)
        self.assertEqual(response.status_code, 405)
        self.assertIsInstance(response.json, dict)
