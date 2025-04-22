def read_and_write_file():
    try:
        with open("source.txt", "r") as source_file:
            content = source_file.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        with open("modified.txt", "w") as modified_file:
            modified_file.write(modified_content)
   

        # Count words
        word_count = len(modified_content.split())

        # Create the final content to write
        final_output = f"{modified_content}\n\n[Word Count: {word_count} words]"

        # Append to 'modified.txt' instead of overwriting
        with open("modified.txt", "a") as modified_file:
            modified_file.write(final_output + "\n" + "-"*40 + "\n")

        print("✅ File modified (uppercased, word counted) and appended to 'modified.txt'")

    
    except FileNotFoundError:
        print("❌ Error: 'source.txt' file not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()
