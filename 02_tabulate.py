import pandas as pd

STATE = "ny"
BASE_URL = "https://lehd.ces.census.gov/data/pseo/latest_release/"
SCHEMA_URL = f"https://lehd.ces.census.gov/data/schema/latest/"

# Read newyork earnings CSV (gzipped)
newyork_earnings = pd.read_csv(
    f"{BASE_URL}{STATE}/pseoe_{STATE}.csv.gz",
    dtype={"institution": str, "degree_level": str, "cipcode": str, "grad_cohort": str},
    low_memory=False,
)

# Read degree level from schema
degree_level_schema = pd.read_csv(f"{SCHEMA_URL}/label_degree_level.csv", dtype=str)

# Read CIP codes

cip_schema = pd.read_csv(f"{SCHEMA_URL}/label_cipcode.csv", dtype=str)

# Display 50th percentile earnings for all New York grads at the bachelor level (degree level 05) for Economics CIP Codes
# and all graduation cohorts

# Use only the strict Economics CIP code '45.06'
econ_cip_codes = ["45.06"]

all_newyork_grads = newyork_earnings.loc[
    (newyork_earnings["degree_level"] == "05") &
    (newyork_earnings["cipcode"].isin(econ_cip_codes)),
    ["y1_p50_earnings", "degree_level", "cipcode", "grad_cohort", "y1_grads_earn", "status_y1_earnings"]
]

print(all_newyork_grads)

# Graph the yearly results
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
plt.figure(figsize=(10, 6))
sns.lineplot(data=all_newyork_grads, x="grad_cohort", y="y1_p50_earnings", marker="o")
plt.title("50th Percentile Earnings for NY Economics Graduates (Bachelor Level)")
plt.xlabel("Graduation Cohort")
plt.ylabel("50th Percentile Earnings")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('plot.png')
plt.close()  # Optional: free memory