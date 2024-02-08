'''
    This script opens a CSV file containing a list of URLs and for each URL it generates PDF files with the impression of these webpages.
    Ensure you have PyQt5 installed in your Python environment. 
    You can install it using: pip install PyQt5
    Author: Alexandre Strapação Guedes Vianna
    E-mail: strapacao@gmail.com
    Website: alexandrevianna.net
    Paper: https://www.sciencedirect.com/science/article/abs/pii/S0164121223001395
'''

import csv
import os
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

# Initialize a QApplication
app = QtWidgets.QApplication(sys.argv)

def html_to_pdf(html, pdf):
        
    # Create a QWebEnginePage object, which is used to load and render web pages
    page = QtWebEngineWidgets.QWebEnginePage()
    
    def handle_print_finished(filename, status):
        print("finished", filename, status)
        # Exit the application once printing is done
        QtWidgets.QApplication.quit()

    def print_pdf():        
        # Initiates printing of the currently loaded web page to a PDF file.        
        page.printToPdf(pdf)

    def handle_load_finished(status):
        if status:
            # If the page loaded successfully, execute any necessary JavaScript before printing
            execute_js()
        else:
            # If the page failed to load, print an error message and exit
            print("Failed")
            QtWidgets.QApplication.quit()

    def handle_run_js(status):
        print("-")
        if status:
            # If the JavaScript executed successfully, proceed to print the page to PDF
            QtCore.QTimer.singleShot(1000, print_pdf)
        else:
            # If JavaScript execution failed, attempt to execute it again
            QtCore.QTimer.singleShot(1000, execute_js)

    def execute_js():
        # Example JavaScript code that clicks elements with a specific class name
        # Note: This specific example may need to be adjusted to target relevant elements on your web page
        page.runJavaScript(
            """
            (function () {
                var elements = document.getElementsByClassName('ClassName')
                for (i = 0; i < elements.length; i++) {
                  elements[i].click()
                } 
                return true;
            })();
            """,
            handle_run_js,
        )

    # Connect signals to their corresponding callback functions
    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    # Load the URL of the web page to convert
    page.setUrl(QtCore.QUrl(html))
    # Execute the application event loop
    app.exec_()

# Main execution block
if __name__ == "__main__":
    # Open the CSV file containing URLs
    with open('search_results.csv') as csv_file:
        # Create a CSV reader object to read the file
        csv_reader = csv.reader(csv_file, delimiter=';')
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Print the ID, title, and URL for each row
            print(f'{row[0]} | {row[1]} | {row[2]}')
            # Convert the web page to PDF using the URL and save it with a specific filename
            html_to_pdf(row[2], "output/"+str(row[0]) + "_" + str(row[1]) + ".pdf")
