from urllib2 import urlopen
from bs4 import BeautifulSoup

# Sample regular season url: http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm
# Sample playoffs url: http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_pl.htm
sample_urls = ['http://www.landofbasketball.com/stats_by_team/2015_2016_warriors_rs.htm', 
'http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm']


def create_rs_urls_scrape(years):
    """Create list of urls to scrape for regular season stats"""

    urls = []
    for year in years:
        urls.append("http://www.landofbasketball.com/stats_by_team/{}_{}_warriors_rs.htm".format(year, year+1))

    return urls


def scrape_player_stats(urls):
    """For list of urls to scrape, use get_player_stats"""

    for url in urls:
        get_player_stats(url)


def get_player_stats(url):
    """Scrape each page for each player's avg points per game"""

    # get_player_stats('http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm')

    soup = start_scrape(url)
    tables = soup.findChildren('table')
    first_table = tables[0]
    rows = first_table.findChildren('tr')
    main_url = "http://www.landofbasketball.com/"

    for row in rows[1:]:
        player_name = row.findChildren('td')[0].text
        games_played = row.findChildren('td')[1].text
        avg_min = row.findChildren('td')[2].text
        avg_pts = row.findChildren('td')[3].text
        player_profile_link = main_url+row.find_all('a', href=True)[0].attrs['href'][3:]

        jersey = get_player_jersey(player_profile_link)

        print player_name, games_played, avg_min, avg_pts, player_profile_link, jersey #need to save these to db


def get_player_jersey(url):
    """Scrape for player jersey number"""

    soup = start_scrape(url)
    tables = soup.findChildren('table')
    first_table = tables[0]
    td_list = first_table.find_all('td')
    i = 0
    for elem in td_list:
        if elem.text=="Jersey Number:":
            ind = i
        i += 1

    jersey = td_list[ind+1].text[1:]
    # jersey = td_list[ind+1].text[1:-11]

    return jersey


# REGULAR SEASON

def start_scrape(url):
    """Scrapes url for html source"""

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup







    # avg_points = first_table.findAll('b')

 




#PLAYOFFS
#if Performance column on (http://www.landofbasketball.com/teams/records_golden_state_warriors.htm) page is not DNQ,
# that means there is an existing page for the stats
# General PL season url:
# pl_url = "http://www.landofbasketball.com/stats_by_team/{}_{}_warriors_pl.htm".format(from_years, to_years)



rs_urls = create_rs_urls_scrape([year for year in range(1946, 2017)])
rs_player_stats = scrape_player_stats(rs_urls)



pl_urls = []
