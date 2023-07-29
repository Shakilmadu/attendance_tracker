def mark_attendance(attendance_dict, event_name, participant_name):
    if event_name not in attendance_dict:
        attendance_dict[event_name] = set()
    attendance_dict[event_name].add(participant_name)

def display_attendance(attendance_dict):
    for event_name, participants in attendance_dict.items():
        print(f"{event_name}: {', '.join(participants)}")

def main():
    attendance_dict = {}
    while True:
        print("\nAttendance Tracker")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            event_name = input("Enter event name: ")
            participant_name = input("Enter participant name: ")
            mark_attendance(attendance_dict, event_name, participant_name)
            print("Attendance marked successfully!")

        elif choice == "2":
            if attendance_dict:
                print("Attendance:")
                display_attendance(attendance_dict)
            else:
                print("No attendance data available.")

        elif choice == "3":
            print("Exiting Attendance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

 if __name__ == "__main__":
    main()



