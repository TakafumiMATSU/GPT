# CSV Analysis Tool

This repository provides a small Python script for computing basic statistics from a CSV file. It was tested with `Metaboanalyst_250513.csv` included in this repo.

## Requirements

Only the Python standard library is required.

## Usage

Run the analysis script and pass the path to the CSV file:

```bash
python3 analyze_csv.py Metaboanalyst_250513.csv
```

The script will create `analysis_summary.csv` containing the mean, median, standard deviation, minimum and maximum for each row (feature).

