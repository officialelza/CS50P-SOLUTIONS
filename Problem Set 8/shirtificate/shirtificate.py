from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png",10,70,200)
        self.set_font("helvetica", "B", 47)
        self.cell(0,64,"CS50 Shirtificate", align= "C")
        self.ln(20)

def main():
    name = input("Enter Name: " )
    turn_to_shirt(name)

def turn_to_shirt(n):
    pdf = PDF()
    pdf.add_page(orientation= "P")
    pdf.set_font("helvetica", "B" , size = 24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0 ,220, f"{n} took CS50" , align= "C")
    pdf.output(f"shirtificate.pdf")


if __name__ == "__main__" :
    main()

