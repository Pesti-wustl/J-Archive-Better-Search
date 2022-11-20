from selenium import webdriver
from selenium.webdriver.common.by import By
import time

placeholder = "Estonia"
placeholder_fix = placeholder.replace(" ","+")

#After testing no need for Browser to show when ran
op = webdriver.ChromeOptions()
op.add_argument('headless')
browser = webdriver.Chrome('chromedriver', options=op)
question_bank = []


#amount of pages
while True: #So Chrome does not get garbage collected

    #Google search J-Archive pages with keyword
    for i in range(1):
        elements = browser.get("https://google.com/search?q=site%3Aj-archive.com+" + placeholder_fix)
        browser.implicitly_wait(5)
        archive_links = browser.find_elements(By.XPATH, "//a[contains(@href,'https://j-archive.com/') or contains(@href, 'https://www.j-archive.com')]")
        translated_archive_links = []
        
        #Fix each link and put into a list
        for link in archive_links:
            game_number = link.get_attribute("href")
            game_id_number = game_number.find("=") + 1
            game_url = "https://www.j-archive.com/showgame.php?game_id=" + str(game_number[game_id_number:])
            translated_archive_links.append(game_url)
        
        #Put each question into the question bank
        good_clues = {}
        for link in translated_archive_links:
            #number (e.g. col6_row5: clue_text)

            #Part 1 - find clues asking with query
            browser.get(link)
            #time.sleep(3)
            print("kodak")
            all_clues_with_query_numbs = []
            clues_with_query = browser.find_elements(By.XPATH, f"//td[@class='clue_text' and contains(.,'{placeholder}')]")
            for clue in clues_with_query:
                #FOR NOW THIS OVERWRITES (its because im not done yet.)
                good_clues[clue.get_attribute("id")] = link
            
        print(good_clues)
    break
        

            
#part 1 nearly done - clues where the keyword is a part of the *question*
#part 2 - clues where keyword is part of the *answer* (using showgameresponses)



