import requests
from bs4 import BeautifulSoup
import csv
import sys

def main():
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    check_arguments(base_url)
    url = sys.argv[1]
    file_name = sys.argv[2]
    first_soup = get_response(url)
    results, header = get_municipality_links(first_soup, base_url)
    print(f"Saving data to file: {file_name}")
    save_to_csv(results, header, file_name)
    print("All done, closing...")

def check_arguments(base_url):
    if len(sys.argv) != 3:
        print("Arguments were not entered correctly. Please check README and try it again.")
        exit()
    elif base_url not in sys.argv[1]:
        print("You have entered wrong URL. Please check README and try it again.")
        exit()
    elif ".csv" not in sys.argv[2]:
        print("You have entered wrong file name. Please check README and try it again.")
        exit()
    else:
        print(f"Downloading data from selected URL: {sys.argv[1]}")

def get_response(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, "html.parser")

def get_municipality_links(soup, base_url):
    results = []
    header = []

    table = soup.find("table", {"class": "table"})  # hlavní tabulka obcí
    rows = table.find_all("tr")[2:]  # přeskočíme hlavičku

    for row in rows:
        columns = row.find_all("td")
        code = columns[0].text.strip()
        location = columns[1].text.strip()
        relative_link = columns[0].find("a")["href"]
        full_url = base_url + relative_link

        detail_soup = get_response(full_url)

        if not header:  # vytvoříme hlavičku pouze jednou
            header = create_header(detail_soup)

        row_data = [code, location]
        row_data.extend(collect_numbers(detail_soup))
        results.append(row_data)

    return results, header

def collect_numbers(soup):
    data = []
    registered = soup.find("td", {"headers": "sa2"}).text
    envelopes = soup.find("td", {"headers": "sa5"}).text
    valid = soup.find("td", {"headers": "sa6"}).text

    data.extend([clean_numbers(registered), clean_numbers(envelopes), clean_numbers(valid)])
    data.extend(collect_votes(soup))
    return data

def collect_votes(soup):
    votes = []
    tables = soup.find_all("div", {"class": "t2_470"}) + soup.find_all("div", {"class": "t2_471"})

    for table in tables:
        rows = table.find_all("tr")[2:]  # přeskočit hlavičku
        for row in rows:
            tds = row.find_all("td")
            if len(tds) >= 3:
                vote_count = clean_numbers(tds[2].text)
                votes.append(vote_count)

    return votes

def create_header(soup):
    header = ["Code", "Location", "Registered", "Envelopes", "Valid"]
    party_names = soup.find_all("td", {"class": "overflow_name"})
    for party in party_names:
        header.append(party.text.strip())
    return header

def clean_numbers(text):
    return text.replace("\xa0", "").replace(" ", "")

def save_to_csv(data, header, filename):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == "__main__":
    main()

