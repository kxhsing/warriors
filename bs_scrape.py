from urllib2 import urlopen
from bs4 import BeautifulSoup

# Sample regular season url: http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm
# Sample playoffs url: http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_pl.htm
sample_urls = ['http://www.landofbasketball.com/stats_by_team/2015_2016_warriors_rs.htm', 
'http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm']

# REGULAR SEASON
# class RSScraper(object):???
def create_rs_urls_scrape(years):
    """Create list of urls to scrape for regular season stats"""

    urls = []
    for year in years:
        urls.append("http://www.landofbasketball.com/stats_by_team/{}_{}_warriors_rs.htm".format(year, year+1))

    return urls


def start_scrape(url):
    """Scrapes url for html source"""

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def scrape_rs_urls(urls):
    scraped_html = []
    for url in urls:
        scraped_html.append(start_scrape(url))

    return scraped_html

def get_points(soup=start_scrape('http://www.landofbasketball.com/stats_by_team/2016_2017_warriors_rs.htm')):
    table = soup.findAll('b')

    for x in table:
        print x
        print x.text

        # print x.find('b').text



#PLAYOFFS
#if Performance column on (http://www.landofbasketball.com/teams/records_golden_state_warriors.htm) page is not DNQ,
# that means there is an existing page for the stats
# General PL season url:
# pl_url = "http://www.landofbasketball.com/stats_by_team/{}_{}_warriors_pl.htm".format(from_years, to_years)



rs_urls = create_rs_urls_scrape([year for year in range(1946, 2017)])
rs_html = scrape_rs_urls(rs_urls)



pl_urls = []
