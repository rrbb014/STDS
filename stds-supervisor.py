import os
import random
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', default='stds-problems.txt', type=str, help='Problem file')
    parser.add_argument('-n', '--number', type=int, default=3, help='Number of problem')
    parser.add_argument('-a', '--all', action='store_true', help='handle all lines')

    args = parser.parse_args()

    with open(args.file, 'r', encoding='utf8') as f:
        problems = [p for p in f.read().split('\n') if p != '']

    num = args.number
    if args.all:
        num = len(problems)

    for _ in range(num):
        p = random.choice(problems)
        problems.remove(p)
        print(p)
