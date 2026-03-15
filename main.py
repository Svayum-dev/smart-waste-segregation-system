from waste_classifier import classify_waste

def display_bin(category):
    
    if category == "biodegradable":
        print("\nDispose in GREEN BIN")
    
    elif category == "recyclable":
        print("\nDispose in BLUE BIN")
    
    elif category == "non-recyclable":
        print("\nDispose in RED BIN")
    
    else:
        print("\nItem not found in database.")


def main():
    
    print("Smart Waste Segregation System")
    print("--------------------------------")
    
    item = input("Enter waste item: ")
    
    category = classify_waste(item)
    
    print("Waste Category:", category)
    
    display_bin(category)


if __name__ == "__main__":
    main()