from hw_2.latex_generation.latex_utils.main import generate_table, get_document

table = [
    ["Book", "Author", "Genre", "Rating"],
    ["The Ravens", "Maggie Stiefvater", "Fantasy", "8.5"],
    ["Eat, Pray, Love", "Elizabeth Gilbert", "Prose", "9"],
    ["Only a Monster", "Vanessa Len", "Fantasy", "10"]
]

file_content = get_document(generate_table(table))

with open("artifacts/task1.tex", "w") as file:
    file.write(file_content)