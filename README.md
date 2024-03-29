# Folder-Maker

This Python script allows you to quickly create a new project folder with default HTML, CSS, and JavaScript files. The script prompts you to enter a folder name, checks if the folder already exists, and creates the necessary files within the new folder.

## How to Use
- Run the script by executing the Python file (create_folder.py).
- Enter the desired folder name when prompted.
- The script checks if the folder already exists.
- If not, it creates a new folder with default HTML, CSS, and JavaScript files.

## Folder Structure
```
Folder/
    │- index.html: Default HTML file with a basic template.
    │- styles.css: Default CSS file with a placeholder comment.
    │- script.js: Default JavaScript file with a placeholder comment.

```
## How to Run
Ensure you have Python installed.
```bash
# Run the script
python create_folder.py
```
> [!NOTE]
> Place the Python file in the folder you want to save the files before running the code.

> [!TIP]
> If you want to add more files, you could just use `open()` function in the `with` statement after putting a comma `,`
