from soup import CreateSoup
import json

# Scrapes each team and saves the team name and a link to their individual pages of stats in a dictionary and returns it
def get_base_links() -> {}:
    
    teamMap = {}
    
    # New soup instance
    soup = CreateSoup()

    # perform the HTTP request
    page = soup.process_request()
    
    # Perform the request to the base page and find the table of team names + links and pull that out
    table = page.find('table', id='teams_active')
    tableBody = table.find('tbody')
    tableRowData = tableBody.find_all('tr', class_='full_table')

    # get the link to each team page
    for el in tableRowData:
        element = el.find('a')
        link = f'{soup.get_url()[:len(element) - 8]}{element["href"]}'
        teamName = element.text
        teamMap[teamName] = link

    return teamMap

# uses the dictionary from the orriginal base url scrape to gather individual html data for every teams stats at that teams main page and returns
# an array of dictionaries containing that teams name and the html page of that team e.g: {'Atlanta Hawks': 'https://www.basketball-reference.com/teams/ATL/' }
# and this data is used to loop over and process all seasons and links to those individual season stats to get more comprehensive data
def get_team_page(teamsMap) -> []:
    
    pagesForTeams = []
    page = None
    
    for name, link in teamsMap.items():
        page = CreateSoup(link)
        pageData = page.process_request()
        pagesForTeams.append({
            'name': name,
            'pageData': pageData
        })
    
    return pagesForTeams, page

# for every processed team in the list from the above function, we want to get every single season they have existed and a link to that teams season
# stats and populate a dictionary of teams which maps to an array of ALL seasons in their history of the links for that teams season for every season ever
# e.g {'Atlanta Hawks' : [{'date' : '1995-1996', 'link': 'https://www.basketball-reference.com/teams/ATL/1996.html'}, {and so on for the other season date and link}]}
# we will then use this array to traverse over every team and get specific statistical data we would find useful for our API like the teams logo, their record, coach, points/game, etc.
# each page with these stats also has the roster during that season of players available as well. So when we run a scrape on the players for a particular season for a team
# we will need some way of relating a player to that team in the database somehow so we can always easily get individual player stats and the team they played for, etc. in their career
# when using player stat views in a frontend project
def process_team_page(teams, soupedPage) -> {}:

    teamSeasons = {}

    # teams is a list of all the teams and their corresponding html @ the link for each teams historical stats
    for team in teams:
        
        teamName = team['name']
        teamPage = team['pageData']

        # create an array for this team which will hold a list of dictionaries of the season and a link to that specific seasons stats
        teamSeasons[teamName] = []

        # find the table in the page data and get all the season rows for this team all time
        allTimeSeasonTable = teamPage.find('tbody').find_all('tr')
        
        # for this team, extract the season and the link to the stats for this team in that season
        for seasons in allTimeSeasonTable:
            seasonAnchor = seasons.select('th > a')[0]
            seasonDate = seasonAnchor.text
            seasonStatsLink = f'{soupedPage.get_url()[:len(seasonAnchor) - 12]}{seasonAnchor["href"]}'
            teamSeasons[teamName].append({'date': seasonDate, 'link': seasonStatsLink})

    return teamSeasons

# main method
def main() -> None:
    scrapedTeamsAndBaseLinks = get_base_links()
    individualTeamPages, soupedPage = get_team_page(scrapedTeamsAndBaseLinks)
    teamSeasons = process_team_page(individualTeamPages, soupedPage)

    # for now, write the data above to json
    with open('teamSeasonDump.json', 'w') as f:
        json.dump(teamSeasons, f, indent=4)

main()