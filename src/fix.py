import os, chardet
import pandas as pd

DELETE_THIS = ["Title", "Suffix", "Initials", "Web Page", "Gender", "Birthday", "Anniversary", "Location", "Language", "Internet Free Busy", "Notes", "Pager", "Home Fax", "Home Address", "Home Street", "Home Street 2", "Home Street 3", "Home Address PO Box", "Home City", "Home State", "Home Postal Code", "Home Country", "Spouse", "Children", "Manager's Name", "Assistant's Name", "Referred By", "Company Main Phone", "Business Phone", "Business Phone 2", "Business Fax", "Assistant's Phone", "Company", "Job Title", "Department", "Office Location", "Organizational ID Number", "Profession", "Account", "Business Address", "Business Street", "Business Street 2", "Business Street 3", "Business Address PO Box", "Business City", "Business State", "Business Postal Code", "Business Country", "Other Phone", "Other Fax", "Other Address", "Other Street", "Other Street 2", "Other Street 3", "Other Address PO Box", "Other City", "Other State", "Other Postal Code", "Other Country", "Callback", "Car Phone", "ISDN", "Radio Phone", "TTY/TDD Phone", "Telex", "User 1", "User 2", "User 3", "User 4", "Keywords", "Mileage", "Hobby", "Billing Information", "Directory Server", "Sensitivity", "Priority", "Private", "Categories"]

def detect_encoding(file_path):
    with open(file_path, 'rb') as textfile:
        result = chardet.detect(textfile.read())
        print(result['encoding'])
    return result['encoding']

def add_empty_df():
    columns = ["First Name", "Middle Name", "Last Name", "Title", "Suffix", "Initials", "Web Page", "Gender", "Birthday", "Anniversary", "Location", "Language", "Internet Free Busy", "Notes", "E-mail Address", "E-mail 2 Address", "E-mail 3 Address", "Primary Phone", "Home Phone", "Home Phone 2", "Mobile Phone", "Pager", "Home Fax", "Home Address", "Home Street", "Home Street 2", "Home Street 3", "Home Address PO Box", "Home City", "Home State", "Home Postal Code", "Home Country", "Spouse", "Children", "Manager's Name", "Assistant's Name", "Referred By", "Company Main Phone", "Business Phone", "Business Phone 2", "Business Fax", "Assistant's Phone", "Company", "Job Title", "Department", "Office Location", "Organizational ID Number", "Profession", "Account", "Business Address", "Business Street", "Business Street 2", "Business Street 3", "Business Address PO Box", "Business City", "Business State", "Business Postal Code", "Business Country", "Other Phone", "Other Fax", "Other Address", "Other Street", "Other Street 2", "Other Street 3", "Other Address PO Box", "Other City", "Other State", "Other Postal Code", "Other Country", "Callback", "Car Phone", "ISDN", "Radio Phone", "TTY/TDD Phone", "Telex", "User 1", "User 2", "User 3", "User 4", "Keywords", "Mileage", "Hobby", "Billing Information", "Directory Server", "Sensitivity", "Priority", "Private", "Categories"]
    df = pd.DataFrame(columns=columns)
    return df

def merge_data(df):
    # Iterates over all csv in "input" folder (local) and merge data with the dataframe.
    for raw_file in os.listdir("input"):
        if raw_file.endswith(".csv"):
            file_path = os.path.join("input", raw_file)
            merge_df = pd.read_csv(file_path, encoding=detect_encoding(file_path), sep=",", index_col=False)
            df = pd.concat([df, merge_df], ignore_index=True)
    return df

def clean_data(df):
    df.drop(columns=DELETE_THIS, inplace=True)
    df.dropna(how="all", inplace=True)
    df.drop_duplicates(inplace=True)
    return df

if __name__ == "__main__":
    df = add_empty_df()
    df = merge_data(df)
    df = clean_data(df)
    df.to_csv("output/contacts.csv", index=False, encoding="utf-8", errors='ignore')
