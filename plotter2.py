import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')

# # Plot mean deviations
# plt.figure(figsize=(10, 6))
# plt.bar(df['name'], df['floor_mean'], alpha=0.7, label='Floor Mean Deviation')
# plt.bar(df['name'], df['ceiling_mean'], alpha=0.7, label='Ceiling Mean Deviation')
# plt.xlabel('Room')
# plt.ylabel('Deviation (degrees)')
# plt.title('Mean Deviation of Floor and Ceiling Corners')
# plt.xticks(rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.savefig('/Users/apple/LessonITC/start_project/test_mision/plots/Mean_Deviation.png')
# plt.show()
# Calculate statistics
mean_deviation_stats = df[['floor_mean', 'ceiling_mean']].describe()
max_deviation_stats = df[['floor_max', 'ceiling_max']].describe()
min_deviation_stats = df[['floor_min', 'ceiling_min']].describe()

print('Mean Deviation Statistics:')
print(mean_deviation_stats)
print('\nMax Deviation Statistics:')
print(max_deviation_stats)
print('\nMin Deviation Statistics:')
print(min_deviation_stats)
