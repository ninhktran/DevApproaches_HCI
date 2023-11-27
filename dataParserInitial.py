import csv
import requests

def filter_csv(input_file, output_file, fieldnames):
    try:
        with open(input_file, 'r', newline='') as input_csvfile, \
             open(output_file, 'w', newline='') as output_csvfile:
            csv_reader = csv.DictReader(input_csvfile)
            csv_writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
                        
            repo_dicts = {
                'cwa-app-android': 'https://github.com/corona-warn-app/cwa-app-android',
                'cwa-app-ios': 'https://github.com/corona-warn-app/cwa-app-ios',
                'firefox-ios': 'https://github.com/mozilla-mobile/firefox-ios',
                'healthchecks': 'https://github.com/healthchecks/healthchecks',
                'mobile-android': 'https://github.com/covidsafe-support/mobile-android',
                'mobile-ios': 'https://github.com/AU-COVIDSafe/mobile-ios'  
            }            
            
            hci_components = ['Inclusiveness','Privacy/security','Compatibility','Location/Language','Preference','Satisfaction','Emotional aspects','Accessibility']
                        
            for row in csv_reader:
                # only writes the rows that are related to an HCI category
                hci_related = row['#1: Inclusiveness']+row['#2: Privacy/security']+row['#3: Compatibility']+row['#4: Location/Language']+row['#5: Preference']+row['#6: Satisfaction']+row['#7: Emotional aspects']+row['#8: Accessibility']
                if hci_related.count('1') > 0:
                    if row['project_name'] in repo_dicts:
                        issue_link = repo_dicts[row['project_name']] + '/issues/'+row['issue_number']

                    else:
                        issue_link = 'github page for issue not found\n issue#:'+row['issue_number']
                    title = ''
                    creation_date = '' 
                    issue_state = ''
                    state_reason = '' 
                    closed_at = ''
                    
                    selected_categories = []

                    # Iterate through each bit in the binary string and check if it's "1"
                    # If the bit is "1" then the row is part of that HCI attribute
                    for i, bit in enumerate(hci_related):
                        if bit == "1":
                            selected_categories.append(hci_components[i])

                    # Join the selected categories into a comma-separated string
                    issue_hci_attributes = ", ".join(selected_categories)

                    csv_writer.writerow({'project_name': row['project_name'],
                                        'issue_link': issue_link,
                                        'issue_number': row['issue_number'],
                                        'author': row['author'],
                                        'Issue_title': title,
                                        'issue_hci_attributes':issue_hci_attributes,
                                        'Created_At':creation_date,
                                        'Issue_State': issue_state,
                                        'State_Reason':state_reason,
                                        'closed_at':closed_at,
                                        'body_summary': '',
                                        'body_text': row['body_text']})
        print(f"Filtered CSV file saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



def main():
    # Change the input and output file paths to a one
    input_file = 'csv_Human-centric-issues-GitHub-552021/Final data-Table 1.csv'
    output_file = 'cleanedData.csv'
    columns_to_keep = ['project_name', 'issue_link','issue_number','author','Issue_title','issue_hci_attributes','Created_At','Issue_State','State_Reason','closed_at','body_summary', 'body_text']

    filter_csv(input_file, output_file, columns_to_keep)

if __name__ == "__main__":
    main()

