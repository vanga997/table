
from main import sparsetable

a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
table = sparsetable()

table.buildSparseTable(a)
table.query(1, 6)
