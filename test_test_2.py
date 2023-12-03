"""Test file for test_2.py."""

import pytest

from test_2 import extract_relevant_data, filter_courts_by_type_and_proximity

def test_extract_relevant_data_works():
    """Testing only the relevant data is extracted and returned as a dictionary."""
    data  = [
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],

        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    }
    ]
    assert extract_relevant_data(
        data) == [{"name": "Central London Employment Tribunal",
                   "dx_number": "141420 Bloomsbury 7",
                   "distance": 1.29,
                   "types": ["Tribunal"]}]


def test_extract_relevant_data_for_invalid_dx_number():
    """Testing the dx_number is changes from none to 'not available'."""
    data = [
        {
            "name": "Central London Employment Tribunal",
            "lat": 51.5158158439741,
            "lon": -0.118745425821452,
            "types": [
                    "Tribunal"
            ],
            "address": {
                "address_lines": [
                    "Victory House",
                    "30-34 Kingsway"
                ],
            },
            "areas_of_law": [
                {
                    "name": "Employment"
                }
            ],

            "dx_number": None,
            "distance": 1.29
        }
    ]
    assert extract_relevant_data(
        data) == [{"name": "Central London Employment Tribunal",
                   "dx_number": "Not Available",
                   "distance": 1.29,
                   "types": ["Tribunal"]}]


def test_filter_court_by_type_works():
    """Testing the filter function works and only returns the first court with a matching type."""
    data = [
        {
            "name": "Central London Employment Tribunal",

            "types": [
                    "Tribunal"
            ],

            "dx_number": "141420 Bloomsbury 7",
            "distance": 1.29
        },
        {
            "name": "Another Court",

            "types": [
                    "Family"
            ],

            "dx_number": "141420 Bloomsbury 7",
            "distance": 1.5
        },
        {
            "name": "Another Another Court",

            "types": [
                    "Crown Court",
                     "Tribunal"
            ],

            "dx_number":"AAC 123",
            "distance": 1.9
        }
    ]
    assert filter_courts_by_type_and_proximity(data, "Crown Court") == {
        "name": "Another Another Court", "dx_number": "AAC 123", "distance": 1.9,  "types": [
            "Crown Court",
            "Tribunal"
        ]}


def test_filter_courts_by_type_none_relevant():
    """Testing the filter function raises a Value Error when no relevant court types
    are found nearby (within the 10 provided by the API.)."""
    with pytest.raises(ValueError):
        data = [
            {
                "name": "Central London Employment Tribunal",

                "types": [
                        "Tribunal"
                ],

                "dx_number": "141420 Bloomsbury 7",
                "distance": 1.29
            },
            {
                "name": "Another Court",

                "types": [
                        "Family"
                ],

                "dx_number": "141420 Bloomsbury 7",
                "distance": 1.5
            },
            {
                "name": "Another Another Court",

                "types": [
                        "Crown Court",
                        "Tribunal"
                ],

                "dx_number":"AAC 123",
                "distance": 1.9
            }
        ]
        courts = filter_courts_by_type_and_proximity(data, "Random Type")
        assert courts == "No relevant courts found nearby."
