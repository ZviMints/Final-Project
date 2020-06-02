import numpy as np
import keras as ks
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD
import tensorflow as tf
from matplotlib import pyplot as plt

def convert2float(x):
    if x == 'N' or x == 'R' or x == '?':
        return x
    else:
        return float(x)

def extractData():
    data = open("wpbc.data", 'r')
    list_of_data = []
    for line in data:
        curr_example = list(map(convert2float, line.strip().split(",")))
        del curr_example[2]
        del curr_example[0]
        list_of_data.append(curr_example)

    # HandleNullFeature
    return list(filter((lambda e: not ('?' in e)), list_of_data))

def normalization(data):
    max_feature = [0 for _ in range(len(data[0]) - 1)]
    for example in data:
        for i in range(len(max_feature)):
            max_feature[i] = max(max_feature[i], example[i + 1])
    for example in data:
        for i in range(len(max_feature)):
            example[i + 1] = example[i + 1] / max_feature[i]
    return data

def getBalanceDate(data):
    BalanceData = list()
    for example in data:
        if 'R' in example:
            BalanceData.append([f for f in example])
            BalanceData.append([f for f in example])
            BalanceData.append([f for f in example])
        else:
            BalanceData.append([f for f in example])
    return BalanceData

def devideDataToTrainAndTest(data, mode):
    if mode == 3:
        second_devide_index = int(len(data) * (66.666 / 100))
        train = data[:second_devide_index]
        test = data[second_devide_index:]

    elif mode == 2:
        first_devide_index = int(len(data) * (33.333 / 100))
        second_devide_index = int(len(data) * (66.666 / 100))
        test = data[first_devide_index:second_devide_index:]
        del data[first_devide_index:second_devide_index:]
        train = data

    else:
        first_devide_index = int(len(data) * (33.333 / 100))
        test = data[:first_devide_index]
        train = data[first_devide_index:]

    return train, test

def devideDataToFeaturesAndOutcome(data):
    y = []
    for example in data:
        y.append(0 if (example[0] == "N") else 1)  # the Outcome (R = recur = 1, N = nonrecur = 0)
        del example[0]
    return data, np.array(y)

if __name__== '__main__':
    # preparing the data
    Data = extractData()
    # normalization
    normalize_data = normalization(Data)

    # balance the dataset by over-sampling method
    balance_data = getBalanceDate(normalize_data)

    # devide data into train and test
    data_train, data_test = devideDataToTrainAndTest(balance_data, 66.666)

    # devide into features and outcome
    data_x_train, data_y_train = devideDataToFeaturesAndOutcome(data_train)
    data_x_test, data_y_test = devideDataToFeaturesAndOutcome(data_test)

    model = Sequential()
    model.add(Dense(1, activation='sigmoid', input_shape=(32,)))
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate=1e-2,
        decay_steps=100,
        decay_rate=0.1)
    optimizer= ks.optimizers.SGD(lr= 0.00001)
    model.compile(optimizer=optimizer , loss='binary_crossentropy', metrics=['accuracy'])
    #80/20 accuracy 0.71-0.72 for 10000 epochs smooth loss 0.54 fixed rate at a=0.01
    #66/34 accuracy 0.72 for 10000 epoch loss 0.54 fixed rate at a=0.01
    #60/40 accuracy 0.71 for 10000 epoch loss 0.54 fixed rate at a=0.01
    #0.7225 at a=0.01 loss 0.65
    #0.7435 at a=0.1 loss 0.48
    #80/20 0.73 at a=0.1 same loss
    #same
    x_tr = np.array(data_x_train)
    x_te = np.array(data_x_test)
    y_tr = np.array(data_y_train)
    y_te = np.array(data_y_test)
    epochs=10000
    history_ = model.fit(x_tr,y_tr, epochs=epochs,validation_data=(x_te,y_te))
    #y_prd = model.predict(x_te, batch_size=10, verbose=0)
    scores=model.evaluate(x_te,y_te, verbose=1)
    print("Accuracy: %.2f%%" % (scores[1]*100))
    acc = history_.history['accuracy']
    val_acc = history_.history['val_accuracy']
    loss = history_.history['loss']
    val_loss = history_.history['val_loss']
    epochs_range = range(epochs)
    plt.figure(figsize=(8,8))
   # plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Test Accuracy')
    plt.title('Training and Test Accuracy')
    plt.show()
