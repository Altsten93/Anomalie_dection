import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the number of data points
num_points = 1000

# Generate data from three different log-normal distributions
# The parameters (mean, sigma) are for the underlying normal distribution.
# A log-normal distribution is more suitable for price simulation as it's non-negative.

# Column 1: Simulating a volatile price
price_1 = np.random.lognormal(mean=0, sigma=1, size=num_points)

# Column 2: Simulating a more stable price with a higher base
price_2 = np.random.lognormal(mean=3, sigma=0.25, size=num_points)

# Column 3: Simulating a price with occasional small spikes
price_3 = np.random.lognormal(mean=2, sigma=0.2, size=num_points)


# Create a pandas DataFrame
df = pd.DataFrame({
    'price_volatile': price_1,
    'price_stable': price_2,
    'price_spiky': price_3
})

# Plot histograms of the features
print("Generating histograms...")
df.hist(bins=50, figsize=(15, 10))
plt.suptitle('Histograms of Simulated Price Features')
plt.show()


# Save the DataFrame to a CSV file
df.to_csv('simulated_data.csv', index=False)

print("Successfully generated 1000 data points with 3 price features using log-normal distribution and saved to simulated_data.csv")
