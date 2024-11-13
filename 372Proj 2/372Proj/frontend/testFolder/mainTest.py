import unittest
from unittest.mock import patch, mock_open, Mock
from ..main import PlayerStatsApp

class TestPlayerStatsApp(unittest.TestCase):

    def setUp(self):
        # Mock the root to avoid Tkinter dependency
        self.app = PlayerStatsApp(root=Mock())

    @patch("builtins.open", new_callable=mock_open, read_data="ID,PlayerName,GamesPlayed,GamesStarted,TotalSteals,StealsPerGame\n1,S. Curry,10,10,20,2.0\n")
    def test_read_csv_data_steals_valid_player(self, mock_file):
        # Test valid player data retrieval in "Steals" category
        data = self.app.read_csv_data("nba-Steals.csv", "S. Curry", "Steals")
        self.assertEqual(data["PlayerName"][0], "S. Curry")
        self.assertEqual(int(data["GamesPlayed"][0]), 10)
        self.assertEqual(float(data["StealsPerGame"][0]), 2.0)

    @patch("builtins.open", new_callable=mock_open, read_data="ID,PlayerName,GamesPlayed,GamesStarted,TotalSteals,StealsPerGame\n1,J. Doe,10,10,10,1.0\n")
    def test_read_csv_data_steals_nonexistent_player(self, mock_file):
        # Test handling of non-existent player in "Steals" category
        data = self.app.read_csv_data("nba-Steals.csv", "S. Curry", "Steals")
        self.assertEqual(data["PlayerName"], [])  # Should return empty list

    @patch("builtins.open", new_callable=mock_open, read_data="ID,Name,GamesPlayed,GamesStarted,MinutesPerGame,PointsPerGame,FieldGoalsMade\n1,S. Curry,10,10,34,30.0,100\n")
    def test_read_csv_data_scores_valid_player(self, mock_file):
        # Test valid player data retrieval in "Scores" category
        data = self.app.read_csv_data("nba-Scores.csv", "S. Curry", "Scores")
        self.assertEqual(data["Name"][0], "S. Curry")
        self.assertEqual(float(data["PointsPerGame"][0]), 30.0)

    @patch("builtins.open", new_callable=mock_open, read_data="ID,PlayerName,GamesPlayed,GamesStarted,MinutesPerGame,TotalRebounds,ReboundsPerGame\n1,S. Curry,10,10,34,50,5.0\n")
    def test_read_csv_data_rebounds_valid_player(self, mock_file):
        # Test valid player data retrieval in "Rebounds" category
        data = self.app.read_csv_data("nba-Rebounds.csv", "S. Curry", "Rebounds")
        self.assertEqual(data["PlayerName"][0], "S. Curry")
        self.assertEqual(float(data["ReboundsPerGame"][0]), 5.0)

    @patch("builtins.open", new_callable=mock_open)
    def test_read_csv_data_missing_file(self, mock_file):
        # Test handling of missing CSV file
        mock_file.side_effect = FileNotFoundError
        data = self.app.read_csv_data("nba-Nonexistent.csv", "S. Curry", "Steals")
        self.assertEqual(data, {})  # Should return empty dictionary

    @patch("builtins.open", new_callable=mock_open, read_data="ID,PlayerName,GamesPlayed\n1,S. Curry,10\n")
    def test_read_csv_data_missing_columns(self, mock_file):
        # Test handling of missing columns in CSV file
        data = self.app.read_csv_data("nba-Steals.csv", "S. Curry", "Steals")
        self.assertEqual(data.get("TotalSteals", []), [])
        self.assertEqual(data.get("StealsPerGame", []), [])

    @patch("builtins.open", new_callable=mock_open, read_data="ID,PlayerName,GamesPlayed,GamesStarted,TotalSteals,StealsPerGame\n1,S. Curry,10,notanumber,20,2.0\n")
    def test_read_csv_data_invalid_data_type(self, mock_file):
        # Test handling of invalid data types in CSV
        with self.assertRaises(ValueError):
            self.app.read_csv_data("nba-Steals.csv", "S. Curry", "Steals")

if __name__ == "__main__":
    unittest.main()
