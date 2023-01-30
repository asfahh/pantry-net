from bs4 import BeautifulSoup
with open( r"C:\Users\hafso\OneDrive\Archive\Documents\URS\pantry.html",'r') as f:

    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

# Get the text of the first paragraph
# Print the text of each paragraph

divs = soup.findAll(class_= 'item')
for div in divs:
    paragraphs = div.find_all("p")
    addresses= div.find_all('address')
    for p in paragraphs:
        print(p.text,end=',')
    for a in addresses:
        print(a.text)
