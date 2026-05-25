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
    pdf.cell(w=50,h=8,txt=f"{filename.title()}")

pdf.output("PDFs/Animal.pdf")