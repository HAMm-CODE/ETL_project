# ETL_project
A simple Python ETL (Extract, Transform, Load) pipeline that reads CSV, JSON, and XML files, converts heights from inches to meters and weights from pounds to kilograms, and writes a consolidated output CSV. Use this README on GitHub as the project overview and usage guide.

**Files**
- etl_code.py — main ETL script (reads files, transforms data, writes output)

**Overview**
- Extracts data from all `.csv`, `.json`, and `.xml` files in the project folder (skips the output file).
- Transforms `height` (inches → meters) and `weight` (pounds → kilograms), rounding to 2 decimals.
- Loads the transformed, consolidated data to `transformed_data.csv` and appends progress logs to `log_file.txt`.

**Requirements**
- Python 3.8+
- pandas
- (standard library: glob, xml.etree.ElementTree, datetime)

Install:
```
pip install pandas
```

**Quick Start**
1. Place your input files in the project folder.
2. Run:
```
python etl_code.py
```
3. Results:
- Output CSV: transformed_data.csv
- Log: log_file.txt

**Input File Expectations**
- Each record must provide: name, height, weight
- Heights in input are in inches; weights in pounds.
- Supported formats:
  - CSV: header row with `name,height,weight`
  - JSON (newline-delimited): objects with `name`, `height`, `weight`
  - XML: each record with `<name>`, `<height>`, `<weight>` elements

Example CSV:
```csv
name,height,weight
Alice,65,130
Bob,70,180
```

Example JSON (lines):
```json
{"name": "Alice", "height": 65, "weight": 130}
{"name": "Bob", "height": 70, "weight": 180}
```

Example XML:
```xml
<people>
  <person>
    <name>Alice</name>
    <height>65</height>
    <weight>130</weight>
  </person>
  <person>
    <name>Bob</name>
    <height>70</height>
    <weight>180</weight>
  </person>
</people>
```

**Behavior Notes & Tips**
- The script concatenates data from all matching files into one DataFrame before transforming.
- The script skips combining `transformed_data.csv` when scanning CSV files.
- Timestamped progress messages are appended to `log_file.txt`. The timestamp format in the script is Year-Monthname-Day-Hour-Minute-Second.
- If your input files vary in column order or include extra columns, ensure they contain `name`, `height`, and `weight` fields; otherwise, pre-normalize them.

**Troubleshooting**

**Empty DataFrame / No data in transformed_data.csv:**
- **Cause:** No source data files (`.csv`, `.json`, or `.xml`) found in the project folder.
- **Solution:** Add at least one input file with the correct format and columns (`name`, `height`, `weight`) to the project folder, then run the script again.

**Extending / Customizing**
- To change output filename or log name, edit variables at the top of etl_code.py.
- Add validation for missing/invalid values before transformation to handle corrupt inputs.
- Add a `--output`/`--log` CLI using `argparse` for flexibility.

**Contributing**
- Open an issue or submit a pull request with improvements or bug fixes.

**License**
- MIT License — modify as needed for your project.

Enjoy!
