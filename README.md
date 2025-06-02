# Task-1---Data-cleaning-and-Preprocessing


Overview
This project is part of a Data Analyst Internship assignment focused on cleaning and preprocessing a raw dataset using Python and Pandas. The main goal was to make the dataset analysis-ready by addressing missing values, duplicates, inconsistent data formats, and column naming issues.

Tools Used
- Python 3.x
- Pandas
- Visual Studio Code (VS Code) / Jupyter Notebook

 Dataset
- *Original File Name*: netflix_titles.csv
- *Source*: [Kaggle - Netflix Movies and TV Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Cleaning Steps Performed
- Loaded the dataset using pandas.read_csv()
- Identified missing values and filled them with "Unknown"
- Removed exact duplicate records
- Standardized column names:
  - All lowercase
  - Replaced spaces with underscores
  - Removed leading/trailing whitespaces
- Standardized values in columns like gender and country
- Reformatted the date_added column to dd-mm-yyyy
- Converted data types:
  - age, release_year to integer
  - price to float (if present)
  - gender to categorical
- Saved the final cleaned dataset as finals_clean.csv

Output
- Cleaned dataset: finals_clean.csv
- Python script used: cleaning_script.py

Summary
Through this task, essential data preprocessing techniques were applied to ensure the dataset is consistent, clean, and structured for further analysis. These foundational skills are critical for any data analyst working with real-world datasets.

---

Feel free to explore the cleaning_script.py file to see the exact logic used for cleaning and transforming the dataset.
