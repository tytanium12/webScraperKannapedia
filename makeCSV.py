import csv


# Make the CSV
def new_csv():
    column_names = [
        "Strain Name",
        "RSP",
        "Grower",
        "Sample Name",
        "Accession Date",
        "Reported Plant Sex",
        "Report Type",
        "Rarity",
        "Heterozygosity",
        "THC + THCA",
        "CBD + CBDA",
        "THCV + THCVA",
        "CBC + CBCA",
        "CBG + CBGA",
        "CBN + CBNA",
        "α-Bisabolol",
        "Borneol",
        "Camphene",
        "Carene",
        "Caryophyllene oxide",
        "β-Caryophyllene",
        "Fenchol",
        "Geraniol",
        "α-Humulene",
        "Limonene",
        "Linalool",
        "Myrcene",
        "α-Phellandrene",
        "Terpinolene",
        "α-Terpineol",
        "α-Terpinene",
        "γ-Terpinene",
        "Total Nerolidol",
        "Total Ocimene",
        "α-Pinene",
        "β-Pinene",
    ]

    csv_file_path = "scraped_data.csv"

    with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=column_names)

        csv_writer.writeheader()

# Make a new CSV with headers when needed
# new_csv()
# Add new data to the CSV


def add_data(data):
    csv_file_path = "scraped_data.csv"

    # Writing to CSV file with utf-8 encoding in append mode
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=data.keys())

        # Write the data (row)
        csv_writer.writerow(data)
