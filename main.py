import requests
from bs4 import BeautifulSoup
import os

def read_web_page(url) :
    output = requests.get(url)
    return output

def parse_HTML(html) :
    parsed = BeautifulSoup(html.content, 'html.parser')
    return parsed

def output_text(parsed_html) :
    text = parsed_html.find_all("div", class_="quote")
    for line in text :
        l = line.find(class_="text").text
        author = line.find(class_="author").text
        print(f'{l}\n--{author}\n')

def __main__() :
    is_running = True
    c_page = 1

    url = "https://quotes.toscrape.com/page/"

    while is_running :
        #Clearing Terminal
        if os.name == "nt" :
            os.system("cls")
        else :
            os.system("clear")

        #Title
        print(f'Welcome to QuoteViewer. Currently on page {c_page} / 10\n----------')

        #Content
        active_url = url + str(c_page)
        output_text(parse_HTML(read_web_page(active_url)))

        #Command Bar
        print(f'----------\n(N)ext Page, (P)revious Page, (J)ump to Page, (Q)uit')

        #Handling User Input
        input_validation = False
        while not input_validation :
            user_input = input().lower()

            #Next
            if user_input == "n" :
                c_page += 1
                if c_page > 10 :
                    c_page = 1
                input_validation = True
            #Previous
            elif user_input == "p" :
                c_page -= 1
                if c_page <= 0 :
                    c_page = 10
                input_validation = True
            #Jump
            elif user_input == "j" :
                #Taking User Input for Page Jump
                jump_input_valid = False
                while not jump_input_valid :
                    page_jump = input("Jump to which page? ")
                    try :
                        if int(page_jump) > 0 and int(page_jump) < 11 :
                            c_page = int(page_jump)
                            jump_input_valid = True
                        else :
                            print(f'Cannot jump to page {page_jump}, enter a number between 1 - 10')
                    except :
                        print("Enter a number please.")
                input_validation = True
            #Quit
            elif user_input == "q" :
                print("Exiting...")
                input_validation = True
                is_running = False
            else :
                print("Invalid Input.")

__main__()