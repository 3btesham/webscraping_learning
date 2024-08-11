from bs4 import BeautifulSoup

with open('index.html', 'r') as test_file: #reads index.html and saves it as test file var
    content = test_file.read() #reading html file content
    
    soup = BeautifulSoup(content, 'lxml') #applies the Beautiful parser method of lxml to the content of the html file
    #print(soup.prettify()) prettify makes the content of the soup var more readable and easier to look at
    
    #first_tag = soup.find('h2') finds first html line with h2 tag
    #food_type_tags = soup.find_all('h2') finds ALL html lines with h2 tag and stores them in a list of lines
    
    #for ft in food_type_tags: goes through each foodtype tag in the list of tags
    #    print(ft.text) prints the text of the tag
    
    menu_items = soup.find_all('article', class_='item') #finds all article tags with a class of item, add underscore after class because python has a built in class var
    for item in menu_items:
        #print(item.p) prints first p tag nested inside of the article tags
        flavors = item.find_all('p', class_='flavor') #finds all flavors of coffee
        price = item.find_all('p', class_='price') #finds all prices of flavors
        
        print(f'{flavors[0].text} costs {price[0].text}')
        
        
#to see webpage source code, right click and press inspect element to see all the parts of the html file
#source code gets a lot more complex with online websites
