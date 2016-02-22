import csv, sys
from configparser import ConfigParser

config = ConfigParser()
config.read('picLab.ini')
dataset_thumbs = (config.get('CSV', 'csv_file'))


def count_img_in_csv(filename):
    counter = 0
    with open(dataset_thumbs, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            counter = counter + 1
    return counter


def write_pic(r,b,g,pic):
    with open(dataset_thumbs, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([r, b, g, pic])


def read_csv():
    with open(dataset_thumbs, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        try:
            for row in reader:
                print (row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (dataset_thumbs, reader.line_num, e))


def load_dataset_in_matrix():
    m = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
    with open(dataset_thumbs, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if m[int(row[0])][int(row[1])][int(row[2])]:
                m[int(row[0])][int(row[1])][int(row[2])] += ','+row[3]
            else:
                m[int(row[0])][int(row[1])][int(row[2])] = row[3]
    return m

