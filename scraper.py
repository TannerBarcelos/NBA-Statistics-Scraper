from soup import CreateSoup
import json

# Gets the team names and links to those teams
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

# gets the specific HTML page for every team on basketball-reference with an n-season summary
def get_team_page(teamsMap) -> []:
    
    pagesForTeams = []
    
    for name, link in teamsMap.items():
        page = CreateSoup(link)
        pageData = page.process_request()
        pagesForTeams.append({
            'name': name,
            'pageData': pageData
        })
    
    return pagesForTeams

def process_team_page(teams) -> {}:

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
            seasonStatsLink = f'https://www.basketball-reference.com{seasonAnchor["href"]}'
            teamSeasons[teamName].append({'date': seasonDate, 'link': seasonStatsLink})

    return teamSeasons

# main method
def main() -> None:
    teams = get_base_links()
    teamPages = get_team_page(teams)
    teamSeasonDictionary = process_team_page(teamPages)
main()