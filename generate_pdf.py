from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

def create_cv_pdf(output_path, readme_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Read content from README.md
    with open(readme_path, "r") as f:
        lines = f.readlines()

    y = height - 72
    c.setFont("Helvetica", 12)

    for line in lines:
        if line.strip():  # Skip empty lines
            if line.startswith("#"):
                c.setFont("Helvetica-Bold", 16)
                c.drawString(72, y, line.strip("# "))
                y -= 24
            elif line.startswith("**"):
                c.setFont("Helvetica-Bold", 14)
                c.drawString(72, y, line.strip("** "))
                y -= 20
            else:  # General text handling
                c.setFont("Helvetica", 12)
                wrapped_lines = wrap(line.strip(), width=80)
                for wrapped_line in wrapped_lines:
                    c.drawString(72, y, wrapped_line)
                    y -= 14

            # Check if the text exceeds the page height
            if y < 72:
                c.showPage()
                y = height - 72
                c.setFont("Helvetica", 12)

    # Save the PDF
    c.save()

# Generate the CV PDF
create_cv_pdf("Nikolaos_Georgiadis_CV.pdf", "README.md")
