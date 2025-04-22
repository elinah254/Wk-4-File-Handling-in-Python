def error_handling_lab():
    filename = input("Enter the name of the file to read: ")
    
    try:
        with open(filename, "r") as file:
            print("\n📄 File Content:\n")
            print(file.read())
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: Permission denied.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    error_handling_lab()
