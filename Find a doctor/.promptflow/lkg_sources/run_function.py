from promptflow import tool
import json
import requests
from bs4 import BeautifulSoup
import urllib.parse

def extract_json_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        doc = BeautifulSoup(response.text, "html.parser")

        doctor_list = []
        # Find the doctor profile section
        doctor_profiles = doc.find_all('div', class_='search-results-resultslist-doctor-profile')
        for doctor_profile in doctor_profiles:
            # Extract the doctor's name
            doctor_name = doctor_profile.find('h2', class_='search-results-resultslist-doctor-profile-name').get_text(strip=True)
            details_section = doc.find('div', class_='search-results-resultslist-doctor-data')
            specialty = details_section.find('li', class_='search-results-resultslist-doctor-data-info-specialty').get_text(strip=True)
            location = details_section.find('li', class_='search-results-resultslist-doctor-data-info-location').get_text(strip=True)
            #relationship = details_section.find('li', class_='search-results-resultslist-doctor-data-info-relationship').get_text(strip=True)

            hrefs = [a['href'] for a in doctor_profile.find_all('a', href=True)]
            doctor_data = {
                    'name': doctor_name,
                    'specialty': specialty,
                    'location': location.strip(),
                  #  'relationship': relationship,
                    'links': hrefs 
                }
            doctor_list.append(doctor_data)

        return doctor_list

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")
        return None




def find_a_doctor(query: str,category: str="Speciality",zip:str ='30097',  sort: str = "BestMatch"):
    url = "https://www.uhhospitals.org/api/doctors/ResultsList?sc_itemid=%7b5F8EE540-805E-46BA-856B-94B4272C8B6B%7d&sc_database=web&sc_site=uhhospitals&q=skin%20doctor&latitude=41.506581&longitude=-81.604962&page=1&sort=Closest&zip=30097"
    params ={ 
    "q":query,
    "zip":zip,
    "sort": sort,
    "page":1,
    "sc_database":"web",
    "sc_itemid":"{5F8EE540-805E-46BA-856B-94B4272C8B6B}",
    "category":category
         }


    try:
                # Parse the base URL and update the query parameters
        url_parts = list(urllib.parse.urlparse(url))
        query = urllib.parse.parse_qs(url_parts[4])  # Existing query parameters

        # Add new parameters
        query.update(params)

        # Rebuild query string
        url_parts[4] = urllib.parse.urlencode(query, doseq=True)

        # Construct the full URL
        full_url = urllib.parse.urlunparse(url_parts)
        print(full_url)
        data = extract_json_from_url(full_url)
        return data
    except requests.RequestException as e:
        return f"An error occurred: {str(e)}"


@tool
def run_function(response_message: dict) -> str:
    function_call = response_message.get("function_call", None)
    if function_call and "name" in function_call and "arguments" in function_call:
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        print(function_args)
        result = globals()[function_name](**function_args)
    else:
        print("No function call")
        if isinstance(response_message, dict):
            result = response_message.get("content", "")
        else:
            result = response_message
    return result
