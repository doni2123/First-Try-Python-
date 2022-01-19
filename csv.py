import numpy as np

file_path = r"D:\Downloads\username.csv"
with open (file_path, username.csv) as f:
    reader = csv.reader(f, delimiter =';')
    headers = next(reader)
data = list(reader)
data = np.array(data).astype(float)