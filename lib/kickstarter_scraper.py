# file: kickstarter_scraper.py
from bs4 import BeautifulSoup
import ipdb

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title_element = project.select("h2.bbcard_name strong a")
        title = title_element[0].text if title_element else "No Title"
        
        image_element = project.select("div.project-thumbnail a img")
        image_link = image_element[0]['src'] if image_element else "No Image"

        description_element = project.select("p.bbcard_blurb")
        description = description_element[0].text if description_element else "No Description"

        location_element = project.select("ul.project-meta span.location-name")
        location = location_element[0].text if location_element else "No Location"

        percent_funded_element = project.select("ul.project-stats li.first.funded strong")
        percent_funded = percent_funded_element[0].text.replace("%", "") if percent_funded_element else "0"

        projects[title] = {
            'image_link': image_link,
            'description': description,
            'location': location,
            'percent_funded': percent_funded
        }

    # Return the projects dictionary
    return projects
