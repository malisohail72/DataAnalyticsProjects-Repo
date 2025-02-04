import matplotlib.pyplot as plt
import pandas as pd

# Create dataset
data = [
    {"monthYear": "January 2024", "price": 105},
    {"monthYear": "February 2024", "price": 108},
    {"monthYear": "March 2024", "price": 112},
    {"monthYear": "April 2024", "price": 143},
    {"monthYear": "May 2024", "price": 149},
    {"monthYear": "June 2024", "price": 155},
    {"monthYear": "July 2024", "price": 166},
    {"monthYear": "August 2024", "price": 185},
    {"monthYear": "September 2024", "price": 210},
    {"monthYear": "October 2024", "price": 254},
    {"monthYear": "November 2024", "price": 298},
    {"monthYear": "December 2024", "price": 316},
    {"monthYear": "January 2025", "price": 347},
    {"monthYear": "February 2025", "price": 380},
]

# Create DataFrame
df = pd.DataFrame(data)

# Configure plot
plt.figure(figsize=(14, 7))
plt.plot(df["monthYear"], df["price"], marker="o", linestyle="-", color="#2E86C1")

# Customize plot
plt.title("FFC Average Stock Price (2024-2025)", fontsize=14, pad=20)
plt.xlabel("Month-Year", fontsize=12, labelpad=15)
plt.ylabel("Price (PKR)", fontsize=12, labelpad=15)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)

# Add data labels
for x, y in zip(df["monthYear"], df["price"]):
    plt.text(x, y, f'{y}', ha='center', va='bottom', fontsize=9)

# Save and show plot
plt.tight_layout()
plt.savefig("FFC_Stock_Prices_Chart.png", dpi=300, bbox_inches="tight")
plt.show()
