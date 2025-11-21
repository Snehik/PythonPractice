from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_pdf_documents(pdf_path: str):
    """
    Load PDF documents from the specified path.

    Args:
        pdf_path (str): The path to the PDF file. 
    
    Returns:
        List[Document]: A list of loaded documents."""
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    pdf_path = Path(__file__).parent / "DLBill.pdf"
    print(pdf_path)
    documents = load_pdf_documents(str(pdf_path))
    for i, doc in enumerate(documents):
        print(f"Document {i+1}:\n{doc.page_content}\n") 