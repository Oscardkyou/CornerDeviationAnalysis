import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')
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

# Save statistics to txt files
mean_deviation_stats.to_csv('/Users/apple/LessonITC/start_project/test_mision/Mean_Deviation_Statistics.txt', sep='\t')
max_deviation_stats.to_csv('/Users/apple/LessonITC/start_project/test_mision/Max_Deviation_Statistics.txt', sep='\t')
min_deviation_stats.to_csv('/Users/apple/LessonITC/start_project/test_mision/Min_Deviation_Statistics.txt', sep='\t')
