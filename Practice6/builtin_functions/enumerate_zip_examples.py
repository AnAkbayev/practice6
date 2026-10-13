students = ["Amina", "Daniyar", "Mira"]
scores = [91, 84, 97]

print("enumerate():")
for index, student in enumerate(students, start=1):
    print(index, student)

print("\nzip():")
for student, score in zip(students, scores):
    print(f"{student}: {score}")

print("\nsorted():", sorted(scores))
print("sorted descending:", sorted(scores, reverse=True))
