"""Reproduce the baseline ANN. Run in Google Colab with Stage 2 CSVs available.
Note: Stage 2 preprocessing artifacts must be retained for future inference.
"""
from pathlib import Path
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

ROOT = Path('/content/drive/MyDrive/ACS')
DATA = ROOT / 'Data_Preparation'
OUT = ROOT / 'Predictive_Modeling'
OUT.mkdir(parents=True, exist_ok=True)
tf.keras.utils.set_random_seed(42)
train = pd.read_csv(DATA / 'training_set_preprocessed.csv')
test = pd.read_csv(DATA / 'testing_set_preprocessed.csv')
X_train = train.drop(columns=['Churn']).astype('float32')
y_train = train['Churn'].astype('float32')
X_test = test.drop(columns=['Churn']).astype('float32')
y_test = test['Churn'].astype('float32')
assert X_train.columns.equals(X_test.columns)
X_fit, X_val, y_fit, y_val = train_test_split(X_train,y_train,test_size=.2,random_state=42,stratify=y_train)
model = Sequential([Input(shape=(X_train.shape[1],)),Dense(64,activation='relu'),Dropout(.30),Dense(32,activation='relu'),Dropout(.20),Dense(1,activation='sigmoid')])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=.001),loss='binary_crossentropy',metrics=['accuracy',tf.keras.metrics.AUC(name='auc')])
history = model.fit(X_fit,y_fit,validation_data=(X_val,y_val),epochs=100,batch_size=32,callbacks=[EarlyStopping(monitor='val_loss',patience=10,restore_best_weights=True)],verbose=1)
model.save(OUT / 'trained_ann_model.keras')
pd.DataFrame(history.history).to_csv(OUT / 'ANN_Training_History.csv',index=False)
print('Saved:', OUT / 'trained_ann_model.keras')
