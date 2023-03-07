import argparse
import pandas as pd
import chardet

from pathlib import Path

class Financer():

    @staticmethod
    def analyze(file_path: Path):
        if not file_path.is_file():
            raise Exception("error: file does not exist")

        with open(file_path, 'rb') as f:
            enc = chardet.detect(f.read())

        df = pd.read_csv(file_path, sep=';', encoding=enc['encoding'])
        print(df)


def main():
    print("financer v0.1")

    parser = argparse.ArgumentParser(prog='Financer', description='analysis toolset for financial data')
    parser.add_argument("-f", "--filepath", help="filepath to financial data", required=True)
    parser.add_argument("-t", "--type", help="type of input data", default="csv", required=False)    

    args = parser.parse_args()

    file_path = Path(args.filepath)

    Financer.analyze(file_path)
