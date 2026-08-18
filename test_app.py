"""Regression tests for Flask prediction inputs."""

import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, mock_open, patch


APP_PATH = Path(__file__).with_name("app.py")


def load_app():
    """Load app.py without deserializing production model objects."""
    for dependency in ("flask", "pandas", "matplotlib.pyplot", "nltk"):
        importlib.import_module(dependency)
    module_name = "sentiment_app_under_test"
    spec = importlib.util.spec_from_file_location(module_name, APP_PATH)
    module = importlib.util.module_from_spec(spec)
    opened = mock_open(read_data=b"model")
    with (
        patch("builtins.open", opened),
        patch("pickle.load", side_effect=[Mock(), Mock()]),
        patch("nltk.corpus.stopwords.words", return_value=[]),
    ):
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
    return module, opened


class PredictionInputTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module, cls.opened = load_app()
        cls.client = cls.module.app.test_client()

    def setUp(self):
        self.predict = patch.object(
            self.module,
            "predict_sentiment",
            return_value="Positive",
        )
        self.predict_mock = self.predict.start()

    def tearDown(self):
        self.predict.stop()

    def test_models_resolve_from_app_directory(self):
        model_dir = APP_PATH.parent / "Models"
        model_names = {"xgboost_model.pkl", "tfidfVectorizer.pkl"}
        opened_paths = [
            Path(call.args[0])
            for call in self.opened.call_args_list
            if Path(call.args[0]).name in model_names
        ]
        self.assertEqual(
            opened_paths,
            [model_dir / "xgboost_model.pkl", model_dir / "tfidfVectorizer.pkl"],
        )

    def test_valid_json_text_returns_prediction(self):
        response = self.client.post("/predict", json={"text": "  works well  "})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": "Positive"})
        self.predict_mock.assert_called_once_with("  works well  ")

    def test_missing_or_malformed_json_returns_400(self):
        cases = (
            {},
            [],
            42,
            {"other": "value"},
            {"text": None},
            {"text": 42},
            {"text": "   "},
        )
        for payload in cases:
            with self.subTest(payload=payload):
                response = self.client.post("/predict", json=payload)
                self.assertEqual(response.status_code, 400)
                self.assertEqual(
                    response.get_json(),
                    {"error": "Text or CSV file required"},
                )
        malformed = self.client.post(
            "/predict",
            data="{",
            content_type="application/json",
        )
        self.assertEqual(malformed.status_code, 400)
        self.predict_mock.assert_not_called()

    def test_non_json_request_returns_400(self):
        response = self.client.post("/predict", data="text=hello")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {"error": "Text or CSV file required"},
        )
        self.predict_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
