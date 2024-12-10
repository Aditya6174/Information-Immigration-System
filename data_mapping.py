import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Path to the CSV file on the desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'process_audit.csv')

# Try to load the dataset
try:
    process_audit = pd.read_csv(file_path)
    print("File loaded successfully.")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please check the file location and try again.")
    exit()

# Display the first few rows of the dataset to understand its structure
print(process_audit.head())

# Assuming the CSV has columns 'x', 'y1', and 'y2'
if 'x' not in process_audit.columns or 'y1' not in process_audit.columns or 'y2' not in process_audit.columns:
    print("The dataset does not contain the required columns 'x', 'y1', and 'y2'. Please check the dataset.")
    exit()

# Overlay Line Graphs
plt.figure(figsize=(10, 5))
plt.plot(process_audit['x'], process_audit['y1'], label='Dataset 1', color='blue')
plt.plot(process_audit['x'], process_audit['y2'], label='Dataset 2', color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Overlay Line Graphs')
plt.legend()
plt.grid(True)
plt.show()

# Dual Axis Plot
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()
sns.lineplot(data=process_audit, x='x', y='y1', ax=ax1, label='Dataset 1', color='blue')
sns.lineplot(data=process_audit, x='x', y='y2', ax=ax2, label='Dataset 2', color='red')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y1-axis', color='blue')
ax2.set_ylabel('Y2-axis', color='red')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Dual Axis Line Graph')
plt.grid(True)
plt.show()
