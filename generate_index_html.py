
import os
import pandas as pd

html_path = "D:\\Git\\GolferChen.github.io\\index2.html"
writer = open(html_path, "w")
writer.write("<!DOCTYPE html>" + "\n")
writer.write("<html>" + "\n")
writer.write("<head>" + "\n")
writer.write("    <title>audios</title>" + "\n")
writer.write("</head>" + "\n")
writer.write("<body>" + "\n")

exper1_csv = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\exper1.csv"
data = pd.read_csv(exper1_csv)
for i in range(len(data)):
    url = data.ix[i, 0]
    item = "    <embed src='" + url + "'/>\n"
    writer.write(item)

exper3_csv = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\exper3.csv"
data = pd.read_csv(exper3_csv)
for i in range(len(data)):
    url = data.ix[i, 0]
    item = "    <embed src='" + url + "'/>\n"
    writer.write(item)

    url = data.ix[i, 1]
    item = "    <embed src='" + url + "'/>\n"
    writer.write(item)

writer.write("</body>" + "\n")
writer.write("</html>" + "\n")

