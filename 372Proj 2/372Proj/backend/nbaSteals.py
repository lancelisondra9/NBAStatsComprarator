from bs4 import BeautifulSoup
import requests
from csv import writer

# Base URL for the stats website
base_url = "https://www.cbssports.com/nba/stats/player/steals/nba/regular/all-pos/qualifiers/"
page_number = 1  # Start from page 1
idCounter = 1

# Open the CSV file once outside the loop
with open('nba-Steals.csv', 'w', encoding='utf8', newline='') as f:
    pWriter = writer(f)
    webHeader = ['ID', 'PlayerName', 'GamesPlayed', 'GamesStarted', 'TotalSteals', 'StealsPerGame']
    pWriter.writerow(webHeader)

    while True:
        # Generate the link for the current page
        link = f"{base_url}?page={page_number}"
        result = requests.get(link)
        doc = BeautifulSoup(result.content, "html.parser")
        tbody = doc.find("tbody")
        
        # If there's no tbody, stop the loop
        if not tbody:
            break

        trs = tbody.find_all("tr")

        for tr in trs:
            tds = tr.find_all("td")
            if tds:
                # Extract data from each row
                playerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
                gamesPlayed = tds[1].get_text(strip=True)
                gamesStarted = tds[2].get_text(strip=True)
                totalSteals = tds[3].get_text(strip=True)
                stealsPerGame = tds[4].get_text(strip=True)

                # Write data to CSV file
                pWriter.writerow([idCounter, playerName, gamesPlayed, gamesStarted, totalSteals, stealsPerGame])

                # Increment ID counter for each player
                idCounter += 1

        # Go to the next page
        page_number += 1
