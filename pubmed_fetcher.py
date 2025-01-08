import argparse
import csv
import logging
import re
from typing import List, Dict, Any
import requests

# Setup logging
def setup_logging(debug: bool):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# Function to query PubMed API
def fetch_papers(query: str) -> List[Dict[str, Any]]:
    logging.info("Fetching papers from PubMed API...")
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 100  # Limit to 100 results for this example
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    search_results = response.json()
    
    if "esearchresult" not in search_results or "idlist" not in search_results["esearchresult"]:
        logging.warning("No results found or invalid response from PubMed.")
        return []

    pubmed_ids = search_results["esearchresult"]["idlist"]
    
    papers = []
    for pmid in pubmed_ids:
        paper_details = fetch_paper_details(pmid)
        if paper_details:
            papers.append(paper_details)

    return papers

# Function to fetch details of a paper by PubMed ID
def fetch_paper_details(pmid: str) -> Dict[str, Any]:
    logging.info(f"Fetching details for PubMed ID: {pmid}")
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    details = response.json()

    if "result" not in details or pmid not in details["result"]:
        logging.warning(f"No details found for PubMed ID: {pmid}")
        return {}

    paper_data = details["result"][pmid]
    return {
        "PubmedID": pmid,
        "Title": paper_data.get("title", "N/A"),
        "PublicationDate": paper_data.get("pubdate", "N/A"),
        "NonAcademicAuthors": extract_non_academic_authors(paper_data),
        "CompanyAffiliations": extract_company_affiliations(paper_data),
        "CorrespondingAuthorEmail": extract_corresponding_author_email(paper_data)
    }

# Helper functions for data extraction
def extract_non_academic_authors(paper_data: Dict[str, Any]) -> List[str]:
    authors = paper_data.get("authors", [])
    non_academic_authors = []
    for author in authors:
        affiliation = author.get("affiliation", "").lower()
        if "university" not in affiliation and "institute" not in affiliation:
            non_academic_authors.append(author.get("name", "N/A"))
    return non_academic_authors

def extract_company_affiliations(paper_data: Dict[str, Any]) -> List[str]:
    affiliations = [author.get("affiliation", "") for author in paper_data.get("authors", [])]
    company_affiliations = [aff for aff in affiliations if "pharma" in aff.lower() or "biotech" in aff.lower()]
    return company_affiliations

def extract_corresponding_author_email(paper_data: Dict[str, Any]) -> str:
    return paper_data.get("corresponding_author", {}).get("email", "N/A")

# Function to save results to CSV
def save_to_csv(papers: List[Dict[str, Any]], filename: str):
    logging.info(f"Saving results to {filename}...")
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["PubmedID", "Title", "PublicationDate", "NonAcademicAuthors", "CompanyAffiliations", "CorrespondingAuthorEmail"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)
