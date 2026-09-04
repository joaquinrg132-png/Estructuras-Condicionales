from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'Código de Programas - Estructuras Condicionales', border=False, ln=True, align='C')
        self.set_font('helvetica', '', 12)
        self.cell(0, 10, 'Nombre: Joaquín Rubén Rosales García', border=False, ln=True, align='C')
        self.cell(0, 10, 'Número de control: 26150079', border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

archivos = [
    "clasificacion_triangulos.py",
    "anio_bisiesto.py",
    "conversor_calificaciones.py",
    "comparacion_numeros.py",
    "tarifa_entrada.py"
]

for arch in archivos:
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, f'Archivo: {arch}', ln=True)
    pdf.set_font('courier', '', 10)
    
    with open(arch, "r", encoding="utf-8") as f:
        codigo = f.read()
    
    for line in codigo.split('\n'):
        clean_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(0, 5, clean_line, ln=True)
        
    pdf.ln(10)

pdf.output("Entrega_Programas_JoaquinR_26150079.pdf")
