# PubMed Data Fetcher

This project fetches research papers and their associated data from PubMed using the PubMed API. The fetched data includes details such as the paper title, publication date, non-academic authors, company affiliations, and corresponding author email. The results are then saved to a CSV file.

## Features

- Query PubMed to fetch papers based on a search term.
- Extract relevant details from the fetched papers.
- Save the results to a CSV file for easy analysis.

## Requirements

Before running the project, ensure you have the following Python libraries installed:

- `requests`
- `argparse`

You can install them using pip:


## Usage

### Command-Line Interface (CLI)

The project can be run using the command line. The following options are available:

1. **Query**: The search term you want to use to find papers in PubMed.
2. **Output File**: The CSV file where the results will be saved.
3. **Debug Mode**: Enable or disable debug logging.

### Example:

To fetch papers related to "cancer and treatment" and save the results in `output.csv`, use the following command:


## Usage

### Command-Line Interface (CLI)

The project can be run using the command line. The following options are available:

1. **Query**: The search term you want to use to find papers in PubMed.
2. **Output File**: The CSV file where the results will be saved.
3. **Debug Mode**: Enable or disable debug logging.

### Example:

To fetch papers related to "cancer and treatment" and save the results in `output.csv`, use the following command:

