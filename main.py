#!/usr/bin/env python3
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import glob
from gsearch import search_google
import webbrowser


def get_text_from_file(write_file, read_file) -> None:
	'''
    Gets the questions to the text file and writes the scraped content into the final file

            Parameters:
                    write_file (file): the final file to be written to
                    read_file (file): the file containing the question prompts

            Returns:
                    None
    '''
	content = read_file.read()
	content_list = content.split("\n\n")
	curr_list = list()

	for question in content_list:
		string = question.split("\n")[0]
		curr_list = curr_list + search_google(string,write_file, curr_list)
	write_file.close()
	read_file.close()


# main function to get directory, start calling other functions
def run() -> None:
	'''
		Gets the file from a tkinter directory pop up and creates the final write file before passing it off to other functions

            Parameters:
                    None
            Returns:
                    None
    '''
	print("Starting script")
	root = tk.Tk()
	root.withdraw()

    # open filepath dialog to get dir
	file_path = filedialog.askopenfilename()

	print("opening file {}".format(file_path))
    
    # gets the file dir by editing abs file path
	file_list = file_path.split("/")
	file_list.pop()
	file_dir = "/".join(file_list) + "/"

    # opens file w/ questions
	file1 = open(file_path,"r")

    #opens file to write to 
	file2 = open(file_dir + "answers.txt","a")

 
	get_text_from_file(file2, file1)
	print("done scraping")
	webbrowser.open(file_dir + "answers.txt")




if __name__ == "__main__":
	run()