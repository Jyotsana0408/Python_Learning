# Real-Time Multiprocessing Downloader

# What Makes It Real-Time?
# Each file shows a live progress bar while downloading.
# Downloads run in parallel using multiple processes.
# You get a summary at the end with success or error messages.

# requests: Downloads files over HTTP.
# os: Helps extract filenames from URLs.
# multiprocessing.Pool: Runs tasks concurrently using separate processes.
# tqdm: Displays a progress bar during downloads.

import requests
import os
from multiprocessing import Pool
from tqdm import tqdm

# A worker function for each process to handle downloading a single file.
def download_file(url):

    # Extracts the file name from the URL (e.g., https://abc.com/file.pdf → file.pdf).
    filename = os.path.basename(url)

    # Begins downloading the file in streaming mode, which is great for big files.
    try:
        response = requests.get(url, stream=True)

        # Reads the total size of the file from the response headers (used by tqdm for progress).
        total = int(response.headers.get('content-length', 0))

        # Opens a local file for writing in binary mode (wb).
        # Creates a progress bar with the expected size, scaling by kilobytes.
        with open(filename, 'wb') as file, tqdm(
            desc=filename,
            total=total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            
            # Downloads and writes the file in chunks of 1024 bytes.
            # Each chunk updates the progress bar to reflect real-time download speed.
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))

        # Returns a success message when the file finishes downloading.
        return f"Downloaded: {filename}"
    
    # Catches errors like network issues and prints a friendly error message.
    except Exception as e:
        return f"Error downloading {url}: {e}"

# Ensures the multiprocessing logic only runs when the script is executed directly.
if __name__ == "__main__":

    # A list of files to download—each URL will be handled by a separate process.
    urls = [
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "https://file-examples.com/wp-content/uploads/2017/02/file-sample_100kB.doc",
        "https://file-examples.com/wp-content/uploads/2017/10/file-example_PDF_1MB.pdf"
    ]

    # Creates a Pool with 3 parallel processes.
    # Applies the download_file function to each URL using map().
    with Pool(processes=3) as pool:
        results = pool.map(download_file, urls)

    # After all downloads finish, it prints a summary showing each file's result.
    print("\nSummary:")
    for r in results:
        print(r)
