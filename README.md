# Natural Language to SQL Chatbot using Google Gemini Pro
Building an end to end natural language to sql converter powered by Google Gemini Pro and Langchain. 
## Flow Diagram for NL2SQL
![NL2SQL_Chatbot](https://github.com/Rahul713713/Natural_Language_to_SQL_Chatbot_using_Google_Gemini_Pro/blob/main/images/Natural_Language_to_SQL_Flow_Diagram.png "NL2SQL Chabot using Google Gemini Pro and Langchain")
- Used an open source model called Google Gemini pro along with the Langchain Library to build a product that can be used to chat with the connected database.
- Built the solution in two parts where the first part is to see if we can create a sql query from text, execute the query and get the answer back in a human readable format using Lagnchain and Google Gemini Pro on Colab and then created a production ready codebase using streamlit and python for the same solution. 
- **This application is very useful for individuals who are not trained to work with SQL commands but would like to interact with the database to get insights With the help of our application, they don't have to orry about wtiting sql commands now as they can jsut type the question in natural language and they will get the answer in a readable format.** 
## Schema for Chinook Database
![Database_Schema](https://github.com/Rahul713713/Natural_Language_to_SQL_Chatbot_using_Google_Gemini_Pro/blob/main/images/sqlite-sample-database.jpg "Database Schema")
- Please refer the above schema while interacting with the Natural Language to SQL Chatbot. 

# Problem Statement
### The Solution is built in two parts to give a complete undestanding of building an end to end project from stratch to deploying it to production. 
#### Part 1: Build a solution using Mistral 7B LLM based on RAG methodology to interact with PDF's on Goggle Colab
The objective here is use the Google Gemini Pro Model to convert text-to-SQL code, use Langchain to execute the generated query and give a human readable response using Langcahina and Gemini Pro. 

### Part 2: Build an end to end Chatbot using Google Gemini Pro and Streamlit to interact with the database on the local system. 
Build Chatbot from scratch that can chat with SQL Database including memory & history on your local laptop using Google Gemini Pro, LangChain, SQLite Database, Python, Streamlit and VS Code.

# Models and Libraries used
- Libraries: python, langchain,langchain-community, langchain_experimental, google-generativeai, langchain-google-genai, streamlit, etc.
- Model: Google Gemini Pro

# Important resources
- Google Gemini API Key Link - https://makersuite.google.com/app/apikey
