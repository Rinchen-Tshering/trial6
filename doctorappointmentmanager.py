import queue

patient_queue = queue.Queue()

def register_patient():
    patient_name = input("Enter the patient's name: ")
    patient_queue.put(patient_name)
    print("Patient registered.")

def remove_patient():
    if not patient_queue.empty():
        removed_patient = patient_queue.get()
        print(f"{removed_patient} removed after meeting the doctor.")
    else:
        print("No patients in the queue.")

def display_patient_queue():
    if not patient_queue.empty():
        print("Current patient queue:")
        for patient in list(patient_queue.queue):
            print(patient)
    else:
        print("No patients in the queue.")

def main():
    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            remove_patient()
        elif choice == "3":
            display_patient_queue()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()