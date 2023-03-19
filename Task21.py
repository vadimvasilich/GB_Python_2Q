# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dict_list =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}] 

all_vals = set()
for into_dict in dict_list:
    val_set = set(into_dict.values())
    
    all_vals |= val_set # (|) = unit.
    
    
print(all_vals)