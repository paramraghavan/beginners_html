# Parse zip file and render as html table

- create a csv data file with median income, population by state/city in usa
- create a html page which parses the zipped csv file, it read the zip using fetch(ZIP_URL) parses each line and loads
  into html table
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

## Optimunm compression

For JSZip, the compression levels you can apply when creating ZIP files are:

1. `STORE` (compression level 0) - No compression, just storage
2. `DEFLATE` (compression levels 1-9) - Standard ZIP deflate compression

The highest compression level you can apply is 9, which provides maximum compression but takes longer to process. Here's
how you would set it:

```javascript
const zip = new JSZip();
zip.file("filename.txt", data, {
    compression: "DEFLATE",
    compressionOptions: {
        level: 9
    }
});
```
```shell
zip -6 output.zip files_to_compress
```

Some practical advice:

- Level 6 is often a good balance between compression ratio and speed
- Levels 7-9 typically only give marginal improvements in file size
- The effectiveness of compression depends heavily on your data type:
    - Text files usually compress well
    - Images, videos, or already-compressed files may see little to no benefit
    - Binary files vary in compressibility

**Note:** that higher compression levels will use more CPU time both when creating and extracting the ZIP file. If
processing speed is important for your application, you might want to test different compression levels with your
specific data to find the optimal balance.
