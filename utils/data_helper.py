import pandas as pd


def read_data(file_path):
    data = pd.read_csv(file_path)
    return data


def test():
    path = '../data/aaa.csv'
    data = read_data(path)
    print data
    print data.keys()

if __name__ == "__main__":
    test()
