import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("note.csv")

# Select features and target
ore = df.iloc[:, 0:1]  # Ensure 'ore' is a DataFrame
note = df["Note"]      # 'note' is a Series

# Initialize the model
model = LinearRegression()

# Fit the model
model.fit(ore, note)

# Predict using the model
note_prezise = model.predict(ore)

# Plot the data
plt.scatter(ore, note, label="Actual Notes")
plt.plot(ore, note_prezise, color='red', label="Predicted Notes")

# Show the plot with labels
plt.xlabel("Hours Studied")
plt.ylabel("Notes")
plt.legend()
plt.show()

# Predict for 7 hours studied
prediction_for_7 = model.predict([[7]])
print(f"Predicted note for 7 hours studied: {prediction_for_7[0]}")
