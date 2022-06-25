import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#reading in the data
def create_panda_frame(filename):
    """create panda dataframe of csv file with ';' as separator"""
    with open(filename, encoding='utf-8') as datafile:
        df = pd.read_csv(datafile, index_col=0, sep=';')
        return df

student_dataframe = create_panda_frame('student_data.csv')

#plot how many students were enrolled in which year
data1 = create_panda_frame('student_data.csv')
df = data1.groupby('Year')[["Master", "Bachelor", "Doctorate"]].sum()

sns.lineplot(data=df, palette = "dark")
plt.title("Students")
plt.show()

#plotting student of the year 2021/22
data1 = create_panda_frame('student_data.csv')
year = data1.loc['2021/22']
year.groupby(by = 'ISCED Field', as_index = False).sum()
year = year.assign(Sum = year['Bachelor'] + year["Master"] + year["Doctorate"])
sns.set(rc = {'figure.figsize':(10,20)})
ax = sns.barplot(x="Sum", y="ISCED Field", data=year,  ci = None)

#gender distribution of students in humanities fields
data2 = pd.read_csv("student_data.csv", encoding = "utf-8", sep=';')
comparison = data2[data2["ISCED Field"].isin(["Political sciences and civics", "Psychology",
                                              "History and archaeology", "Economics", "Law"])]
comparison['Number of students'] = comparison.sum(axis=1)
comparison = comparison.loc[:, ~comparison.columns.isin(['Bachelor', 'Master', "Doctorate"])]
print(comparison)


plot = sns.FacetGrid(data = comparison, col = "Sex", hue = "ISCED Field", palette = "tab10")
plot.map(sns.lineplot, "Year", "Number of students")
plot.add_legend()

plot.set_xticklabels(rotation=45)
plt.show()