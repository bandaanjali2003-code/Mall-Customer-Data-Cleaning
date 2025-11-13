 Mall Customer Data Cleaning and Preprocessing
Project Overview

This project focuses on cleaning and preprocessing the Mall Customer Segmentation dataset from Kaggle using Python (Pandas).
The dataset originally contained raw customer data (with inconsistent formatting and potential duplicates).
The objective was to prepare a clean and consistent dataset for further analysis or segmentation tasks.

 Objective

Clean and prepare a raw dataset by handling missing values, duplicates, inconsistent formats, and data-type issues.

 Tools & Libraries

Python 3

Pandas

NumPy

(Optional: Jupyter Notebook / VS Code for running code)

 Dataset Information

Dataset Name: Mall Customer Segmentation Data
Source: Kaggle

Original Columns

Column	Description
CustomerID	Unique ID for each customer
Gender	Male / Female
Age	Age of customer
Annual Income (k$)	Annual income in thousands
Spending Score (1-100)	Customer’s spending score
⚙️ Data Cleaning Steps
Step	Description
1️⃣	Loaded dataset using Pandas (read_csv())
2️⃣	Checked for and confirmed no missing values
3️⃣	Removed duplicate rows with .drop_duplicates()
4️⃣	Standardized text fields – capitalized “Male”, “Female”
5️⃣	Renamed columns to clean format (lowercase, underscores)
6️⃣	Verified and fixed data types (int, object)
7️⃣	Saved cleaned dataset as Cleaned_Mall_Customers.csv
🧾 Cleaned Dataset Summary

Rows: 200

Columns: 5

No missing values or duplicates

Column Names:

['customerid', 'gender', 'age', 'annual_income_k$', 'spending_score_1-100']

 How to Run the Code
# 1. Install dependencies
pip install pandas numpy

# 2. Run the cleaning script
python clean_data.py


 The cleaned file will be generated as Cleaned_Mall_Customers.csv in the same folder.

 Before & After Snapshot
Before Cleaning	After Cleaning
Annual Income (k$)	annual_income_k$
Spending Score (1-100)	spending_score_1-100
Mixed case “male”, “FEMALE”	Standardized “Male”, “Female”
Possible duplicates	Removed
Untidy column names	Clean, uniform names
📸 Screenshots (for GitHub)

Add the following screenshots to your repo’s /screenshots folder:

original_data_preview.png – a screenshot of the first few rows of the raw dataset

cleaning_code.png – your Python code in VS Code or Jupyter

cleaned_data_preview.png – preview of cleaned dataset after running the script

(Attach these images in your README with Markdown syntax, for example:)

![Original Data](screenshots/original_data_preview.png)
![Cleaned Data](screenshots/cleaned_data_preview.png)

 Repository Structure
Mall-Customer-Data-Cleaning/
│
├── Mall_Customers.csv
├── Cleaned_Mall_Customers.csv
├── clean_data.py
├── README.md
└── /screenshots

Learnings

Learned how to use Pandas for data cleaning tasks

Understood handling of missing values, duplicates, and inconsistent data

Practiced column renaming and data-type conversion

Submission

After completing:

Commit all files to your GitHub repo

Copy your repository link (e.g. https://github.com/YourName/Mall-Customer-Data-Cleaning)

Submit it via the official submission form before 10:00 PM