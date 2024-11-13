from bs4 import BeautifulSoup
import requests
from csv import writer

# Base URL for the assists and turnovers stats
base_url = "https://www.cbssports.com/nba/stats/player/assists-turnovers/nba/regular/all-pos/qualifiers/"
page_number = 1  # Start from the first page
idCounter = 1

# Open the CSV file once outside the loop
with open('nba-Assists', 'w', encoding='utf8', newline='') as f:
    pWriter = writer(f)
    webHeader = ['ID', 'PlayerName', 'GamesPlayed', 'GamesStarted', 'TotalAssists', 'AssistsPerGame', 
              'Turnovers', 'TurnoversPerGame', 'AssistsPerTurnover']
    pWriter.writerow(webHeader)

    while True:
        # Generate the link for the current page
        url = f"{base_url}?page={page_number}"
        result = requests.get(url)
        doc = BeautifulSoup(result.content, "html.parser")
        tbody = doc.find("tbody")
        
        # If no tbody element is found, stop the loop
        if not tbody:
            break

        trs = tbody.find_all("tr")

        for tr in trs:
            tds = tr.find_all("td")
            if tds:
                # Extract data from each row
                PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
                GamesPlayed = tds[1].get_text(strip=True)
                GamesStarted = tds[2].get_text(strip=True)
                TotalAssists = tds[3].get_text(strip=True)
                AssistsPerGame = tds[4].get_text(strip=True)
                Turnovers = tds[5].get_text(strip=True)
                TurnoversPerGame = tds[6].get_text(strip=True)
                AssistsPerTurnover = tds[7].get_text(strip=True)

                # Write data to CSV file
                pWriter.writerow([
                    idCounter, PlayerName, GamesPlayed, GamesStarted, TotalAssists, AssistsPerGame, 
                    Turnovers, TurnoversPerGame, AssistsPerTurnover
                ])

                # Increment ID counter for each player
                idCounter += 1

        # Go to the next page
        page_number += 1
