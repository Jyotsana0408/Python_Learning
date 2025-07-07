import csv

csv_file = r"E:\Jyotsna\Python_Learning\31_JSON_and_CSV\mini_project\student.csv"

def find_top_scorer(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        top_student = None
        top_score = -1

        for row in reader:
            score = int(row["score"])
            if score > top_score:
                top_score = score
                top_student = row["name"]

    print(f"Top Scorer: {top_student} with {top_score} points")

find_top_scorer(csv_file)
