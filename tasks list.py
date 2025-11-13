tasks = []
while True:
    print("\n Select Option from below: ")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("\n Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "3":
        print("Goodbye Thank you!😊 ")
        break

    else:
        print("Invalid choice. Try again.")
