import csv
import xml.etree.ElementTree as ET
import os, re

def main():

    with open((os.path.basename(os.getcwd())+'.csv'), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        spamwriter.writerow(['Amplifier', 'Name', 'Author', 'Rating', 'Tags', 'Filename', 'Info'])
        passed = 0
        failed = 0

        for f in os.listdir('.'):
          if f.endswith(".fuse"):
            try:
                tree = ET.parse(f)
                root = tree.getroot()       
                for fuse in root.findall('FUSE'):
                    name = fuse.find('Info').attrib['name']
                    author = fuse.find('Info').attrib['author']
                    tags = fuse.find('Info').attrib['tags']
                    rating = fuse.find('Info').attrib['rating']
                    info = fuse.find('Info').text
                    
                spamwriter.writerow([root.attrib['amplifier'], name, author, rating, tags, f, info])
                passed+=1
            except:
                failed+=1
                pass

    print(passed , " files processed, " , failed ,  "  files failed.")
   
if __name__ == "__main__":
    main()