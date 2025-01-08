# PubMed Paper Fetcher

This project fetches research papers from PubMed using a user-defined query. It extracts specific details about each paper, such as title, publication date, authors, company affiliations, and the corresponding author's email, and then saves the results in a CSV format.

## Project Organization

- **cli.py**: The main script for running the program via the command line. It accepts a query, saves the results to a CSV file, and provides logging for debugging.
- **pubmed_fetcher.py**: Contains functions that interact with the PubMed API to fetch paper details based on a given query.
- **output.csv**: The file where the results of the query are saved. Each row contains details like PubMed ID, title, publication date, non-academic authors, company affiliations, and corresponding author emails.
- **README.md**: This file, which provides an overview and instructions on how to use the program.
- **Backend takehome problem.pdf**: Additional document related to the project (if applicable).

## Tools and Libraries Used

- **Python** (version 3.9 or higher)
- **Requests** library: Used for making HTTP requests to the PubMed API.
  - Installation: `pip install requests`
- **argparse**: For parsing command-line arguments.
- **csv**: For saving results to a CSV file.
- **logging**: To log the progress of the program and for debugging.

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sarvagya-pec/your-repository-name.git
    ```

2. **Install dependencies**:
    If you haven't already installed the required libraries, you can do so using the following command:
    ```bash
    pip install requests
    ```

3. **Running the Program**:
    You can run the program by using the following command:
    ```bash
    python cli.py "<your-query>" -f <output-file>.csv -d
    ```
    - `<your-query>`: Replace with the query you want to search on PubMed (e.g., `"cancer AND treatment"`).
    - `<output-file>.csv`: Replace with the desired filename where you want to save the results (e.g., `output.csv`).
    - `-d`: (optional) Enables debug mode for detailed logs.

    The program will fetch papers from PubMed and save them into the specified CSV file.

## Example Usage

```bash
python cli.py "cancer AND treatment" -f output.csv -d
