from datetime import datetime

# Get the current timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = f"# Hello, World!\n\nThis script was generated on: {current_time}"

with open("README.md", "w") as file:
    file.write(content)

print("README.md file created successfully!")
