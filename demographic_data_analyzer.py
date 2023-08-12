import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the data from the env
    df = pd.read_csv('adult.data.csv')

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
    average_age_men = float(f'{age_men:.1f}')

    # What if the precentage of people who have a Banchelor's Degree?
    banchelors = df[df['education'] == 'Bachelors']
    percentage_banchelors = float(f'{(len(banchelors) / len(df)) * 100:.1f}')

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`)
    # make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    sample_higher = higher_education[higher_education['salary'] == '>50K']
    sample_lower = lower_education[lower_education['salary'] == '>50K']
    higher_education_rich = float(f'{(len(sample_higher) / len(higher_education)) * 100:.1f}')
    lower_education_rich = float(f'{(len(sample_lower) / len(lower_education)) * 100:.1f}')
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50k?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    earn_by_country = df[df['salary'] == '>50K'].value_counts(df['native-country'])
    pop_per_native_country = df['native-country'].value_counts()
    result = earn_by_country / pop_per_native_country
    highest_earning_country = result.index[result == max(result)][0]
    highest_earning_country_percentage = float(f'{(max(result)) * 100:.1f}')

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax())

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_banchelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_banchelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
       highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()