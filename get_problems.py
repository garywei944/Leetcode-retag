import numpy as np
import pandas as pd
import re

if __name__ == '__main__':
    with open('README.md', 'r', encoding='gbk', errors='ignore') as f:
        file = f.readlines()

    r = []
    for line in file:
        if e := re.match(r'^- \[(\d+)\. .*$', line):
            r.append(int(e.group(1)))

    print(r)

    r = np.random.permutation(r)
    print(r)

    df = pd.DataFrame.from_dict({'id': r})
    print(df)

    df.to_excel('problems.xlsx', index=False)
