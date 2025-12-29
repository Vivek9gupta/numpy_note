from datetime import datetime

# Data storage
children = []
vaccinations = []
doctor_visits = []

# Functions
def add_child():
    name = input("Enter child's name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    children.append({"name": name, "dob": dob})
    print("✅ Child added!\n")

def add_vaccination():
    child = input("Enter child's name: ")
    vaccine = input("Enter vaccine name: ")
    due = input("Enter due date (YYYY-MM-DD): ")
    vaccinations.append({"child": child, "vaccine": vaccine, "due": due, "status": "Pending"})
    print("✅ Vaccination scheduled!\n")

def add_doctor_visit():
    child = input("Enter child's name: ")
    visit_date = input("Enter visit date (YYYY-MM-DD): ")
    notes = input("Enter notes: ")
    doctor_visits.append({"child": child, "date": visit_date, "notes": notes})
    print("✅ Doctor visit added!\n")

def show_upcoming_events():
    today = datetime.today().date()
    print("\n📅 Upcoming Events:")

    for v in vaccinations:
        due_date = datetime.strptime(v["due"], "%Y-%m-%d").date()
        if due_date >= today and v["status"] == "Pending":
            print(f"💉 {v['child']} - {v['vaccine']} on {v['due']} (Status: {v['status']})")

    for d in doctor_visits:
        visit_date = datetime.strptime(d["date"], "%Y-%m-%d").date()
        if visit_date >= today:
            print(f"👨‍⚕️ {d['child']} - Doctor visit on {d['date']} ({d['notes']})")
        else:
            print("----------today no work--------")

    print()

def mark_vaccination_done():
    child = input("Enter child's name: ")
    vaccine = input("Enter vaccine name to mark as done: ")
    for v in vaccinations:
        if v["child"] == child and v["vaccine"].lower() == vaccine.lower():
            v["status"] = "Done"
            print("✅ Vaccination marked as done!\n")
            return
    print("⚠️ Vaccination not found!\n")

# ---------------------- Main Menu ----------------------
while True:
    print("====== Child Care Companion ======")
    print("1. Add Child")
    print("2. Add Vaccination")
    print("3. Add Doctor Visit")
    print("4. Show Upcoming Events")
    print("5. Mark Vaccination as Done")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_child()
    elif choice == "2":
        add_vaccination()
    elif choice == "3":
        add_doctor_visit()
    elif choice == "4":
        show_upcoming_events()
    elif choice == "5":
        mark_vaccination_done()
    elif choice == "6":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, try again!\n")
