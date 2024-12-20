import unittest
from unittest.mock import patch, Mock
from datetime import datetime

from . import ChessDotCom

class TestChessDotComService(unittest.TestCase):

    def setUp(self):
        self.service = ChessDotCom.ChessDotComService()
        self.username = "cmess4401"
        self.date = datetime(2024, 12, 20)

    @patch('requests.get')
    def test_get_player_stats(self, mock_get):
        mock_response = Mock()
        expected_data = {"chess_blitz": {"last": {"rating": 1200}}}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_player_stats(self.username)
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(f"https://api.chess.com/pub/player/{self.username}/stats", headers=self.service.headers)

    @patch('requests.get')
    def test_get_player_current_games(self, mock_get):
        mock_response = Mock()
        expected_data = {"games": []}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_player_current_games(self.username)
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(f"https://api.chess.com/pub/player/{self.username}/games", headers=self.service.headers)

    @patch('requests.get')
    def test_get_player_game_by_id(self, mock_get):
        game_id = "12345"
        mock_response = Mock()
        expected_data = {"game": {"id": game_id}}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_player_game_by_id(self.username, game_id)
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(f"https://api.chess.com/pub/player/{self.username}/game/{game_id}", headers=self.service.headers)

    @patch('requests.get')
    def test_get_player_archives_games(self, mock_get):
        mock_response = Mock()
        expected_data = {"games": []}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_player_archives_games(self.username, self.date)
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(f"https://api.chess.com/pub/player/{self.username}/games/{self.date.year}/{self.date.month}", headers=self.service.headers)

    @patch('requests.get')
    def test_get_user_pgns(self, mock_get):
        mock_response = Mock()
        expected_data = "PGN data"
        mock_response.text = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_user_pgns(self.username, self.date)
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(f"https://api.chess.com/pub/player/{self.username}/games/{self.date.year}/{self.date.month}/pgn", headers=self.service.headers)

if __name__ == '__main__':
    unittest.main()