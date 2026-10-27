# Personal Job Application Tracker
applications = {"ABC Technologies": ["Python Intern", "2026-10-27", "Applied"], "XYZ Solutions": ["Data Analyst Intern", "2026-10-25", "Interview"]}
statuses = ["Applied", "Interview", "Selected", "Rejected"]

def add_application():
    company = input("Enter company name: ").strip()
    if not company:
        print("Company name cannot be empty.")
        return
    if company in applications:
        print("An application for this company already exists.")
        return
    role = input("Enter job role: ").strip()
    date = input("Enter date applied (YYYY-MM-DD): ").strip()
    if not role or not date:
        print("Job role and date cannot be empty.")
        return
    applications[company] = [role, date, "Applied"]
    print("Application added successfully!")

def search_application():
    company = input("Enter company name to search: ").strip()
    if company in applications:
        details = applications[company]
        print(f"Company: {company}")
        print(f"Job Role: {details[0]}")
        print(f"Date Applied: {details[1]}")
        print(f"Status: {details[2]}")
    else:
        print("Application not found.")

def update_status():
    company = input("Enter company name: ").strip()
    if company not in applications:
        print("Application not found.")
        return
    print("Available statuses:", ", ".join(statuses))
    new_status = input("Enter new status: ").strip().title()
    if new_status in statuses:
        applications[company][2] = new_status
        print("Status updated successfully!")
    else:
        print("Invalid status.")

def view_applications():
    if not applications:
        print("No applications recorded.")
        return
    for company, details in applications.items():
        print(f"\nCompany: {company}")
        print(f"Job Role: {details[0]}")
        print(f"Date Applied: {details[1]}")
        print(f"Status: {details[2]}")

def generate_report():
    total = len(applications)
    report = ["PERSONAL JOB APPLICATION REPORT", f"Total applications: {total}\n"]
    for status in statuses:
        count = sum(1 for details in applications.values() if details[2] == status)
        report.append(f"{status}: {count}")
    report.append("\nAPPLICATION DETAILS")
    for company, details in applications.items():
        report.append(f"{company} | {details[0]} | {details[1]} | {details[2]}")
    report_text = "\n".join(report)
    print("\n" + report_text)

    with open("application_report.txt", "w") as file:
        file.write(report_text)
    print("\nReport saved to application_report.txt")


while True:
    print("\n--- JOB APPLICATION TRACKER ---")
    print("1. Add application")
    print("2. Search application")
    print("3. Update application status")
    print("4. View all applications")
    print("5. Generate and save report")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_application()
    elif choice == "2":
        search_application()
    elif choice == "3":
        update_status()
    elif choice == "4":
        view_applications()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        print("Exiting tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-6.")
