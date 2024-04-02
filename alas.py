import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

days_to_check = 30
today = datetime.utcnow()

rss_urls = [
    ["Amazon Linux", "https://alas.aws.amazon.com/alas.rss"],
    ["Amazon Linux 2", "https://alas.aws.amazon.com/AL2/alas.rss"],
    ["Amazon Linux 2023", "https://alas.aws.amazon.com/AL2023/alas.rss"]
]

criticities = [
    'low',
    'medium',
    'important',
    'critical'
]

def create_file(filename, filencontent):
    f = open(filename, 'w')
    f.write(filencontent)
    f.close()

def download_list(url):
    """Descarga una lista de vulnerabilidades"""
    my_request = requests.get(url)
    if my_request.status_code != 200:
        return("Error al realizar la consulta.")
    else:
        return my_request.text

def filter_vulnerabilities(my_text):
    """Filtra las vulnerabilidades publicadas el día anterior"""
    items = []
    root = ET.fromstring(my_text)
    first_day_checked = today - timedelta(days=days_to_check)

    for item in root.findall('.//item'):
        pub_date_str = item.find('pubDate').text
        pub_date = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %Z')
        formatted_pub_date = pub_date.strftime('%Y-%m-%d')
        title = item.find('title').text
        link = item.find('link').text
        for cricity in criticities:
            if (cricity in title) and (first_day_checked <= pub_date <= today):
                items.append([title, link, formatted_pub_date])
    return items

def get_vulnerabilities():
    result = "# Vulnerabilidades Amazon Linux\n\n"
    for i, rss_url in enumerate(rss_urls):
        vulnerabilities = filter_vulnerabilities(download_list(rss_url[1]))
        if (i == 0):
            result += "## " + rss_url[0]
        else:    
            result += "\n\n## " + rss_url[0]
        if (len(vulnerabilities)) < 1:
            result += "\n > No hay vulnerabilidades pendientes."
        for item in vulnerabilities:
            result += "\n* [" + item[0] + "](" + item[1] + ") (" + item[2] + ")."
    result += "\n"
    create_file("vulnerabilities_" + today.strftime("%Y_%m_%d") + ".md", result)

get_vulnerabilities()
