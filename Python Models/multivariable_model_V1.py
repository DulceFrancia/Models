# -*- coding: utf-8 -*-
"""Multivariable_Model_V1.ipynb"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos_df_1.csv')
df.head()

df.shape

df.describe()

# Search for outliers
# Visualize temp information on plot scatters
plt.figure(figsize=(10,7))
# Plot temperature data
plt.scatter(df['Index'], df['Body Temp'], c='b', s=4, label="Body Temperature")
# Plot title
plt.title("Body Temperature")
# Show the plot
plt.show()

# Search for outliers
plt.figure(figsize=(10,7))
# Plot temperature data
plt.scatter(df['Index'], df['Room Temp'], c='g', s=4, label="Environmental Temperature")
# Plot title
plt.title("Environmental Temperature")
# Show the plot
plt.show()

# Search for outliers
plt.figure(figsize=(10,7))
# Plot temperature data
plt.scatter(df['Index'], df['Pressure'], c='y', s=4, label="Pressure")
# Plot title
plt.title("Pressure")
# Show the plot
plt.show()

# Look for missing data
df.info()

# Add pytorch attributes
import torch
from torch import nn

# Prepare data
X1_seg = df['Body Temp'].to_numpy()
X2_seg = df['Room Temp'].to_numpy()
X3_seg = df['Pressure'].to_numpy()
X1_seg[:5], X2_seg[:5], X3_seg[:5]

# We already now it's a float64
X1_seg.dtype, X2_seg.dtype, X3_seg.dtype

# Convert to tensors
X1_tensor = torch.from_numpy(X1_seg).unsqueeze(dim=1)
X2_tensor = torch.from_numpy(X2_seg).unsqueeze(dim=1)
X3_tensor = torch.from_numpy(X3_seg).unsqueeze(dim=1)

X1_tensor[:5], X2_tensor[:5], X3_tensor[:5]

# Interchange and simplify float format
X1 = X1_tensor.type(torch.float32)
X2 = X2_tensor.type(torch.float32)
X3 = X3_tensor.type(torch.float32)

X1.dtype, X2.dtype, X3.dtype

# Set weights and bias
weight = torch.tensor([[3.0],
                  [4.0],
                  [2.0]],
                 requires_grad=True)
bias = torch.tensor([[1.0]],
                    requires_grad=True)

weight.shape

# Define a forward function for y_preds
def forward_y(x):
  y_pred = torch.mm(x, weight) + bias
  return y_pred

# Convert tensor into a unique [3, 1] shape for three variables
new_tensor = torch.tensor([[X1[0], X2[0], X3[0]]])
new_tensor

new_tensor.shape

# Convert all tensors to  [1, 3] shape
X_preview = []
for i in range(200):
  tens = torch.tensor([[X1[i], X2[i], X3[i]]])
  X_preview.append(tens)

X = torch.stack(X_preview)
X[:5]

X[0]

# Making predictions for Multi-Dimensional tensor "X"
y_pred = forward_y(X[0])
print(f"Prediction for  first 'X' tensor: {y_pred}")

"""Conclusion. This model can be used only if we know an output value, such as asigning a value by answering a question. For example, this data behaviour could answer: *how is the body gonna react to personal and environmental conditions?*

However, this model is not complete because we're looking for body behaviour, external influence in the body, routines and activities.

There should be many models to answer all this questions and many variables they should depend on, such as:
1. Heart rate
2. SpO2 lecture
3. Daily activities: sleep, activity, rest, etc.
"""