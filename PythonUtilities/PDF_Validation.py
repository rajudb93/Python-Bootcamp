import pymupdf  # PyMuPDF

def extract_and_search(pdf_path, search_text):
    # Open the PDF file
    doc = pymupdf.open(pdf_path)
    
    print(f"Document opened: {pdf_path}")
    print(f"Number of pages: {doc.page_count}\n")
    
    # Extract text page by page
    for i in range(doc.page_count):
        page = doc.load_page(i)
        text = page.get_text()
        print(f"--- Page {i+1} ---")
        print(text[:500])  # print first 500 chars of the page text
        print()
    
    # Search for all occurrences of search_text on the first page as example
    page = doc.load_page(0)
    found_instances = page.search_for(search_text)
    
    if found_instances:
        print(f"Found '{search_text}' {len(found_instances)} time(s) on Page 1 at locations:")
        for inst in found_instances:
            print(inst)
    else:
        print(f"'{search_text}' not found on Page 1.")

    doc.close()

# Usage example:
extract_and_search("E:\Learning\Python\PythonBasic\PythonUtilities\example.pdf", "Python")
