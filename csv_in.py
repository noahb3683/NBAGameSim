import csv

file_locations = []


def csv_reader(file):  # 'C:\\Users\\NWHAL\\Documents\\nba_project\\test_csv_in.csv'
    data = list(csv.reader(open(file)))
    enc = data[0][0].encode("ascii", "ignore")
    dec = enc.decode()
    data[0][0] = dec
    return data


def import_excel():
    [csv_reader(i) for i in file_locations]
