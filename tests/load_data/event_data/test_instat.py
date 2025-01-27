import unittest

import pandas as pd

from databallpy.load_data.event_data.instat import (
    _load_event_data,
    _load_metadata,
    _update_metadata,
    load_instat_event_data,
)
from tests.expected_outcomes import ED_INSTAT, MD_INSTAT


class TestInstat(unittest.TestCase):
    def setUp(self):
        self.instat_metadata_loc = "tests/test_data/instat_md_test.json"
        self.instat_event_data_loc = "tests/test_data/instat_ed_test.json"

    def test_load_instat_event_data(self):
        expected_metadata = MD_INSTAT.copy()
        expected_metadata.pitch_dimensions = [100.0, 50.0]
        event_data, metadata = load_instat_event_data(
            self.instat_event_data_loc, self.instat_metadata_loc
        )
        pd.testing.assert_frame_equal(event_data, ED_INSTAT)
        assert metadata == expected_metadata

    def test_load_metadata(self):
        metadata = _load_metadata(self.instat_metadata_loc)
        expected_metadata = MD_INSTAT.copy()
        expected_metadata.home_players = pd.DataFrame(
            columns=["id", "full_name", "shirt_num"]
        )
        expected_metadata.away_players = pd.DataFrame(
            columns=["id", "full_name", "shirt_num"]
        )
        expected_metadata.home_formation = ""
        expected_metadata.away_formation = ""
        assert metadata == expected_metadata

    def test_update_metadata(self):
        input_metadata = MD_INSTAT.copy()
        input_metadata.home_players = pd.DataFrame(
            columns=["id", "full_name", "shirt_num"]
        )
        input_metadata.away_players = pd.DataFrame(
            columns=["id", "full_name", "shirt_num"]
        )
        input_metadata.home_formation = ""
        input_metadata.away_formation = ""
        expected_metadata = MD_INSTAT
        assert (
            _update_metadata(input_metadata, self.instat_event_data_loc)
            == expected_metadata
        )

    def test_load_event_data(self):
        event_data, pitch_dimensions = _load_event_data(
            self.instat_event_data_loc, MD_INSTAT
        )
        expected_event_data = ED_INSTAT
        pd.testing.assert_frame_equal(event_data, expected_event_data)
        assert pitch_dimensions == [100.0, 50.0]
