from pathlib import Path
from parse_reciept import pdf_to_text
import re
from collections import defaultdict

pdfs = Path(".").glob("*.pdf")

totals = defaultdict(float)
for pdf in pdfs:
    text = pdf_to_text(pdf)
    lines = text.split('\n')
    header = lines[0].strip()
    year = header[-4:]
    amount = [l for l in lines if "לתשלום" in l][0]
    re_match = re.search(r"\d+(\.\d+)?", amount)
    amount_float = float(re_match.group())
    print(f"{pdf} : '{header}' , '{year}', '{amount_float}'")
    totals[year]+= amount_float
    pdf.replace(pdf.parent / year / pdf.name)

with open("totals.csv","wt") as f: 
    f.write(str(totals))
