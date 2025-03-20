# Expense Management System

I have been concerned about well being at retirement for young people for sometime. Today the norm is that individuals can change their financial habits if presented with facts (rather than telling them what to do with their life).
I start from calculating how much money a person (to live) would need post-retirement. This is based on the well-established notion that the annual cost outlay must be 4% of the retirement savings corpus.
This is available in my short substack article:
 - ***Calculating your FI number*** : https://ittalktoomuch24.substack.com/p/calculating-your-financial-independence


Some other articles that probably go hand-in-hand:
- ***Destruction of savings*** : https://ittalktoomuch24.substack.com/p/capital-flight-destruction-of-personal
- ***Thoughts on Financial independence if you're scared*** https://ittalktoomuch24.substack.com/p/financial-independence-what-if-youre
- ***The connection between self-belief and wealth creation***: https://ittalktoomuch24.substack.com/p/self-belief-and-wealth-creation


This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.
Its primary intention is to enable the use of expense habits analytics to drive changes in financial behavious and mindset by being bluntly factual.
I have added some categories such as Narcotics and Alcohol. I think other categories to be added are expenses on gaming devices and tobacco.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
