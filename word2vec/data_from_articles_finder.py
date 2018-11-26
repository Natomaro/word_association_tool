import re 

import glob

read_files = glob.glob("*.txt")

my_str = "This is a sentence. <once a day> [twice a day]"
print(re.sub("[<\(\[].*?[\)\]>]", "", my_str))

with open("data_from_articles.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            text=infile.read().decode('utf-8')
            #re.sub(r'\s<>\s', '', '<hi>')
            clean_text = re.sub("[<\(\[].*?[\)\]>]", "", text)
            outfile.write(clean_text.encode())