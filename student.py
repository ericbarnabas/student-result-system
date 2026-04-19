import json


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 45:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {"name": self.name, "scores": self.scores}


class ResultSystem:
    def __init__(self, filename="results.json"):
        self.filename = filename
        self.students = self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Student(s["name"], s["scores"]) for s in data]
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([s.to_dict() for s in self.students], f)

    def add_student(self, name, scores):
        self.students.append(Student(name, scores))
        self.save()
        print(f"Student '{name}' added successfully.")

    def display_all(self):
        if not self.students:
            print("No students found.")
            return
        print(f"\n{'Name':<20} {'Average':<10} {'Grade'}")
        print("-" * 40)
        for s in self.students:
            print(f"{s.name:<20} {s.average():<10.2f} {s.grade()}")

    def run(self):
        while True:
            print("\n--- Student Result System ---")
            print("1. Add student")
            print("2. View all results")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter student name: ")
                scores_input = input("Enter scores separated by commas: ")
                scores = [float(x) for x in scores_input.split(",")]
                self.add_student(name, scores)
            elif choice == "2":
                self.display_all()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    system = ResultSystem()
    system.run()