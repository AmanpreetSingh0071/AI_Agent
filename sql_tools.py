from smolagents import tool
from sqlalchemy import text
from sqlalchemy import create_engine

# Assuming engine is already created
engine = create_engine("sqlite:///:memory:")  # In-memory SQLite database (replace with your own setup)

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The SQL query to perform. This should be a correct SQL query.

    Returns:
        A string representing the result of the SQL query.
    """
    output = ""
    try:
        with engine.connect() as con:
            rows = con.execute(text(query))
            for row in rows:
                output += "\n" + str(row)
    except Exception as e:
        output = f"Error executing query: {str(e)}"

    return output