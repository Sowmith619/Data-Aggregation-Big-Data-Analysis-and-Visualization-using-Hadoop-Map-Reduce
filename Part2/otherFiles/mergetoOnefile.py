import glob

read_files = glob.glob("C:/Users/nallu/OneDrive/Documents/Semester2/DataIntensivecomputing/Lab2/cc_all/*.txt")

with open("commoncrawl.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
