import os
import random
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', default='stds-problems.txt', type=str, help='Problem file')
    parser.add_argument('-n', '--number', type=int, default=3, help='Number of problem')

    args = parser.parse_args()

    with open(args.file, 'r', encoding='utf8') as f:
        problems = [p for p in f.read().split('\n') if p != '']

    for _ in range(args.number):
        p = random.choice(problems)
        problems.remove(p)
        print(p)