#%%
import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
# from tensorflow import keras
keras = tf.keras
from keras import layers
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

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

model.fit(x=scaled_train_samples, y=train_lables, validation_split=0.1, batch_size=10, epochs=30, shuffle=True, verbose=2)

#%%
test_lables = []
test_samples = []
for i in range(50):
    # 5% of younder people who had side effects
    random_younger = randint(13, 64)
    test_samples.append(random_younger)
    test_lables.append(1)
    
    # 5 of older people who did not have side effects
    random_older = randint(65, 100)
    test_samples.append(random_older)
    test_lables.append(0)

for i in range(1000):
    # 5% of younder people who did not have side effects
    random_younger = randint(13, 64)
    test_samples.append(random_younger)
    test_lables.append(0)
    
    # 5 of older people who have side effects
    random_older = randint(65, 100)
    test_samples.append(random_older)
    test_lables.append(1)

test_lables = np.array(train_lables)
test_samples = np.array(train_samples)
test_lables, test_samples = shuffle(train_lables, train_samples)

scaled_test_samples = scaler.fit_transform(test_samples.reshape(-1,1))
# %% Predict

predictiions = model.predict(x=scaled_test_samples, batch_size=10, verbose=1)

# %%
for p in  predictiions:
    print(p)

# %%
rounded_predicts = np.argmax(predictiions, axis=-1)
print(rounded_predicts)

# %%
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import itertools
import matplotlib.pyplot as plt

# %% 
cm = confusion_matrix(y_true=test_lables, y_pred=rounded_predicts)
print(cm)

#%%
cm_plot_lables = ['no_side_effects', 'had_side_effects']
disp = ConfusionMatrixDisplay(cm, display_labels=cm_plot_lables)
disp.plot()

# %% Save Model
model.summary()

# %%
import os.path
if os.path.isfile('models/med_trial_model.h5') is False:
    model.save('models/med_trial_model.h5')
    
# %%
from keras.models import load_model
new_model = load_model('models/med_trial_model.h5')

# %%
print(new_model.summary())
print(new_model.get_weights())
print(new_model.optimizer)
# %% JSON 

json_str = model.to_json()
# %%
json_str
# %%
from keras.models import model_from_json
model_arch = model_from_json(json_str)
print(model_arch.summary())

# %%
if os.path.isfile('models/med_trial_model_weights.h5') is False:
    model.save_weights('models/med_trial_model_weights.h5')
# %%
model2 = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])
# %%
model2.load_weights('models/med_trial_model_weights.h5')
# %%
model2.get_weights()
# %%
from keras.utils.vis_utils import plot_model
plot_model(model, to_file='models/model_plot.png', show_shapes=True, show_layer_names=True)
# %%
