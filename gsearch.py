from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

#constant
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

def search_google(question_text: str, write_file, curr_list: list) -> list:
    query = "quizlet " + question_text
    counter = 1
    for i in search(query,num_results=2, lang="en"):
        if i not in curr_list:
            curr_list.append(i)
            url = i
            if re.search("https://quizlet.com/",url):
                print(f'scraping {url}')

                soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

                for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
                    string = ""
                    string = string +"\n"+ ('QUESTION {}'.format(counter)) + "\n\n" + (question.get_text(strip=True, separator='\n')) + "\n\n" + ('ANSWER:') + "\n"+ answer.get_text(strip=True, separator='\n') +"\n" + ('-' * 160)
                    counter += 1
                    try:
                        write_file.write(string)
                    except UnicodeEncodeError:
                        pass
    return curr_list







