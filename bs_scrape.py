from urllib2 import urlopen
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy

from model import Player, RSGame, PLGame
from model import connect_to_db, db
from server import app


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
    """Scrape each page for each player's stats for regular season/playoffs"""

    # get_player_stats('http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm')

    soup = start_scrape(url)
    tables = soup.findChildren('table')
    first_table = tables[0]
    rows = first_table.findChildren('tr')
    main_url = "http://www.landofbasketball.com/"

    for row in rows[1:]:
        player_name = row.findChildren('td')[0].text.strip()
        games_played = row.findChildren('td')[1].text.strip()
        avg_min = row.findChildren('td')[2].text.strip()
        avg_pts = row.findChildren('td')[3].text.strip()
        avg_rebounds = row.findChildren('td')[6].text.strip()
        avg_assists = row.findChildren('td')[7].text.strip()
        avg_steals = row.findChildren('td')[8].text.strip()
        avg_blocks = row.findChildren('td')[9].text.strip()
        player_profile_link = main_url+row.find_all('a', href=True)[0].attrs['href'][3:]

        jersey = get_player_jersey(player_profile_link)

        if not Player.query.filter(Player.url==player_profile_link).all():
            new_player = Player(name=player_name,
                                url=player_profile_link,
                                jersey=jersey)
            db.session.add(new_player)
            db.session.commit()


        #print player_name, games_played, avg_min, avg_pts, avg_rebounds, avg_assists, avg_steals, avg_blocks, player_profile_link, jersey #need to save these to db


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
    # jersey_list = jersey.split(",  ") #create list of all jersey numbers player has had
    

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

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    rs_urls = create_rs_urls_scrape([year for year in range(2010, 2017)]) #1946 , 2017
    rs_player_stats = scrape_player_stats(rs_urls)



# pl_urls = []
