import matplotlib.pyplot as plt

# Data for the top 10 greenhouse gas emitting countries in 2020 (in MtCO₂e)
countries = [
    "China", "United States", "India", "Russia", "Japan", 
    "Brazil", "Indonesia", "Germany", "Iran", "Canada"
]
emissions = [11680, 5030, 2910, 2120, 1210, 1160, 975, 738, 720, 670]

# Create the bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(countries, emissions, color='skyblue')

# Add emission values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), 
             ha='center', va='bottom', fontsize=12)

# Customize the plot
plt.title('Top 10 Greenhouse Gas Emitting Countries in 2020', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Emissions (MtCO₂e)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
