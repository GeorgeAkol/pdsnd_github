# The following code was completed by George Akol using the template 
# provided by Udacity
import time
import pandas as pd
import numpy as np
import calendar


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
 
    # Ask the user for the city name until a valid city has been selected
    while True:
            city = str(input("Would you like to see data for Chicago, New York City, or Washington? ")).lower()
            if city in CITY_DATA:
                break
            else:
                print("It seems like you entered an invalid city name! Please try again.\n")
                
    # Ask user the user for a filter period (month, day, both or none)       
    while True:        
            filter_period = str(input("Would you like to filter by month, day, both or continue with no filters (type 'none')? ")).lower()
            if filter_period in ['month', 'day', 'both', 'none']:
                break
            else: 
                print("It seems like you entered an invalid time period! Please try again.\n")
      
    # If applicable, request user to supply valid month filter 
    if filter_period == "month" or filter_period == "both":        
        avail_months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        while True:
            month = str(input("Enter the name of the month you are interested in (Options: Janauary, February, March, April, May, or June): ")).lower()
            if month in avail_months:    
                if filter_period != "both":
                    day = 'all'
                break
            else:
                print("It seems like you entered an invalid day! Please try again.\n")
                       
    # If applicable, request user to supply valid day filter                 
    if filter_period == "day" or filter_period == "both":        
        avail_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        while True:
            day = str(input("Enter the day of the week you are interested in (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")).lower()
            if day in avail_days:
                if filter_period != "both":
                    month = 'all'
                break
            else:
                print("It seems like you entered an invalid day! Please try again.\n")           
                      
    # If no filter is select, select all data         
    elif filter_period == "none":
        month = 'all'
        day = 'all'
   
            
        
    print('-'*40)
        
    return city, month, day
     

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    #We convert the start time column to the datetime format 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #We extract the month and weekday from the start time column
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #If applicable, filter by the chosen month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1    
        df = df[df['month'] == month]
    
    #If applicable, filter by the chosen day
    elif day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    # We return the filtered dataframe
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    #Select and display the most popular month
    pop_month = df['month'].mode()[0]
    print('Most Popular Month: {}'.format(calendar.month_name[pop_month]))

    #Select and display the most common day of week
    pop_weekday = df['day_of_week'].mode()[0]
    print('Most Common day of the week: {}'.format(pop_weekday)) 
    
    #Select and display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: {}'.format(pop_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_most = df['Start Station'].mode()[0]
    print("Most common start station is: {}".format(start_most))
    
    # TO DO: display most commonly used end station
    end_most = df['End Station'].mode()[0]
    print("Most commonly used end station is: {}".format(end_most))
    
    # TO DO: display most frequent combination of start station and end station trip
    #combo_count_idx = df[['Start Station','End Station']].value_counts()
    combo_most = df.groupby(['Start Station','End Station']).size().idxmax()
    #combo = df[combo_count]
    print("Most common combination of start and end stations is: {}".format(combo_most))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #print(df) 
    #df['Trip Duration'] = pd.to_numeric(df['Trip Duration'])

    # Display total travel time (in days, hours and minutes)
    tot_duration = df['Trip Duration'].sum() #df.loc?
    print("The total travel time is: ")
    t_minutes, t_seconds = divmod(tot_duration, 60)
    t_hours, t_minutes = divmod(t_minutes, 60)
    t_days, t_hours = divmod(t_hours, 24)
    
    print("{} days : {} hours : {} minutes : {} seconds".format(t_days, t_hours, t_minutes, t_seconds))
  
    
    # Display average travel time (in days, hours and minutes)
    avg_duration = df['Trip Duration'].mean()
    print("The average travel time is: ")
    a_minutes, a_seconds = divmod(avg_duration, 60)
    a_hours, a_minutes = divmod(a_minutes, 60)
    a_days, a_hours = divmod(a_hours, 24)
    
    print("{} days : {} hours : {} minutes : {} seconds".format(a_days, a_hours, a_minutes, a_seconds))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display the number of user types
    user_count = df['User Type'].value_counts() 
    print("The number of user types are: \n{}\n".format(user_count))
    
    # Display the number of gender types
    if "Gender" in df:
        gender_count = df['Gender'].value_counts()
        print("The number of genders are: \n{}\n".format(gender_count))
    
    else:
        print("There is no gender data available\n")
    
    # Display earliest, most recent, and most common birth years
    if "Birth Year" in df:
        
        early_birth = df['Birth Year'].min()
        print("The earliest birth year is:  {}".format(early_birth))
    
        common_birth = df['Birth Year'].mode()[0]
        print("The most common birth year is:  {}".format(common_birth))
    
        recent_birth = df['Birth Year'].max() 
        print("The most recent birth year is:  {}".format(recent_birth))
        
    else:
        print("There is no birth year data available")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_stats(df):
    """ Asks the user whether they would like to see the raw data, and outputs it in groups of 5 """
    idx = 0
    raw = str(input("Would you like to see the raw data (y or n)? ")).lower()
    
    while True:
        if raw == 'y':
            print(df[idx : idx+5])
            idx += 5
            raw = str(input("Would you like to see more raw data (y or n)? ")).lower()
            
        elif raw =='n':
            break
        
        else:
            print("You did not enter a valid response! Please try again")
        
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
