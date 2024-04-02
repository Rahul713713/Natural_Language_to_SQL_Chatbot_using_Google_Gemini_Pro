# Natural Language to SQL Chatbot
Building an end to end natural language to sql converter powered by Google Gemini Pro. 
## Flow Diagram for NL2SQL
![NL2SQL_Chatbot](https://github.com/Rahul713713/Natural_Language_to_SQL_Chatbot_using_Google_Gemini_Pro/blob/main/images/Natural_Language_to_SQL_Flow_Diagram.png "NL2SQL Chabot using Google Gemini Pro and Langchain")
- Created multiple charts,graphs,countplots,etc. in order to understand how to minimise the risk of losing money while lending to customers.
- Worked on a dataset consisting of 614 rows of data for 12 different features.
- Performed univariate analysis as well as multivariate analysis on various features to understand the importance of every feature.
- Used EDA to understand how consumer attributes and different features help us in identifying customers who are eligible for a loan from customers who are not.
## Schema for Chinook Database
![Database_Schema](https://github.com/Rahul713713/Natural_Language_to_SQL_Chatbot_using_Google_Gemini_Pro/blob/main/images/sqlite-sample-database.jpg "Database Schema")

# Problem Statement
Predicting whether an applicant is eligible for the loan that he/she has applied for based on multiple independent variables and Machine Learning. This will help the company in automating the process of checking the eligibility of the applicant for the loan.Now,when a customer applies for a loan, the company has to make a decision whether to approve the loan or not based on the applicant's profile. 

The data that I have contains information about applicants and their Gender,Education,Self_Employed,ApplicantIncome,etc. and whether they are eligible for the loan or not.

# Code and Resources Used
- Packages: pandas, numpy, matplotlib, seaborn, scikit-learn

# Data Cleaning and Preprocessing
## After reading the data, I needed to clean it up so that it would be fit for our data analysis. I made the following changes and created the following variables:
- Checked whether we have missing data for various columns.
- Some columns had missing values. So, I replaced them accordingly with the median value of the column for the numerical columns. For categorical columns, I replaced the missing values with the most repeating values with respect to the output class. 
- Performed Data Standardisation to get the data on the same scale with the mean of 0 and standard deviation of 1.
- Finally,the columns used for EDA are

 1   Loan_ID             
 2   Gender              
 3   Married             
 4   Dependents          
 5   Education           
 6   Self_Employed       
 7   ApplicantIncome     
 8   CoapplicantIncome  
 9   LoanAmount         
 10  Loan_Amount_Term   
 11  Credit_History     
 12  Property_Area       
 13  Loan_Status        

# EDA
After cleaning the data,I started with EDA. These are some of the outcomes of EDA 

![loan_status](https://github.com/Rahul713713/Loan_Status_Prediction/blob/main/loan_eligibilty_based_on_credit_history.png "loan_eligibilty_based_on_credit_history")
![loan_status](https://github.com/Rahul713713/Loan_Status_Prediction/blob/main/loan_eligibilty_based_on_education.png "loan_eligibilty_based_on_education")
![loan_status](https://github.com/Rahul713713/Loan_Status_Prediction/blob/main/most_important_features.png "most_important_features")

# Machine Learning Models
- The Machine Learning Models that I've used are as follow:

 1   Naive Bayes             
 2   K Nearest Neighbors              
 3   Logistic Regression - Without Class Balancing             
 4   Logistic Regression - With Class Balancing          
 5   Linear SVC           
 6   SVC With Rbf Kernel      
 7   Random Forest  

# Result
    +--------------------------------------------------------------------------------+
    |           *** Model Summary *** [Performance Metric: Accuracy Score]           |
    +-----------------------------------------------+----------------+---------------+
    |                   Model Name                  | Train Accuracy | Test Accuracy |
    +-----------------------------------------------+----------------+---------------+
    |                  Naive Bayes                  |     0.794      |     0.817     |
    |              K Nearest Neighbors              |     0.836      |      0.8      |
    | Logistic Regression - Without Class Balancing |     0.807      |     0.817     |
    |   Logistic Regression - With Class Balancing  |     0.801      |     0.808     |
    |                   Linear SVC                  |     0.807      |     0.808     |
    |              SVC With Rbf Kernel              |     0.824      |     0.808     |
    |                 Random Forest                 |     0.817      |     0.808     |
    +-----------------------------------------------+----------------+---------------+
