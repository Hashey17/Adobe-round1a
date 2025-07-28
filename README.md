  Smart PDF Mapper – Structured Outline Extractor (Adobe Hackathon Round 1A)

   Overview

This project was developed for   Adobe India Hackathon 2025 – Round 1A   under the theme  "Connecting the Dots" . The task was to extract a   structured outline   from a given PDF document, specifically capturing all hierarchical headings (H1, H2, H3) along with their   corresponding page numbers  , and return them in a well formatted   JSON   structure.

   

   Problem Statement

Given a PDF file, build an offline system that:

  Extracts all the headings (H1 to H3)
  Retrieves their respective page numbers
  Outputs the structure in a clean JSON format
  Runs entirely inside a   Docker container  
  Completes execution in   under 60 seconds   (CPU only)

   

   Approach

We used the   PyMuPDF (fitz)   library in Python to traverse and extract the outline tree of the PDF. Here's the high level logic:

1.   Load the PDF   using PyMuPDF.
2.   Parse the document's outline   using recursive traversal.
3.   Match each heading   with its corresponding page number.
4.   Build a nested JSON structure   based on heading levels.
5.   Save the output   as `output.json`.

The entire system is packaged in a lightweight Docker container for offline usage.

   


