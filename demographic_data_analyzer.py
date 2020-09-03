import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count().sort_values(ascending=False)

    # What is the average age of men?
    mens = df[df['sex'] == 'Male']
    average_age_men = mens['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    # num_with_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    # or
    num_with_bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((num_with_bachelors / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`)
    # make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    advanced_ed = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    advanced_ed_rich = advanced_ed[advanced_ed['salary'] == '>50K']

    low_ed = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    low_ed_rich = low_ed[low_ed['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = round((len(advanced_ed_rich) / len(advanced_ed)) * 100, 1)
    lower_education_rich = round((len(low_ed_rich) / len(low_ed)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work = df[df['hours-per-week'] == min_work_hours]
    min_work_with_big_salary = df[(df['hours-per-week'] == min_work_hours) &
                                  (df['salary'] == '>50K')]

    rich_percentage = round((len(min_work_with_big_salary) / len(min_work)) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    cnt_sal = df[['native-country', 'salary']]
    ppl_in_cnt = cnt_sal.groupby('native-country').count()
    rich_ppl_in_cnt = cnt_sal[cnt_sal['salary'] == '>50K'].groupby('native-country').count()
    rich_2_all = (rich_ppl_in_cnt * 100) / ppl_in_cnt
    top_country = rich_2_all[rich_2_all['salary'] == rich_2_all['salary'].max()]

    highest_earning_country = top_country.index[0]
    highest_earning_country_percentage = round(top_country.iloc[0]['salary'], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    in_occs = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby(['occupation'])['occupation'].agg('count').reset_index(name='Total')
    most_popular_occ = most_popular = in_occs[in_occs['Total'] == in_occs['Total'].max()]
    top_IN_occupation = most_popular_occ.iloc[0]['occupation']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
