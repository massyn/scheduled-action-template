from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = f"# Hello, World!\n\nThis script was generated on: {current_time}\n\n[![Daily Build](https://github.com/massyn/scheduled-action-template/actions/workflows/python-app.yml/badge.svg)](https://github.com/massyn/scheduled-action-template/actions/workflows/python-app.yml)"

with open("README.md", "w") as file:
    file.write(content)

print("README.md file created successfully!")
