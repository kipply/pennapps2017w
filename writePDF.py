from fpdf import FPDF, HTMLMixin
import time
import random
import string

def writePDF(stories):

  class MyFPDF(FPDF, HTMLMixin):
	  pass
	 
  pdf=MyFPDF()
  #First page
  pdf.add_page()
  pdf.set_font("Arial", size=72)
  pdf.cell(200, 30, txt="CHICKEN SOUP", ln=1, align="C")
  pdf.set_font("Arial", size=30)
  pdf.cell(200, 30, txt="FOR", ln=1, align="C")
  pdf.set_font("Arial", size=72)
  pdf.cell(200, 30, txt="YOUR", ln=1, align="C")
  pdf.cell(200, 30, txt="SOUL", ln=1, align="C")

  pdf.add_page()

  i = 1
  for story in stories: 
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 30, txt="Chapter " + str(i), ln=1, align="C")

    html = story + "<br><br>"
    pdf.write_html(html)
    i = i + 1

  fileName = "static/books/" + time.strftime("%d-%m-%Y_%X_") + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(9)]) + ".pdf"
  
  pdf.output(fileName, "F")
  return fileName
