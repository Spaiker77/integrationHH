import pytest
from unittest.mock import Mock, patch
from src.hh import HH


def test_hh_initialization():
    mock_saver = Mock()
    hh = HH(mock_saver)


@patch("requests.get")
def test_load_vacancies(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"items": [{"id": "1", "name": "Test"}]}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    mock_saver = Mock()
    hh = HH(mock_saver)
    hh.load_vacancies("Python")

    assert len(hh.vacancies) > 0
    mock_saver.save_to_file.assert_called_once_with(hh.vacancies)
