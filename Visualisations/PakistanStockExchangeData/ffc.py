# python code


import matplotlib.pyplot as plt

# Data (same as before)
months = ["Feb 2024", "Mar 2024", "Apr 2024", "Jun 2024", "Jul 2024", "Sep 2024", "Oct 2024", "Dec 2024", "Jan 2025", "Feb 2025"]
prices = [271.5, 390, 400, 415, 425, 435, 445, 390, 400, 382]

# Plotting (same as before)
plt.figure(figsize=(12, 6))
plt.plot(months, prices, marker='o', linestyle='-')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Price (PKR)", fontsize=12)
plt.title("FFC Stock Price (2024-2025)", fontsize=14)
plt.grid(True)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Saving the figure
filename = "ffc_stock_price.png"  # Choose your filename and extension (png, jpg, pdf, etc.)
plt.savefig(filename, dpi=300)  # dpi controls the resolution (300 is good for printing)

# Optionally, you can still show the plot:
plt.show()

print(f"Plot saved as {filename}") #Confirmation message
