from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow
import pandas as pd

# Num rows
num_rows = 10**6
batch_size = 250

# Load data
in_dir = "/home/viren/Thesis/MixedNormalAttack/attack_normal_mix0.csv"


def generate_arrays_from_file(path, batchsize):
    inputs = []
    targets = []
    batchcount = 0
    while True:
        with open(path) as f:
            next(f)
            for line in f:
                csvline = line.split(',')
                inputs.append(csvline[5 :-1])
                if csvline[-1] == "True":
                    targets.append(1)
                else:
                    targets.append(0)
                batchcount += 1
                if batchcount > batchsize:
                  X = np.array(inputs, dtype='float32')
                  y = np.array(targets, dtype='bool')
                  yield (X, y)
                  inputs = []
                  targets = []
                  batchcount = 0

# Create the model
model = Sequential()
model.add(Dense(16, input_dim=93, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mean_absolute_error',
              optimizer=tensorflow.keras.optimizers.Adam(),
              metrics=['mean_squared_error'])

# Fit data to model
model.fit(generate_arrays_from_file(in_dir, batch_size),
                    steps_per_epoch=num_rows / batch_size, epochs=10)

# df = pd.read_csv(in_dir)
# cols = df.columns
# print(len(cols))