def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    my_dict = {}
    for row in rows:
      row_cells = row.strip().split()
      codon = row_cells[0]
      amino_acid_abbrev = row_cells[2]
      my_dict[codon] = amino_acid_abbrev
    return my_dict
