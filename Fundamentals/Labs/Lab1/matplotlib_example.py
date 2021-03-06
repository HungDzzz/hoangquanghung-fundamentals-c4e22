# only for MAC
# import matplotlib 
# matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1. prepare data
machine_counts = [18, 4, 2]

# 2. prepare labels
machine_name = ["PC", "MAC", "Linux"]

# 3. Draw pie
pyplot.pie(machine_counts, labels=machine_name, autopct="%.1f%%", shadow=True, explode=[0, 0.1, 0])
pyplot.title("PC vs MAC vs Linux usage")
pyplot.axis("equal")
# 4. show
pyplot.show()