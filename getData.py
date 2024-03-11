import requests
from bs4 import BeautifulSoup
from makeCSV import add_data

##### NDR means No Data Reported #####

### Test URLS
## All Info Present
# URL = "https://www.kannapedia.net/strains/rsp10585"
## CBs no Terps
# URL = "https://www.kannapedia.net/strains/rsp10763"
## No CBs no Terps
# URL ="https://www.kannapedia.net/strains/rsp13088"


# Make the soup
def get_data(url):
    response = requests.get(url)
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")

    # Create dictionary for scraped data
    scraped_dict = {}

    # Find if the both CB and Terpene info is missing. If both are missing, do not collect data on the entry.
    # nip = No information provided
    nip = soup.find_all('p', class_='StrainChemicalInfo--none')
    if len(nip) == 2:
        print("Skip")
        pass
    else:
        print("Collecting Information...")
        # Title Information
        # Strain Name
        strain_name = soup.find(name="h1").text.strip()
        if strain_name:
            scraped_dict["Strain Name"] = strain_name
            print("Strain Name:", strain_name)
        else:
            scraped_dict["Strain Name"] = "NDR"
            print("Strain Name:", "NDR")

        # RSP (Registered Strain ID)
        rsp = soup.find('p', class_='StrainInfo--reportId').contents[-1].strip()
        if rsp:
            scraped_dict["RSP"] = rsp
            print("RSP:", rsp)
        else:
            scraped_dict["rsp"] = "NDR"
            print("RSP:", "NDR")

        # Grower Name
        grower_text = soup.find('p', class_='StrainInfo--registrant').text.strip()
        if grower_text:
            grower = grower_text.replace("Grower:", "").strip()
            scraped_dict["Grower"] = grower
            print("Grower:", grower)
        else:
            scraped_dict["Grower"] = "NDR"
            print("Grower:", "NDR")

        # General Information
        # Sample Name
        sample_name_element = soup.find(name='dt', string='Sample Name')
        if sample_name_element:
            sample_name = sample_name_element.find_next('dd').text.strip()
            scraped_dict["Sample Name"] = sample_name
            print("Sample Name:", sample_name)
        else:
            sample_name = "NDR"
            scraped_dict["Sample Name"] = sample_name
            print("Sample Name:", sample_name)

        # Accession Date (Date added to Kannapedia database)
        accession_date_element = soup.find('dt', string='Accession Date')
        if accession_date_element:
            accession_date_value = accession_date_element.find_next('dd').text.strip()
            scraped_dict["Accession Date"] = accession_date_value
            print("Accession Date:", accession_date_value)
        else:
            scraped_dict["Accession Date"] = "NDR"
            print("Accession Date:", "NDR")

        # Reported Plant Sex
        plant_sex_element = soup.find('dt', string='Reported Plant Sex')
        if plant_sex_element:
            plant_sex_value = plant_sex_element.find_next('dd').text.strip()
            scraped_dict["Reported Plant Sex"] = plant_sex_value
            print("Reported Plant Sex:", plant_sex_value)
        else:
            scraped_dict["Reported Plant Sex"] = "NDR"
            print("Reported Plant Sex:", "NDR")

        # Report Type
        report_type_element = soup.find('dt', string='Report Type')
        if report_type_element:
            report_type_value = report_type_element.find_next('dd').text.strip()
            scraped_dict["Report Type"] = report_type_value
            print("Report Type:", report_type_value)
        else:
            scraped_dict["Report Type"] = "NDR"
            print("Report Type:", "NDR")

        # Rarity Value
        rarity_value_element = soup.find('figcaption', class_='DataPlot--caption')
        if rarity_value_element:
            rarity_value = rarity_value_element.strong.a.text.strip()
            scraped_dict["Rarity"] = rarity_value
            print("Rarity:", rarity_value)
        else:
            scraped_dict["Rarity"] = "NDR"
            print("Rarity:", "NDR")

        # Genetic Information
        # Heterozygosity
        heterozygosity_element = soup.find_all(name='figcaption', class_='DataPlot--caption')
        if heterozygosity_element:
            heterozygosity = heterozygosity_element[1].strong.text.strip()
            scraped_dict["Heterozygosity"] = heterozygosity
            print("Heterozygosity:", heterozygosity)
        else:
            scraped_dict["Heterozygosity"] = "NDR"
            print("Heterozygosity:", "NDR")

        # Chemical Information
        # Cannabinoids
        cannabinoid_terms = ["THC + THCA", "CBD + CBDA", "THCV + THCVA", "CBC + CBCA", "CBG + CBGA", "CBN + CBNA"]

        for term in cannabinoid_terms:
            element = soup.find('dt', string=term)
            if element:
                value = element.find_next('dd').text.strip()
                scraped_dict[term] = value
                print(f"{term}:", value)
            else:
                scraped_dict[term] = "NDR"
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
                scraped_dict[term] = value
                print(f"{term}: {value}")
        else:
            for terp in terpenoid_terms:
                scraped_dict[terp] = "NDR"
                print(f"{terp}:", "NDR")

        add_data(scraped_dict)

# For testing code
# get_data(URL)
