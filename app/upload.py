import requests
import re
from PyPDF2 import PdfReader
from io import BytesIO

def download_pdf_from_google_drive(drive_url):
    try:
        file_id = drive_url.split("/d/")[1].split("/")[0]
    except IndexError:
        raise ValueError("Unvalid Google Drive link")

    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"

    response = requests.get(download_url)
    if response.status_code == 200:
        response_stream = BytesIO(response.content)
        return response_stream
    else:
        raise Exception(f"{response.status_code} : Download Error")

def extract_text_from_pdf(pdf_stream, output_filename):
    try:
        pdf_reader = PdfReader(pdf_stream)
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    text = text.replace('\n', ' ')
                    text = re.sub(r'([.!?])\s*', r'\1\n', text)
                    output_file.write(text)
        print(f"{output_filename} created")
        
    except Exception as e:
        raise Exception(f"Error during text extraction : {e}")

if __name__ == "__main__":
    google_drive_link = "https://drive.google.com/file/d/1NguvBe7x4_Vw14AOHnPG3Q9-dgjB7dLs/view?usp=sharing"
    output_txt_path = "vault.txt"

    try:
        pdf_stream = download_pdf_from_google_drive(google_drive_link)

        extract_text_from_pdf(pdf_stream, output_txt_path)
    except Exception as err:
        print(f"Error : {err}")
