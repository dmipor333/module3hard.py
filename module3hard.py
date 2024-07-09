data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def len_all_list(data_structure):
    if isinstance(data_structure, int):
        return data_structure
    if isinstance(data_structure, str):
        return len(data_structure)
    if isinstance(data_structure, list) or isinstance(data_structure, tuple):
        if len(data_structure) == 0:
            return 0
        return len_all_list(data_structure[0]) + len_all_list(data_structure[1:])
    if isinstance(data_structure, set):
        a = 0
        for i in data_structure:
            a += len_all_list(i)
        return a
    if isinstance(data_structure, dict):
        a = 0
        for key, value in data_structure.items():
            a += len_all_list(key) + len_all_list(value)
        return a
result = len_all_list(data_structure)
print(result)


