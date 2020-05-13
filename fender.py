import csv
import xml.etree.ElementTree as ET
import os, re


def main():

    with open('fenderTEST.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        spamwriter.writerow(['Amplifier', 'Name', 'Author', 'Rating'])

        for f in os.listdir('.'):
          if re.match('preset', f):
            tree = ET.parse(f)
            root = tree.getroot()       
            for fuse in root.findall('FUSE'):
                name = fuse.find('Info').attrib['name']
                author = fuse.find('Info').attrib['author']
                rating = fuse.find('Info').attrib['rating']
            spamwriter.writerow([root.attrib['amplifier'], name, author, rating])
   
if __name__ == "__main__":
    main();