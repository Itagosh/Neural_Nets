# -*- coding: utf-8 -*-
"""Kan_Perdictions_Simple.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tnjOMPtcO0d0fqh9csI0x5bu2WJ7Uc2F
"""

#KAN Perdictions of -x^4 +17x^3 -5x^2 + cos(x-3) - 334
from kan import KAN, create_dataset
import numpy as np
import torch
import matplotlib.pyplot as plt

def actual_func(x):
    return -x ** 4 + 17*x **3 - 5*x**2 + torch.cos(x+3)  - 334

kan_model = KAN(width=[1, 16, 16, 1], grid=10, k=3)

f = lambda x: -x ** 4 + 17*x **3 - 5*x**2 + torch.cos(x+3)  - 334

train_x = torch.tensor([[x] for x in np.linspace(-5, 5, 500)], dtype=torch.float32)
train_y = f(train_x)
dataset = {'train_input': train_x, 'train_label': train_y,
           'test_input': train_x, 'test_label': train_y}

kan_model.train(dataset, opt='LBFGS', steps=200, log=100)

x_values = torch.tensor([[x] for x in np.linspace(-5, 5, 300)], dtype=torch.float32)

with torch.no_grad():
    y_predicted = kan_model.forward(x_values).squeeze().numpy()

y_actual = actual_func(x_values.squeeze()).numpy()

plt.figure(figsize=(8, 6))
plt.plot(x_values.numpy(), y_actual, label='Actual', color='blue')
plt.plot(x_values.numpy(), y_predicted, label='Predicted', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Prediction using KAN')
plt.grid(True)
plt.legend()
plt.show()

