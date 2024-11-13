from bs4 import BeautifulSoup
import requests
from csv import writer

# Base URL for stats website
base_url = "https://www.cbssports.com/nba/stats/player/rebounds/nba/regular/all-pos/qualifiers/"
page_number = 1  # Start from page 1

idCounter = 1

with open('nba-Rebounds.csv', 'w', encoding='utf8', newline='') as f:
    pWriter = writer(f)
    webHeader = ['ID', 'PlayerName', 'GamesPlayed', 'GamesStarted', 'MinutesPerGame', 'OffensiveRebounds', 'DeffensiveRebounds', 'TotalRebounds', 'ReboundsPerGame']
    pWriter.writerow(webHeader)

    # Loop through pages until there's no data left
    while True:
        # Generate the link for the current page
        link = f"{base_url}?page={page_number}"
        result = requests.get(link)
        
        doc = BeautifulSoup(result.content, "html.parser")
        tbody = doc.find("tbody")
        
        if not tbody:
            break
        
        trs = tbody.find_all("tr")

        for tr in trs:
            tds = tr.find_all("td")
            if tds:
                PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
                GamesPlayed = tds[1].get_text(strip=True)
                GamesStarted = tds[2].get_text(strip=True)
                MinutesPerGame = tds[3].get_text(strip=True)
                OffensiveRebounds = tds[4].get_text(strip=True)
                DeffensiveRebounds = tds[5].get_text(strip=True)
                TotalRebounds = tds[6].get_text(strip=True)
                ReboundsPerGame = tds[7].get_text(strip=True)

                # Write data to CSV
                pWriter.writerow([idCounter, PlayerName, GamesPlayed, GamesStarted, MinutesPerGame, OffensiveRebounds, DeffensiveRebounds, TotalRebounds, ReboundsPerGame])
                
                # Increment ID counter for each player
                idCounter += 1

        # Go to the next page
        page_number += 1
