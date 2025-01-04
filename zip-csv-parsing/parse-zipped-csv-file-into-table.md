# Parse zip file and render as html table
- create a csv data file with median income, population by state/city in usa
- create a html page which parses the zipped csv file, it read the zip using fetch(ZIP_URL) parses each line and loads into html table
Here is a snippet of zip file content:
"""
State,City,Median_Household_Income,Population
California,Los Angeles,67739,3898747
New York,New York City,70663,8336817
"""

**Libraries used:**
   - JSZip for ZIP file handling
   - Papa Parse for CSV parsing
**Steps**
1. Read the ZIP file
2. Extract the first CSV file it finds
3. Parse the CSV content
4. Display the data in a formatted table


