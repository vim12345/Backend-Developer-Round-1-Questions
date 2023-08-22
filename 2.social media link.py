import requests
from bs4 import BeautifulSoup
import re

def get_website_details(url):
    # Send a GET request to the given URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find social links
        social_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.search(r'facebook|linkedin', href):
                social_links.append(href)
        
        # Find email addresses
        email_addresses = []
        email_pattern = r'\S+@\S+'
        email_matches = re.findall(email_pattern, response.text)
        email_addresses.extend(email_matches)
        
        # Find contact numbers
        contact_numbers = []
        contact_pattern = r'\+\d+\s\d+\s\d+\s\d+'
        contact_matches = re.findall(contact_pattern, response.text)
        contact_numbers.extend(contact_matches)
        
        return social_links, email_addresses, contact_numbers
    else:
        print("Failed to fetch the website.")
        return [], [], []

# Take user input for the website URL
website_url = input("Enter the website URL: ")

# Get details from the website
social_links, email_addresses, contact_numbers = get_website_details(website_url)

# Print the extracted details
print("Social links:")
for link in social_links:
    print(link)

print("\nEmail addresses:")
for email in email_addresses:
    print(email)

print("\nContact numbers:")
for contact in contact_numbers:
    print(contact)
