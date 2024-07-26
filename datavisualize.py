import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(r'C:\Users\kk\Desktop\All Folders\6th sem\MACHINE LEARNING\final\Breast_cancer_data.csv')


print(data.head())


print("\nStates:")
print(data.describe())


print("\nDataType:")
print(data.dtypes)


print("\nMissValues:")
print(data.isnull().sum())

# warm color is daignosis and blue color is nomral
plt.figure(figsize=(10, 6))
sns.countplot(x='diagnosis', data=data, palette='coolwarm', hue='diagnosis', legend=False)
plt.title('Countof Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.show()
