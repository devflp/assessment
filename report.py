import pandas as pd


def print_summary():
    path = "./data/Restaurant_Scores_-_LIVES_Standard.csv"
    dataframe = pd.read_csv(path)
    inspection = dataframe['inspection_score']  # gets the inspection_score column
    print("**---    Summary Statistics for Inspection Scores    ---**")
    # The >8 string format specification aligns the field ({}) to the right with a width of 8
    print(f"Minimum: {int(inspection.min()): >8}")
    print(f"Maximum: {int(inspection.max()): >8}")
    print(f"Mean:    {round(inspection.mean(), 4): >8}")  # Rounded to 4 decimal places for readability
    print(f"Median:  {inspection.median(): >8}")

    print("**--- Violations ---**")
    violation_count = dataframe["violation_description"].value_counts()
    print(violation_count.to_string())


if __name__ == '__main__':
    print_summary()
