
import csv
from pathlib import Path
from datetime import date

FILE = Path("reports.csv")
FIELDS = ["id", "date", "category", "location", "summary"]


def load_reports():
    if not FILE.exists():
        return []
    with FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def add_report():
    reports = load_reports()

    category = input("Category: ").strip()
    location = input("Fictional location: ").strip()
    summary = input("Fictional report summary: ").strip()

    if not category or not location or not summary:
        print("Please complete every field.")
        return

    report = {
        "id": str(len(reports) + 1),
        "date": date.today().isoformat(),
        "category": category,
        "location": location,
        "summary": summary,
    }

    new_file = not FILE.exists() or FILE.stat().st_size == 0

    with FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(report)

    print("Report saved successfully!")


def view_reports():
    reports = load_reports()

    if not reports:
        print("No reports found.")
        return

    for report in reports:
        print(report)


def search_reports():
    keyword = input("Enter search keyword: ").strip().lower()

    matches = [
        report for report in load_reports()
        if keyword in str(report).lower()
    ]

    if matches:
        for report in matches:
            print(report)
    else:
        print("No matching reports found.")


def main():
    while True:
        print("\\n--- Case Organizer ---")
        print("1. Add report")
        print("2. View reports")
        print("3. Search reports")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_report()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            search_reports()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

