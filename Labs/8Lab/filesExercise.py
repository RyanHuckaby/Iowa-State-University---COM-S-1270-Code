"""
Ryan Huckaby
Lab #8 (Week Ten)
Date Started: 10/29/2025
This code calculates and stores several
aspects of grade scores of fictitious college students, given two
different files containing the relevant information
"""
def main():
    students = []
    with open("students.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            parts = line.strip().split(",")
            sid = parts[0].strip()
            name = parts[1].strip()
            students.append((sid, name))

    scores_by_id = {}
    with open("scores.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue
            sid = parts[0].strip()
            score_text = parts[2].strip()
            if not score_text.isdigit():
                continue 
            score = float(score_text)
            if sid not in scores_by_id:
                scores_by_id[sid] = []
            scores_by_id[sid].append(score)

    grades = [["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]]

    for sid, name in students:
        if sid == "Student ID":
            continue
        scores = scores_by_id.get(sid, [])
        total = len(scores)
        total_sum = sum(scores)
        avg = total_sum / total if total > 0 else 0
        grades.append([sid, name, str(total), str(int(total_sum)), f"{avg:.1f}"])

    with open("grades.txt", "w") as f:
        index = 0
        while index < len(grades):
            row = grades[index]
            f.write(",".join(row))
            if index < len(grades) - 1:
                f.write("\n")
            index += 1
if __name__ == "__main__":
    main()