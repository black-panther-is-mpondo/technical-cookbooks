# %% [markdown]
# # SQL Practice Problems — SQLite Setup
#
# This notebook is for working through **SQL Practice Problems** by **Sylvia Moestl Vasilik**.
#
# The goal is to practice SQL against a local SQLite version of the Northwind database.
#
# The database file is tracked in this repository at:
#
# ```text
# data/processed/sql/001-sql-practice-problems-sylvia-moestl-vasilik.sqlite
# ```
#
# Since this notebook lives in:
#
# ```text
# cookbooks/sql/
# ```
#
# the relative path to the database is:
#
# ```text
# ../../data/processed/sql/001-sql-practice-problems-sylvia-moestl-vasilik.sqlite
# ```

# %%
from pathlib import Path
from contextlib import closing
import sqlite3

import pandas as pd

# %% [markdown]
# ## Database path
#
# Define the path to the SQLite database.
#
# This database should already exist. We do not want SQLite to silently create a new empty database because that can hide path mistakes.

# %%
DB_PATH = Path("../../data/processed/sql/001-sql-practice-problems-sylvia-moestl-vasilik.sqlite")

if not DB_PATH.exists():
    raise FileNotFoundError(f"Database not found: {DB_PATH.resolve()}")

DB_PATH

# %% [markdown]
# ## SQL helper function
#
# This helper runs a SQL query and returns the result as a Pandas DataFrame.
#
# A context manager is used so the SQLite connection is closed properly after each query.

# %%
def read_sql(query: str, params: tuple | dict | None = None) -> pd.DataFrame:
    """Run a SQL query against the SQLite database and return a DataFrame."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        return pd.read_sql_query(query, conn, params=params)

# %% [markdown]
# ## List available tables
#
# SQLite stores table metadata in `sqlite_master`.
#
# This query confirms that the database is connected correctly and shows the available tables.

# %%
read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
    """
)

# %% [markdown]
# ## Test query
#
# The Northwind tables in this SQLite file include `dbo.` in the table names.
#
# Because of that, table names must be wrapped in double quotes.
#
# Correct:
#
# ```sql
# SELECT *
# FROM "dbo.Customers";
# ```
#
# Incorrect:
#
# ```sql
# SELECT *
# FROM dbo.Customers;
# ```

# %%
read_sql(
    """
    SELECT *
    FROM "dbo.Customers"
    LIMIT 5;
    """
)

# %%