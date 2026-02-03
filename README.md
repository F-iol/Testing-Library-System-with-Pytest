# Features for library :
-**Book Management:** Borrowing and returning logic with automated status updates.  
-**User History:** Relational tracking of all past and current loans.  
-**Relational Database:** Implemented with SQLite and SQLAlchemy ORM.  
-**Data Integrity:** Handled via foreign keys, unique constraints, and transaction rollbacks.  


# Testing :
-**Integration Tests:** Verifying the full flow between Users, Books, and Loans in an in-memory database.  
-**Negative Testing:** Validating system behavior against invalid IDs, unavailable books, and double-returns.  
-**Parameterized Testing:** Efficiently testing multiple scenarios (Edge Cases) with minimal code duplication.  
-**Database Isolation:** Using Pytest fixtures to ensure a clean state for every test run.  

## Installation
```bash
pip install -r requirements.txt
```
## Running tests
```bash
pytest tests/
```
## Coverage report
```bash
pytest --cov=app --cov-report=term-missing tests/
```

Logic coverage should be around 98%
