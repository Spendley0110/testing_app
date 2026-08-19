from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import sys
from urllib.parse import urljoin, urlparse
from RequestGuard import RequestGuard
def validate_commands(argument):
    if len(argument):
        if (argument[0] == "-c" and len(argument) == 4):
            return True
        elif (argument[0] == "-p" and len(argument) == 4):
            return True
        elif (argument[0] == "-i" and len(argument) >= 4):
            return True
            return True
        else:
            return False
    return False

def count_page_links(request_guard, link, dictionary):
    parsed = urlparse(link)
    response = request_guard.make_get_request(link)
    if response is None:
        return dictionary
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    href_contents = soup.find_all('a')
    for hyperlink in href_contents:
        found_link = (urljoin(f"{parsed.scheme}://{parsed.netloc}{parsed.path}", hyperlink.attrs['href']).split('#')[0])
        if found_link in dictionary:
            dictionary[found_link] += 1
        else:
            dictionary[found_link] = 1
            if request_guard.can_follow_link(found_link):
                dictionary = count_page_links(request_guard, found_link, dictionary)
    return dictionary

def count_links(argument):
    #The base link starts as one, because it would be added to the links to visit as originally written, then counted due to being in that list, if I functioned off of a two link
    #system. By checking whether I can follow a link before throwing it in the recursive function, I skip counting that original visit, only needing to check the values on the site,
    #rather than starting with a hard value in a to visit list.
    dictionary = {f"{argument[1]}": 1}
    robot = RequestGuard(argument[1])
    dictionary = count_page_links(robot, argument[1], dictionary)
    bin = []
    counts = list(dictionary.values())
    for i in range(1, max(counts) + 2):
        bin.append(i)
    values, bins, a = plt.hist(counts, bin)
    plt.savefig(argument[2])
    plt.clf()
    file = open(argument[3], 'w')
    i = 0
    while i < len(values):
        file.write(f"{bins[i]},{values[i]}\n")
        i+=1
    file.close()
    return dictionary

def plot_data(argument):
    colors = ['b', 'g', 'r', 'k']
    plt.clf()
    robot = RequestGuard(argument[1])
    response = (robot.make_get_request(argument[1])).text
    soup = BeautifulSoup(response, 'html.parser')
    tables = soup.find_all('table')
    table = soup.find('table')
    for object in tables:
        if object.attrs['id'] == "CS111-Project4b":
            table = object
    rows = table.find_all('tr')
    row_example = rows[0].find_all('td')
    full_data = {}
    for i in range(len(row_example) - 1):
        full_data = []
        x = []
        y = []
        for row in rows:
            temp_lst = []
            for cell in row.find_all('td'):
                temp_lst.append(cell.text)
            full_data.append(temp_lst)
            row_x = float(row.find_all('td')[0].text)
            row_y = float(row.find_all('td')[i + 1].text)
            x.append(row_x)
            y.append(row_y)
        plt.plot(x, y, colors[i])
    file = open(argument[3], 'w')
    for data in full_data:
        temp_str = ""
        while len(data):
            try:
                data[0] = f"{float(int(data[0])):.1f}"
            except ValueError:
                data[0] = float(data[0])
            temp_str = temp_str + f"{(data.pop(0))},"
        temp_str = temp_str[:-1]
        file.write(f"{temp_str}\n")
    file.close()
    plt.savefig(argument[2])
    plt.clf()
    
if __name__ == "__main__":
    given_argument = sys.argv[1:len(sys.argv)]
    if validate_commands(given_argument):
        if (given_argument[0] == "-c"):
            count_links(given_argument)
        elif (given_argument[0] == "-p"):
            plot_data(given_argument)
        elif (given_argument[0] == "-i"):
            pass
        else:
            print("invalid arguments")
    else:
        print("invalid arguments")