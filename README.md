F1 Qualifying Lap Analyis

Instructions
- open VSCode with the JSON file within the same directory
- in terminal, run: python3 f1_application.py

Configurations
- runs as a single script (f1_application.py)
- ensure session_laptimes.json is in the same folder
- no environment variables / configuration files, it runs as a console app

Language & Framework
- language: python3
- framework: none used
- libraries: JSON, operator

Overall Approach
1. I created a draft file to test and understand the dataset I'm working with which included:
    - testing different variables within the JSON file
    - seeing the relationship between sesT, lST, time
    - understanding how qualifiers worked for each team
    - creating a draft solution that can be run in (DRAFT... .py)
2. Initally, the JSON file was read with error handling (try/except)
3. A list of drivers were created for the user to select using a Bool While loop
4. Q1, Q2, Q3 shortest times were created as lists, iterated over followed by using the min() function as long as the list was not empty giving the solution for 3A
5. A function was created to get the best times from Q3 descending for each team. I used a dictionary here. Then I sorted the dictionary using sort() & itemgetter, processing the information into an ordered list.
6. I made sure that Q3 entries would not be present in Q2 & 1. Same with Q2 not being in Q1. I then appended the list
7. The driver position was found indexing the original user input into the sorted list, resulting in the solution for 3B
8. The final file made was as a result of refactoring and removing test code

Assumptions & Tradeoffs
- I assumed that there would be no 'null' values in the dataset (I used "None" instead)
- I assumed that the final rankings are determined from the best possible lap times
- I assumed that the dataset remained consistent e.g. all drivers being 3 letters etc
- I assumed that I didn't need to display a driver profile once selected, though it would have been something additional I would have liked to have done

- The trade off is that code may have to be modified for future datasets
- For improvements:
    - I would have liked to build a flask based web application
    - I could have thought about how to manage null values

How did I use AI
- debugging issues related to using import itemgetter
- formed a layout for the license template
- using AI to double check if sorted values are ranked correctly whilst testing

Please read DATASET_LICENSE.md for information about the dataset used

Thanks,
Hanijan Majuran