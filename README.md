# Generate-Barcode-Price-Labels-From-Excel
Python Script To Generate Barcode Price Labels From Excel
------------------------------------------------------------------------------------------------
Instructions for naming column in Excel

barcode number column name should be 		             **EAN/Barcode Number**

name of article/product column name should be	       **Name**

price column name should be 			                   **Price**

--------------------------------------------------------------------------------------------------

Instructions for Using Script
Click Link Download and Install Program(check add to path checkbox if unchecked)
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2021-01-30/gtk2-runtime-2.24.33-2021-01-30-ts-win64.exe 
(if above link is dead)
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

Download and Install Python. There is option add to path **check** it if its uncheck
https://www.python.org/downloads/

Create New Folder and Copy all 3 files to new folder
1.	main.py
2.	template.css
3.	template.html
now open that folder 
go to address bar of file explorer

 ![image](https://user-images.githubusercontent.com/59804772/119804646-fa46a500-bef9-11eb-8eb7-fb3a98b2489f.png)

Enter cmd and press enter key console open up

 ![image](https://user-images.githubusercontent.com/59804772/119804667-00d51c80-befa-11eb-835c-132d595816a3.png)


At Console enter these commands one by one. packages installation takes time kindly wait (:
Each command download package and take little bit time depending on internet
pip install blabel
pip install pandas
pip install openpyxl

Congratulations Everything is Ready

Now just type the final command and script will generate labels 24 per page
(Few more instructions put the excel file in same folder as script and rename it as input)

python gen.py

every time you want to generate new label just put excel file in same folder as script and rename it as input
go to address type cmd and press enter when console appears just run python gen.py
and new pdf file will be generated with new label also always copy generated labels to another folder as each time new file generated previous will be replaced if its in same folder as script

If You Don’t Understand Anything or Having Difficulty Do Let Me Know and if you can’t do anything let me know we can do zoom meeting and I will do everything, myself. Don’t worry even after order is finished, I will help you with any issue you face. Also, any more data can be added to label in future just keep 3 files with you as these are source files.
