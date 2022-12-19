import csv
import os
import re

files = []
filenames = []
for file in os.listdir(os.getcwd()):
        if (re.search(".log", file) != None):
            with open(file, "r") as f:
                data = f.readlines()
            data = [file.removeprefix("model").removesuffix(".log").replace("_", " ")] + [line[11:15].replace("%", "0").replace(".", ",") for line in data if line.__contains__("Accuracy")]
            files.append(data)

print(*files, sep="\n")

# with open("data.csv", 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, dialect="excel", delimiter=";")
#     csvwriter.writerows(files)