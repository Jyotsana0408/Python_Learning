tasks = []

while True:
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task description: ")
        tasks.append({"task": task, "done": False})
        print(f"✅ Task added: {task}")

    elif choice == "2":
        if not tasks:
            print("🕳️ No tasks yet.")
        else:
            print("\n📝 Your Tasks:")
            for i in range(len(tasks)):
                status = "✔️" if tasks[i]["done"] else "❌"
                print(f"{i + 1}. {tasks[i]['task']} [{status}]")

    elif choice == "3":
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"✅ Marked '{tasks[index]['task']}' as done!")
        else:
            print("⚠️ Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("⚠️ Invalid choice. Please select 1-4.")
