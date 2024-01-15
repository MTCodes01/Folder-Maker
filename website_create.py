import os

while True:
    folder = input('Enter folder name(q -> quit):') # Asking for the Folder name
    cwd = os.getcwd()                               # Current Working Directory
    if folder.lower() == 'q':                       # For Exiting the loop
        quit()
    else:
        if os.path.exists(folder):                      # Checking if the folder exists
            print('\nThe folder already exists.\n')
        else:
            os.mkdir(folder)                            # Making the folder
            print(f'\n{folder} Created.')
            with open(f"{cwd}\\{folder}\\index.html", 'w') as fh_1, open(f"{cwd}\\{folder}\\styles.css", 'w') as fh_2, open(f"{cwd}\\{folder}\\script.js", 'w') as fh_3: # Creating the nessasary files
                print(f'All nessasary files created in {folder}.\n')

                # Default code in the files.
                fh_1.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>{folder}</title>\n    <link rel="stylesheet" type="text/css" href="styles.css">\n</head>\n<body>\n    \n    <script src="script.js"></script>\n</body>\n</html>')
                fh_2.write('/* CSS styles */\n')
                fh_3.write('// JavaScript code\n')