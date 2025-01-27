import unittest

import numpy as np

from databallpy.load_data.tracking_data._add_player_tracking_data_to_dict import (
    _add_player_tracking_data_to_dict,
)


class TestAddPlayerTrackingDataToDict(unittest.TestCase):
    def setUp(self):
        self.input_t0 = [
            ["0", "10", np.nan, "-100"],
            ["0", "11", "300", "60"],
            ["1", "9", "400", np.nan],
        ]

        self.input_t1 = [
            ["0", "10", "60", "100"],
            ["0", "11", "120", "-50"],
            ["1", "9", "40", "100"],
            ["1", "10", "200", "40"],
        ]

        self.expected_output = {
            "frame": [0, 1],
            "away_10_x": [np.nan, 60.0],
            "away_10_y": [-100.0, 100],
            "away_11_x": [300.0, 120.0],
            "away_11_y": [60.0, -50.0],
            "home_9_x": [400.0, 40.0],
            "home_9_y": [np.nan, 100.0],
            "home_10_x": [np.nan, 200.0],
            "home_10_y": [np.nan, 40.0],
        }

    def test_add_player_tracking_to_data_dict(self):
        data = {
            "frame": [0, 1],
            "away_10_x": [np.nan, np.nan],
            "away_10_y": [np.nan, np.nan],
            "home_9_x": [np.nan, np.nan],
            "home_9_y": [np.nan, np.nan],
        }

        for player in self.input_t0:
            team_id, shirt_num, x, y = player
            if team_id == "0":
                team = "away"
            elif team_id == "1":
                team = "home"
            else:
                continue
            data = _add_player_tracking_data_to_dict(team, shirt_num, x, y, data, 0)

        for player in self.input_t1:
            team_id, shirt_num, x, y = player
            if team_id == "0":
                team = "away"
            elif team_id == "1":
                team = "home"
            else:
                continue
            data = _add_player_tracking_data_to_dict(team, shirt_num, x, y, data, 1)

        assert data == self.expected_output
