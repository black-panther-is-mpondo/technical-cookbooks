# %% [markdown]
# # Example Cookbook Title
#
# Briefly explain what this cookbook is about.
#
# ## Goal
#
# By the end of this cookbook, you should understand how to:
#
# - Do one practical thing
# - Reuse a simple pattern
# - Apply it in a real project

# %%
from pathlib import Path

# %% [markdown]
# ## 1. Setup
#
# Define paths, constants, or configuration values here.

# %%
PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# %% [markdown]
# ## 2. Example input
#
# Add sample data or explain what kind of input the code expects.

# %%
example_text = "hello cookbook"
example_text

# %% [markdown]
# ## 3. Main logic
#
# Keep the main reusable logic in functions where possible.

# %%
def clean_text(value: str) -> str:
    """Clean a text value by stripping spaces and converting to title case."""
    return value.strip().title()

# %% [markdown]
# ## 4. Run the example

# %%
cleaned_text = clean_text(example_text)
cleaned_text

# %% [markdown]
# ## 5. Notes
#
# Use this section for:
#
# - Things to remember
# - Common mistakes
# - Links to further reading
# - Variations of the same pattern