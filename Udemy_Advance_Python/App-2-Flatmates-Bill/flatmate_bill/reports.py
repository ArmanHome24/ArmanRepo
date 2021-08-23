import os.path
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(flatmate1.pays(bill=bill, flatmate2=flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill=bill, flatmate2=flatmate1))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', size=24, style='B')

        pdf.image("resources/house.jpg", w=30, h=30)

        # Insert title
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font(family='Times', size=14, style='B')

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period:", border=0)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open('file://' + os.path.realpath(self.filename))