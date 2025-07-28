import fitz  # PyMuPDF
import json

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    title = doc.metadata.get("title", "Untitled Document")

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text = " ".join(span["text"] for span in line["spans"]).strip()
                    if not text or len(text) < 3:
                        continue

                    font_size = max(span["size"] for span in line["spans"])
                    if font_size > 12:
                        if font_size > 18:
                            level = "H1"
                        elif font_size > 15:
                            level = "H2"
                        else:
                            level = "H3"
                        headings.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    return {
        "title": title,
        "headings": headings
    }

if __name__ == "__main__":
    pdf_path = "/app/sample_structured.pdf"
    result = extract_headings(pdf_path)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump([result], f, indent=2, ensure_ascii=False)
    print("✅ Extracted headings saved to output.json")
