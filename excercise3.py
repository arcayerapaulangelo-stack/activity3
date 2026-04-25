def main():
    try:
        
        username = input("Enter username: ")
        age = int(input("Enter age: "))

    
        if username.strip() == "":
            raise ValueError("Username cannot be empty.")
        if age <= 0:
            raise ValueError("Age must be a positive number.")

        
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

        print("\nUser saved successfully!\n")

    except ValueError as e:
        print(f"Input Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    finally:
        
        print("\nSaved Users:")
        try:
            with open("users.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No users found yet.")

        
        print("System complete.")



main()