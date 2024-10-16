from fpdf import FPDF

def main():
        
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', "B", 30)
    pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align="c")


    pdf.image(r'C:\Projects\CS50P\Problem_set_8\shirtificate.png', x= 20, y= 80, w=170)
    
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(200, 150, f'{name} took CS50', new_x="LMARGIN", new_y="NEXT", align='c')

    pdf = pdf.output('shirtification.pdf')
    
    
if __name__ == "__main__":
    main()



