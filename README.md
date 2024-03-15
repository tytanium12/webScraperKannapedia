# webScraperKannapedia

The Kannapedia Database WebScraper

This bot is designed to scrape data from the Kannapedia cannabis strain database website. Here are a few notes about the current state of the program, its purpose, and how it was designed. Finally, in Section 4, I give a quick run-down of how to use the program.

1) Purpose of the Program
The purpose of this program is to automatically index each entry into the Kannapedia database. This database contains information of "registered strains" of cannabis. The scope of the information includes registered name, genetic information, chemical information, and other information such as "rarity" of a strain.

This program is designed to crawl through each database entry and record the specified information into a CSV file for future data analysis.

2) Design of the Program

The program uses beautiful soup to scrape data and selenium to drive the browser to gather the data. The output is a CSV file with one line per cannabis database strain entry webpage. ** NOTE ** Currently the program is desinged to skip all of the database entries that do not contain either cannabinoid nor terpene content information. I am a chemist, so I am initially focusing on gathering the chemical information. I plan to add to this program to capture more and more of the genetic information over time so I can include that in my data analysis.

The program is divided into 3 major sections: getData.py, makeCSV.py, and main.py

The first section I wrote is the WebScraper using beautiful soup. This file is called getData.py. The code defines the function get_data which requires a URL input. The URLs are initially provided manually so I could program and test the WebScraper. Later, the URLs are provided by the selenium webdriver through main.py which I will explain last.

The second section I wrote was makeCSV which serves two functions: The first is the function new_csv which creates the initial CSV file with the column headings in place. The second is a function called add_data whiched takes a dictionary of data from getData.py and writes it to the next line of the pre-made CSV file. The dictionary of data from getData has key:value pairs where the keys are the column headings and the values are the corresponding data scraped from the database entry.

Finally, we get to main.py which automates the gathering of URLs for database entries and gathering their corresponding data. main.py uses the selenium webdriver with the chrome browser to gather the data. It initiates by going to "/strains" of the Kannapedia website and clicking the "Allow Cookies" button to give a view of the first page of the database, which is currently 26 pages long. The program operates by generating a list of URLs where each list entry is a URL to a strain database entry. This list is then passed on item at a time to get_data in getData.py to scrape the data. getData.py in turn passes the data automatically to add_data in makeCSV.py.

The program reports when it is gathering links, skipping database entries, gathering data, and when it has successfully completed.

3) Current State of the Program

Currently this program gathers the following data from the Kannapedia strain database entries:

['Strain Name', 'RSP', 'Grower', 'Sample Name', 'Accession Date',
       'Reported Plant Sex', 'Report Type', 'Rarity', 'Heterozygosity',
       'THC + THCA', 'CBD + CBDA', 'THCV + THCVA', 'CBC + CBCA', 'CBG + CBGA',
       'CBN + CBNA', 'α-Bisabolol', 'Borneol', 'Camphene', 'Carene',
       'Caryophyllene oxide', 'β-Caryophyllene', 'Fenchol', 'Geraniol',
       'α-Humulene', 'Limonene', 'Linalool', 'Myrcene', 'α-Phellandrene',
       'Terpinolene', 'α-Terpineol', 'α-Terpinene', 'γ-Terpinene',
       'Total Nerolidol', 'Total Ocimene', 'α-Pinene', 'β-Pinene']

Most of the genetic information is not gathered by the program at this time. The focus was to gather the chemical information for analysis first. I plan to program this bot to gather more and more data over time.

4) Quick Start

The first thing you need to do is go to makeCSV.py directly. Scroll down to the comments just below the make_csv() function definition. Remove the comment hash in front of new_csv() in line 53 that says "# new_csv()". Run the makeCSV.py file one time. A new CSV called scraped_data.csv should be created. Replace the comment hash on line 53 and save. Whenever you need to make a fresh CSV, delete, rename, or move the old CSV to a different folder and then follow this procedure again.

You can use getData.py directly for testing the webscraping functionality. But unless you're changing the data being gathered, you won't need to mess with this file.

To initiate the program, MAKE SURE YOU FOLLOWED THE INTRUCTIONS TO MAKE A NEW CSV AT THE BEGINNING OF THIS QUICK START SECTION. Ensure that you have a fresh scraped_data.csv file. Then simply run the main.py program and watch it do its work. It will give status updates in the console and you can watch the webdriver drive the chrome browser. When it is done it will print "No more pages. Exiting." to the console.

Now you can use the data for whatever you please!

Closing:

Thank you for taking the time to read this file and show some love to this program. I hope you have fun with it and feel free to share any interesting information, ideas, or critiques that you have!

Kannapedia Website:
https://www.kannapedia.net/
