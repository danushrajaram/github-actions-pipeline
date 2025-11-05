from src.logger import DailyLogger
from datetime import date

def main():
    print("\n=== Intern Daily Progress Tracker ===\n")

    intern_name = input("Enter your name: ").strip()
    today = str(date.today())

    tasks = input("Tasks Completed: ").strip()
    challenges = input("Challenges Faced: ").strip()
    learnings = input("Key Learnings: ").strip()
    next_goals = input("Goals for Tomorrow: ").strip()
    hours = input("Hours Worked: ").strip()

    logger = DailyLogger("data/progress_log.csv")
    logger.log_entry(today, intern_name, tasks, challenges, learnings, next_goals, hours)

    print("\n✅ Daily progress recorded successfully!\n")

if __name__ == "__main__":
    main()
