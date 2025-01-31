import pandas as pd

# Step 2: Upload the CSV file

from google.colab import files

uploaded = files.upload()

# Step 3: Read the uploaded CSV file

# Replace 'your_file.csv' with the actual file name after upload

file_name = list(uploaded.keys())[0]  # Automatically gets the uploaded file name

df = pd.read_csv(file_name)