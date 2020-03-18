# extract-data-from-image-using-uipath-and-python
This code will extract data from OCR based pdf file using UiPath and Python (without using any OCR activity).

1. Install Requirememt.txt file for Python Packages:
   "pip install -r Requirements.txt"
   It will be good if you create separate python_environment and install packages in that specific python_environment.

2. Create directory structure according to your feasibility and change the paths in config.xlsx file.

3. Change your Python Environment Path in ConvertToText.xaml workflow. For example in my case it was:
   "C:\Users\abhishek.o\AppData\Local\Programs\Python\Python36"
   
4. Customize the ExtractData.xaml workflow on the basis of your requirement.   

5. Run the framework from the Main.xaml workflow inside UiPath Studio.

Thank You.

