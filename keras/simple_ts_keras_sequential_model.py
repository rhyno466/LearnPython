#%%
import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy

#%%
train_lables = []
train_samples = []

#%%
for i in range(50):
    # 5% of younder people who had side effects
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_lables.append(1)
    
    # 5 of older people who did not have side effects
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_lables.append(0)

for i in range(1000):
    # 5% of younder people who did not have side effects
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_lables.append(0)
    
    # 5 of older people who have side effects
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_lables.append(1)

#%% 
for i in train_samples:
    print(i)

for i in train_lables:
    print(i)
    
# %%

train_lables = np.array(train_lables)
train_samples = np.array(train_samples)
train_lables, train_samples = shuffle(train_lables, train_samples)

#%%
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1,1))

# %%

for i in scaled_train_samples:
    print(i)
# %%

#%%
model = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])

# %%
model.summary()

# %%
model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# %%

model.fit(x=scaled_train_samples, y=train_lables, batch_size=10, epochs=50, shuffle=True, verbose=2)
# %%
