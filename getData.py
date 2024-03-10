import bs4
import lxml
import requests
from bs4 import BeautifulSoup

### NDR means No Data Reported

### URL - Will expand to use webdriver to crawl the pages for me
# This whole file needs to become a class "GrabData" with an input of a URL that is clicked on by the webdriver
# The webdriver will be driven by another file
### Test URLS
## All Info Present
# URL = "https://www.kannapedia.net/strains/rsp10585"
## CBs no Terps
# URL = "https://www.kannapedia.net/strains/rsp10763"
## No CBs no Terps
# URL ="https://www.kannapedia.net/strains/rsp13088"

# Make the soup
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# print(all_content)

# Title Information
# Strain Name
strain_name = soup.find(name="h1").text.strip()
if strain_name:
    print("Strain Name:", strain_name)
else:
    print("Strain Name:", "NDR")

# RSP (Registered Strain ID)
RSP = soup.find(name="span", class_="StrainInfo--reportIdPrefix").text.strip()
if RSP:
    print("RSP:", RSP)
else:
    print("RSP:", "NDR")

# Grower Name
grower_text = soup.find('p', class_='StrainInfo--registrant').text.strip()
if grower_text:
    grower = grower_text.replace("Grower:", "").strip()
    print("Grower:", grower)
else:
    print("Grower:", "NDR")

# General Information
# Sample Name
sample_name_element = soup.find(name='dt', string='Sample Name')
if sample_name_element:
    sample_name = sample_name_element.find_next('dd').text.strip()
    print("Sample Name:", sample_name)
else:
    sample_name = "NDR"
    print("Sample Name:", sample_name)

# Accession Date (Date added to Kannapedia database)
accession_date_element = soup.find('dt', string='Accession Date')
if accession_date_element:
    accession_date_value = accession_date_element.find_next('dd').text.strip()
    print("Accession Date:", accession_date_value)
else:
    print("Accession Date:", "NDR")

# Reported Plant Sex
plant_sex_element = soup.find('dt', string='Reported Plant Sex')
if plant_sex_element:
    plant_sex_value = plant_sex_element.find_next('dd').text.strip()
    print("Reported Plant Sex:", plant_sex_value)
else:
    print("Reported Plant Sex:", "NDR")

# Report Type
report_type_element = soup.find('dt', string='Report Type')
if report_type_element:
    report_type_value = report_type_element.find_next('dd').text.strip()
    print("Report Type:", report_type_value)
else:
    print("Report Type:", "NDR")

# Rarity Value
rarity_value_element = soup.find('figcaption', class_='DataPlot--caption')
if rarity_value_element:
    rarity_value = rarity_value_element.strong.a.text.strip()
    print("Rarity:", rarity_value)
else:
    print("Rarity:", "NDR")

# Genetic Information
# Heterozygosity
heterozygosity_element = soup.find_all(name='figcaption', class_='DataPlot--caption')
if heterozygosity_element:
    heterozygosity = heterozygosity_element[1].strong.text.strip()
    print("Heterozygosity:", heterozygosity)
else:
    print("Heterozygosity:", "NDR")

# Chemical Information
# Cannabinoids
cannabinoid_terms = ["THC + THCA", "CBD + CBDA", "THCV + THCVA", "CBC + CBCA", "CBG + CBGA", "CBN + CBNA"]

for term in cannabinoid_terms:
    element = soup.find('dt', string=term)
    if element:
        value = element.find_next('dd').text.strip()
        print(f"{term}:", value)
    else:
        print(f"{term}:", "NDR")

# Terpenoids
terpenoid_terms = [
    'α-Bisabolol',
    'Borneol',
    'Camphene',
    'Carene',
    'Caryophyllene oxide',
    'β-Caryophyllene',
    'Fenchol',
    'Geraniol',
    'α-Humulene',
    'Limonene',
    'Linalool',
    'Myrcene',
    'α-Phellandrene',
    'Terpinolene',
    'α-Terpineol',
    'α-Terpinene',
    'γ-Terpinene',
    'Total Nerolidol',
    'Total Ocimene',
    'α-Pinene',
    'β-Pinene',
]

terpenoid_rows = soup.select('.StrainChemicalInfo--terpenoids .ChemicalValues--row')

if terpenoid_rows:
    for row in terpenoid_rows:
        term = row.find('dt').text.strip()
        value = row.find('dd').text.strip()
        print(f"{term}: {value}")
else:
    for terp in terpenoid_terms:
        print(f"{terp}:", "NDR")












#### Random Comments ###
# Test code for me to figure my way around
# all_titles = soup.find_all(name="dt")
# print(all_titles)
#
# clean_titles = []
#
# for title in all_titles:
#     clean_titles.append(title.text)
#
# print(clean_titles)
#
# all_content = []
#
# for title in clean_titles:
#     all_content.append(soup.find(string=title).find_next().text)
#