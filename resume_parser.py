from pypdf import PdfReader


def extract_text_from_txt(file):
    return file.read().decode("utf-8")


def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_resume_text(file):

    file_name = file.name.lower()

    if file_name.endswith(".txt"):
        return extract_text_from_txt(file)

    elif file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)

    else:
        raise ValueError(
            "Unsupported file format. Please upload PDF or TXT."
        )