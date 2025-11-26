fire_cells = input()
total_water = int(input())
effort = 0
put_out_cells = []
fires = fire_cells.split("#")
for fire in fires:
   fire_intensity, value = fire.split(" = ")
   if total_water > 0:
       if fire_intensity == "High" and 81 <= int(value) <= 125:
           if total_water >= int(value):
               total_water -= int(value)
               effort += int(value) * 0.25
               put_out_cells.append(int(value))
       elif fire_intensity == "Medium" and 51 <= int(value) <= 80:
           if total_water >= int(value):
               cell_is_valid = True
               total_water -= int(value)
               effort += int(value) * 0.25
               put_out_cells.append(int(value))
       elif fire_intensity == "Low" and 1 <= int(value) <= 50:
           if total_water >= int(value):
               cell_is_valid = True
               total_water -= int(value)
               effort += int(value) * 0.25
               put_out_cells.append(int(value))

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}\n"
      f"Total Fire: {sum(put_out_cells)}")

