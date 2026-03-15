import csv

def load_dataset():
    waste_data = {}
    
    with open("dataset.csv", "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            waste_data[row["item"]] = row["category"]
    
    return waste_data


def classify_waste(item):
    
    waste_data = load_dataset()
    
    item = item.lower()
    
    if item in waste_data:
        return waste_data[item]
    
    else:
        return "unknown"