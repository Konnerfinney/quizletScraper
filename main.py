from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import glob




# function will get questions and answers from the file, write it to answers.txt
# and return list of questions written to check for duplicates
def get_text_from_file(file_name, write_file, check_list):
    # opens file to read html from
    f = open(file_name, 'r', encoding='utf-8')
    document= BeautifulSoup(f.read())

    # gets divs containing question/answers
    table = document.find_all('div', attrs = {'class':'SetPageTerms-term'})  

    # loops through all divs containing q/a
    for row in table:
        qaList = []
        splitList = str(row).split('<span class="TermText notranslate lang-en">')
        qList = splitList[1].split("</span>")
        qaList.append(qList[0].replace('<br/>','\n'))
        qList = splitList[2].split("</span>")
        qaList.append("ANSWER: " + qList[0])
        temp_str = ""

        # creates string w/ q/a and checks for duplicates
        for i in qaList:
            temp_str = temp_str + i + "\n" 
        if (temp_str not in check_list):
            write_file.write(temp_str)
            check_list.append(temp_str) 
                
    # return list for duplicate checking
    return check_list

# main function to get directory, start calling other functions
if __name__ ==  "__main__":
    print("Starting script")
    root = tk.Tk()
    root.withdraw()

    # open filepath dialog to get dir
    dir_path = filedialog.askdirectory()

    # gets all files within dir
    file_list = glob.glob(dir_path + "/*")

    # creates url for answers.txt
    answerURL = dir_path + "/answers.txt"

    # opens or creates file
    write_file = open(answerURL,"a")
    list_of_questions = []

    # loops through all files in dir
    for read_file in file_list:
        temp_list = []
        temp_list = get_text_from_file(read_file, write_file, list_of_questions)
        list_of_questions.append(temp_list)

    
