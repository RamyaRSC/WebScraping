from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>') # Get the input from the user
print(f'Filtering out {unfamiliar_skill}') # Print the input from the user

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs): # Enumerate the jobs list to get the index and the job itself - job is a tag
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '') # Replace - Remove the spaces
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills: # If the unfamiliar skill is not in the skills
                with open(f'posts/{index}.txt', 'w') as f: # Open a file with the index as the name
                    f.write(f"Company Name: {company_name.strip()}\n") # Write the company name
                    f.write(f"Required Skills: {skills.strip()}\n") # Write the skills
                    f.write(f"More Info: {more_info}\n") # Write the more info

                print(f'File saved: {index}') # Print the index of the job

if __name__ == '__main__': # If the script is run directly
    while True: # Run the script forever
        find_jobs() # Call the function
        time_wait = 10  # Wait 10 minutes
        print(f'Waiting {time_wait} minutes...') # Print the waiting time
        time.sleep(time_wait * 60) # Wait for the time_wait in seconds