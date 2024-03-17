from pathlib import Path
from parse_reciept import pdf_to_text
import re
from collections import defaultdict

pdfs = Path(".").glob("*.pdf")

totals = defaultdict(float)
for pdf in pdfs:
    text = pdf_to_text(pdf)
    lines = text.split('\n')
    date = [l for l in lines if "תאריך" in l][1]
    re_match = re.search(r"\d\d/\d\d/(\d\d\d\d)", date)
    year = re_match.group(1)
    amount = [l for l in lines if "שולם" in l][1]
    re_match = re.search(r"\d+(\.\d+)?", amount)
    amount_float = float(re_match.group())
    print(f"{pdf} : '{year}', '{amount_float}'")
    totals[year]+= amount_float
    pdf.replace(pdf.parent / year / pdf.name)

with open("totals.csv","wt") as f: 
    f.write(str(totals))

