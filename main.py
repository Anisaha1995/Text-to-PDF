import pandas as pd
from fpdf import FPDF
from glob import glob
from pathlib import Path

filepaths = glob("Texts/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = pd.read_csv(filepath)
    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family= "Times",style= "B",size= 16)
    pdf.cell(w=50,h=8,txt=f"{filename.title()}", ln=1)
    with open(filepath,'r') as file:
        content = file.read()
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("PDFs/Animal.pdf")