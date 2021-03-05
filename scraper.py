from soup import Soup

# Gets the team names and links to those teams
def get_base_links() -> {}:
    teamMap = {}
    
    soup = Soup()
    
    # Perform the request to the base page and find the table of team names + links and pull that out
    table = soup.getData().find('table', id='teams_active')
    tableBody = table.find('tbody')
    tableRowData = tableBody.find_all('tr', class_='full_table')

    # get the link to each team page
    for el in tableRowData:
        element = el.find('a')
        link = f'{soup.getURL()[:len(element) - 8]}{element["href"]}'
        teamName = element.text
        teamMap[teamName] = link

    return teamMap

# gets the specific HTML page for every team on basketball-reference with an n-season summary
def get_team_page(teamsMap) -> []:
    pagesForTeams = []
    for name, link in teamsMap.items():
        pagesForTeams.append(Soup(link).getData())
    return pagesForTeams

# main method
def main() -> None:
    teams = get_base_links()
    teamPages = get_team_page(teams)

    for teamPage in teamPages:
        print(teamPage)

main()