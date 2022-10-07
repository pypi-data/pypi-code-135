import sys
from argparse import ArgumentParser

from pandas import read_csv 
from numpy import split

class CustomParser(ArgumentParser):

    def error(self, message: str):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def split_csv_dataset(csv_path: str, split_info: tuple[int,int,int]):
    assert len(split_info) == 3, f'split_info {split_info} must contain 3 elements'
    assert sum(split_info) == 100, f'Splits must sum to 100, not {sum(split_info)}'
    df = read_csv(csv_path)

    train, validation, test = split(df.sample(frac=1, random_state=42), [int((split_info[0]/100.0)*len(df)), int((1.0-(split_info[2]/100.0))*len(df))])
    assert sum([
        len(train), len(validation), len(test)
    ]) == len(df), 'Splits must sum to size of original dataset'
    return train, validation, test

def main():
    parser = CustomParser()
    parser.add_argument('-i', '--input', required=True, help='Path to csv file to split')
    parser.add_argument('-s', '--split', nargs='+', required=True, help='Percentages to split into TRAIN, VALIDATION and TEST (in that order)')
    args = parser.parse_args()

    train, validation, test = split_csv_dataset(args.input,  tuple(map(int,args.split)))
    train.to_csv(f'{args.input[:-4]}_train_{args.split[0]}.csv', index=False)
    validation.to_csv(f'{args.input[:-4]}_validation_{args.split[1]}.csv', index=False)
    test.to_csv(f'{args.input[:-4]}_test_{args.split[2]}.csv', index=False)

    print(f'Finished splitting {args.input} into three csvs containing {args.split} percent of the original')