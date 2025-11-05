import csv
import os

class DailyLogger:
    def __init__(self, filepath):
        self.filepath = filepath
        self.fields = [
            "Date", "Intern Name", "Tasks Completed", "Challenges Faced",
            "Learnings", "Next Day Goals", "Hours Worked"
        ]

        if not os.path.exists(filepath):
            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()

    def log_entry(self, date, name, tasks, challenges, learnings, goals, hours):
        with open(self.filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerow({
                "Date": date,
                "Intern Name": name,
                "Tasks Completed": tasks,
                "Challenges Faced": challenges,
                "Learnings": learnings,
                "Next Day Goals": goals,
                "Hours Worked": hours
            })
