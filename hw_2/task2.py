from latex_utils.main import generate_table, generate_img, get_document
from pdflatex import PDFLaTeX

table = [
    ["Book", "Author", "Genre", "Rating"],
    ["The Ravens", "Maggie Stiefvater", "Fantasy", "8.5"],
    ["Eat, Pray, Love", "Elizabeth Gilbert", "Prose", "9"],
    ["Only a Monster", "Vanessa Len", "Fantasy", "10"]
]

file_content = get_document(generate_table(table) + "\n" + generate_img("book.png"))
file_path = "artifacts/task2.tex"

with open(file_path, "w") as file:
    file.write(file_content)

pdfl = PDFLaTeX.from_texfile(file_path)
pdf, log, completed_process = pdfl.create_pdf(True, True)

with open("artifacts/task2.pdf", "wb") as file:
    file.write(pdf)