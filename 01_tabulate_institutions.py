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

# Tabulate all institutions in the data. Match to label_institution.csv for names
all_newyork_institutions = newyork_earnings[["institution"]].drop_duplicates()

# Read institution labels
label_url = f"{SCHEMA_URL}/label_institution.csv"
institution_labels = pd.read_csv(label_url, dtype={"institution": str})

# Merge to get institution names
all_newyork_institutions = all_newyork_institutions.merge(
    institution_labels, on="institution", how="left"
)

# Print all without truncation
pd.set_option("display.max_rows", None)
print(all_newyork_institutions)

