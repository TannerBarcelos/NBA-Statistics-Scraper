from soup import Soup

# Gets the team names and links to those teams
def get_base_links():

    # store the team name and link as key-val pairs
    teamMap = {}

    # root beautifulsoup object
    soup = Soup()

    # pull out the table of teams
    table = soup.getData().find('table', id='teams_active')

    # get the tables body [the <tr>'s, and their data]
    tableBody = table.find('tbody')

    # get just the table rows of the team links
    tableRowData = tableBody.find_all('tr', class_='full_table')

    # get the link to each team long-term data
    for el in tableRowData:
        element = el.find('a')
        link = f'{soup.getURL()[:len(element) - 8]}{element["href"]}'
        teamName = element.text
        teamMap[teamName] = link

    return teamMap

# gets the specific HTML page for every team on basketball-reference with a n-season summary
def getTeamPageSummary(teamsMap):
    pagesForTeams = []
    for name, link in teamsMap.items():
        print(f'{name} : {link}')
        base = Soup(link).getData()
        pagesForTeams.append(base)
    return pagesForTeams

teamMap = get_base_links()

getTeamPageSummary(teamMap)