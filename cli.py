import argparse
from pubmed_fetcher import fetch_papers, save_to_csv, setup_logging

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="PubMed query string.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results as CSV.", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    
    args = parser.parse_args()

    # Setup logging based on debug flag
    setup_logging(args.debug)
    
    try:
        # Fetch papers using the provided query
        papers = fetch_papers(args.query)
        
        if args.file:
            # Save results to CSV if file argument is provided
            save_to_csv(papers, args.file)
        else:
            # Print results to the console if no file is specified
            for paper in papers:
                print(paper)
    except Exception as e:
        # Handle any errors during execution
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
