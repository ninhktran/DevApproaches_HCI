import csv
import requests

"""
This takes an already preprocessed csv file and adds the info needed from the GitHub API
"""
def filter_csv(input_file, output_file, fieldnames):
    try:
        with open(input_file, 'r', newline='') as input_csvfile, \
             open(output_file, 'w', newline='') as output_csvfile:
            csv_reader = csv.DictReader(input_csvfile)
            
            csv_writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()

            api_repo_dicts = {
                'cwa-app-android': 'https://api.github.com/repos/corona-warn-app/cwa-app-android',
                'cwa-app-ios': 'https://api.github.com/repos/corona-warn-app/cwa-app-ios',
                'firefox-ios': 'https://api.github.com/repos/mozilla-mobile/firefox-ios',
                'healthchecks': 'https://api.github.com/repos/healthchecks/healthchecks'
                ## Commented out because the repos do not have an issue tab available anymore
                #'mobile-android': 'https://api.github.com/repos/covidsafe-support/mobile-android',
                # 'mobile-ios': 'https://api.github.com/repos/AU-COVIDSafe/mobile-ios' 
            }
            
                        
            for row in csv_reader:
                if row['project_name'] in api_repo_dicts:
                    url = api_repo_dicts[row['project_name']]+'/issues/'+row['issue_number']

                    # Send a GET request to the GitHub API
                    response = requests.get(url)
                    if response.status_code == 200:
                        issue_data = response.json()
                        title = issue_data['title']
                        issue_state= issue_data['state']
                        creation_date = issue_data['created_at']
                        state_reason = issue_data['state_reason']
                        closed_at = issue_data['closed_at']                        
                    else:
                        print(f"Failed to retrieve issue. Status code: {response.status_code}\n repo link: {url}")
                    
                else: #mainly deals with mobile-android and mobile-ios
                    title = ''
                    creation_date = '' 
                    issue_state = ''
                    state_reason = '' 
                    closed_at = ''

                csv_writer.writerow({'project_name': row['project_name'],
                                     'issue_link': row['issue_link'],
                                     'issue_number': row['issue_number'],
                                     'author': row['author'],
                                     'issue_hci_attributes':row['issue_hci_attributes'],
                                     'Issue_title': title,
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
    input_file = 'cleanedData.csv'
    output_file = 'newOutput.csv'
    columns_to_keep = ['project_name', 'issue_link','issue_number','author','Issue_title','issue_hci_attributes','Created_At','Issue_State','State_Reason','closed_at','body_summary', 'body_text']

    filter_csv(input_file, output_file, columns_to_keep)

if __name__ == "__main__":
    main()

