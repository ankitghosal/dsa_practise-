import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

batch_size = 20 # 20 providers per batch
max_batches = 10 # Only show 10 batches (200 providers)
sorted_providers = final_df_copy['Provider'].value_counts().index

# Ensure we don't exceed available providers
num_batches = min(max_batches, int(np.ceil(len(sorted_providers)/batch_size)))

# Loop we don't exceed available providers
for i in range(num_batches):
    batch_providers = sorted_providers[i * batch_size: (i + 1) * batch_size]  # Select 20 providers
    plt.figure(figsize=(16,6))
    sns.countplot(data=final_df_copy, x='Provider', hue='PotentialFraud', order=batch_providers)

    plt.xticks(rotation=90)
    plt.title(f'Provider Distribution (Batch {i + 1})')
    plt.show()