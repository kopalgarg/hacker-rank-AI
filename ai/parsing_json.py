import pandas as pd 
import json
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

num_lines = int(input())
inputs = [json.loads(input()) for _ in range(num_lines)]
test_df = pd.DataFrame(inputs).fillna(0)
with open('training.json') as f:
    data = [json.loads(line) for line in f]
    data.remove(data[0])
    train_df = pd.DataFrame(data).fillna(0)

test_df = test_df.drop(columns=['serial'])
train_df = train_df.drop(columns=['serial'])
missing_cols = list(train_df.columns.difference(test_df.columns))

if len(missing_cols) > 1:
    zeros = [0 for i in range(len(test_df))]
    for c in missing_cols:
        train_df[c] = zeros

X_train = train_df[['Physics','Chemistry','PhysicalEducation','English','Biology','Accountancy','BusinessStudies','Economics','ComputerScience']]
Y_train = train_df['Mathematics']

model = LDA()
X_train = model.fit(X_train.to_numpy(), Y_train.values.ravel())
X_test = test_df.to_numpy()

out = model.predict(X_test)
for i in out:
    print(i)

