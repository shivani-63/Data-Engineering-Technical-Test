"""Script to extract court data from an API and assign the closest, relevant court to a person 
given their postcode and the type of court they require. 
Script also creates a csv file with the relevant data."""

import csv
import requests

def read_csv_data() -> list[dict]:
    """Reads the .csv file for peoples data and returns a list of dictionaries."""
    peoples_data = []
    with open("people.csv", "r") as file:
        data = csv.DictReader(file)
        [peoples_data.append(row) for row in data]
    return peoples_data


def get_closest_courts_from_postcode(postcode:str) -> list[dict]:
    """Get a list of the closest airports to people using their home postcodes."""
    url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}"
    response = requests.get(url)

    if response.status_code == 404:
        raise ValueError(
            "Unable to locate nearby court information.", 404)

    if response.status_code == 500:
        raise ConnectionError("Unable to connect to server.", 500)

    if response.status_code == 200:
        json_courts = response.json()
        return json_courts


def extract_relevant_data(courts:list[dict]) -> list[dict]:
    """Extracts only the relevant information for the closest courts."""
    filtered_courts = []

    for court in courts:
        name = court["name"]
        distance = court["distance"]
        types = court["types"]
        if court["dx_number"] is None:
            dx_number = "Not Available"
        else:
            dx_number = court["dx_number"]

        relevant_information = {"name": name, "dx_number": dx_number, "distance": distance, "types": types}
        filtered_courts.append(relevant_information)
    
    return filtered_courts


def filter_courts_by_type_and_proximity(relevant_courts: list[dict], type: str) -> dict:
    """Filters the courts by type and returns the first one, as they are already arranged in order of proximity."""
    correct_type_of_court = []
    for court in relevant_courts:
        if type in court["types"]:
            correct_type_of_court.append(court)
    return correct_type_of_court[0]


def write_data_to_csv_file(compiled_data: list[dict]) -> None:
    """Writes the compiled data for each person to a csv file to access when necessary."""
    fields = ["name", "type_of_court_desired",
              "postcode", "closest_court_name", "court_dx_number", "distance_from_home_postcode"]
    
    with open('people_court_data.csv', 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(compiled_data)


if __name__ == "__main__":

    peoples_data = read_csv_data()
    compiled_people_and_court_data = []

    for person in peoples_data:
        courts = get_closest_courts_from_postcode(person["home_postcode"])
        relevant_court_data = extract_relevant_data(courts)
        closest_court = filter_courts_by_type_and_proximity(
            relevant_court_data, person['looking_for_court_type'])
        info = {"name": person["person_name"],
                "type_of_court_desired": person['looking_for_court_type'], 
                "postcode": person["home_postcode"], 
                "closest_court_name": closest_court["name"], 
                "court_dx_number": closest_court["dx_number"], 
                "distance_from_home_postcode": f"{closest_court['distance']} miles"}
        compiled_people_and_court_data.append(info)

    write_data_to_csv_file(compiled_people_and_court_data)
