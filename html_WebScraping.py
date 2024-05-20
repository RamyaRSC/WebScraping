from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read() # Read the content of the file
    
    soup = BeautifulSoup(content, 'lxml') # Parse the content of the file
    # tags = soup.find('h5') # Find the first h5 tag in the file
    courses_html_tags = soup.find_all('h5') # Find all the h5 tags in the file
    # for course in courses_html_tags:
        # print(course.text) # Print the text of the h5 tags

    course_cards = soup.find_all('div', class_='card') # Find all the div tags with the class card
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}') # Print the course name and price