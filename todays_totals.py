#!/usr/bin/python -tt
# Project: covid19
# Filename: todays_totals
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "4/4/20"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
import pandas as pd
import datetime
import os
import re


def load_flu_rates_2018_19():

    # https://www.cdc.gov/flu/about/burden/2018-2019.html
    # Estimated rates of influenza-associated disease outcomes,
    # per 100,000, by age group — United States, 2018-2019 influenza season

    fn = 'cdc_flu_rates_by_age_2018_2019.csv'

    df_pastflu = df_from_csv(fn)

    # df_pastflu['Illness rate Estimate'] = df_pastflu['Illness rate Estimate'].astype('float64')
    # df_pastflu['Medical visit rate Estimate'] = df_pastflu['Medical visit rate Estimate'].astype('float64')
    # df_pastflu['Hospitalization rate Estimate'] = df_pastflu['Hospitalization rate Estimate'].astype('float64')
    # df_pastflu['Mortality rate Estimate'] = df_pastflu['Mortality rate Estimate'].astype('float64')

    df_check(df_pastflu, "CDC Estimated rates of influenza-associated disease outcomes,per 100,000, by age group")

def get_todays_date_utc():
    # from datetime import datetime, timezone
    # "%Y%m%d"  20200404
    tdy = datetime.datetime.now(datetime.timezone.utc).strftime("%m-%d-%Y")
    # print(tdy)
    return tdy

def find_file_in_dir(dir, fname, debug=False):

    print(f"\tFUNCTION find_file_in_dir: Looking for file {fname} in directory: \n\t{dir}")
    found_file_name = ''

    # root, dirs, files = os.walk(dir)

    files = os.scandir(dir)

    # for root, dirs, files in os.walk(dir):
    #     print(f"{root} {dirs} {files}")

    for f in files:
        # print(f.name)
        if re.search(fname, f.name, re.IGNORECASE):
            found_file_name = f
            break

    if found_file_name:
        print(f"\tReturning: {found_file_name}\n")
    else:
        print(f"\t****** WARNING FILE NOT FOUND: File {fname} *****")
    return found_file_name


def df_from_csv(path):
    """
    Create Pandas Data Frame from given Excel file
    :param path:
    :return:  Pandas Data Frame from Excel file
    """

    try:
        data_frame = pd.read_csv(path)

    except IOError:
        exit(f"ERROR!!! Failed to read Excel file: \n\t{path}\nABORTING PROGRAM Execution."
             f"\nConfirm a valid file and correct path have been provided.")

    # Return the data frame object created from the Excel file
    return data_frame


def df_check(dfc, note="DATA FRAME CHECK", debug=False):

    print(f"\n\n====================  DATA FRAME CHECK ====================")
    print(f"====================  {note} ====================\n")
    print(f"\n== Describe the Data Frame: \n{dfc.describe()}")
    print(f"\n== Shape of the Data Frame: \n{dfc.shape}")

    print(f"\n== SAMPLE (first and last 5 rows):")
    print(dfc.head())
    print(dfc.tail())

    print(f"\n== Column Headings of the data set: \n{dfc.columns.values}\n")

    print(f"\n== Column default data type: \n{dfc.dtypes}\n")

    # Whitespace Check on Country_Region
    # _ = df.loc[df.Country_Region.str.contains(r'\s$', regex=True)]

    print("\n== Number of MISSING values in each column:")
    print(dfc.isna().sum())
    # print()
    print("\nSum all the columns in the Data Frame")
    print(dfc.sum())

    print("\n== Sum just the numeric columns in the Data Frame:")
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    dfc_num = dfc.select_dtypes(include=numerics)
    print(dfc_num.sum())

    # print("\nValue Counts")
    # print("\nCountry_Region")
    # print(dfc.Country_Region.value_counts())
    # print("\nProvince_State")
    # print(dfc.Province_State.value_counts())


    # print("Missing Country_Region data:")
    # print(dfc['Country_Region'].isna().sum())
    # print(dfc['Country_Region'].isnull().sum())
    #
    #
    # print("Missing Province_State data:")
    # print(dfc['Province_State'].isna().sum())
    # print(dfc['Province_State'].isnull().sum())

    if len(dfc) == 0:
        print(f"WARNING:  Empty data frame. \nThere is no data for {note}\n")


def main():

    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

    #######################################################################
    # ### DEFAULT WHO file is analyzed by default

    # If a new file path and name are provided with the -w option
    # then that file will be loaded into a Pandas data frame and analyzed
    # otherwise the default file from 6 April 2020 will which is included in the
    # repository will be analyzed.
    if arguments.who_data_file:
        who_default_datafile = arguments.who_data_file
    else:
        who_default_datafile = "WHO-COVID-19-global-data.csv"

    df_who = df_from_csv(who_default_datafile)
    df_check(df_who, f"WHO Data Frame from {who_default_datafile}")

    if arguments.country_region:
        print(f"\n\n========= Country Data for {arguments.country_region}")
        # Mask Data Frame
        df_country_bool = df_who['Country'] == arguments.country_region
        df_country = df_who[df_country_bool]
        df_check(df_country, f"{arguments.country_region}")


    #######################################################################
    ## Todays CSSE JHU data set
    # This section of the script will look for todays daily file for analysis
    # If todays is not found it will automaticaly look for yesterdaysn
    # Important:  The Path to the https://github.com/CSSEGISandData/COVID-19.git repository must be set.
    # It is assumed that the CSSE JHU repo will be cloned directly under this repository

    if arguments.today_csse:

        if arguments.specific_day:
            day = arguments.specific_day
        else:
            # Look for the most recent file - Start with Todays file
            day = get_todays_date_utc()

        print(f"\n=========== Looking for data file: {day}")
        found_file = find_file_in_dir(arguments.daily_reports_folder, f"{day}.csv")

        if found_file:
            print(f"\nFound requested file is {found_file} with name {found_file.name}")
        else:
            yesterday = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1)
            ytdy = yesterday.strftime("%m-%d-%Y")
            print(f'File {day} was not found. Lets look for the previous days file {ytdy} of type {yesterday}.')
            found_file = find_file_in_dir(arguments.daily_reports_folder, f"{ytdy}.csv")
            print(f"\nFound calculated file is {found_file} with name {found_file.name}")
            day = ytdy

        df = df_from_csv(found_file.path)
        df_check(df, f"Data for {day}")

        if arguments.country_region:
            print(f"\n\n========= Country Data for {arguments.country_region}")
            # Mask Data Frame
            df_country_bool = df['Country_Region'] == arguments.country_region
            df_country = df[df_country_bool]
            df_check(df_country, f"{arguments.country_region}")

        if arguments.province_state:
            print(f"\n\n========= State/Province Data for {arguments.province_state} ")
            df_country_state_bool = df['Province_State'] == arguments.province_state
            df_country_state = df[df_country_state_bool]
            df_check(df_country_state, f"{arguments.province_state}")

        # FIPS
        if arguments.fips:
            print(f"\n\n========= FIPS County {arguments.fips} ")
            df_fips_bool = df['FIPS'] == int(arguments.fips)
            df_fips = df[df_fips_bool]
            df_check(df_fips, f"{arguments.fips}")


    #######################################################################
    if arguments.new_york_times:
        print(f"\n\n========= New York Times Data file from NYT GitHub Repo ")
        ny_state_data = os.path.join(".", "covid-19-data", "us-states.csv")
        dfnystate = df_from_csv(ny_state_data)
        df_check(dfnystate, f"New York Times Data")



# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python todays_totals' ")

    parser.add_argument('-d', '--daily_reports_folder',
                        help='Set path to CSSE Dailty Report folder csse_covid_19_daily_reports.  '
                             'Default is ./COVID-19/csse_covid_19_data/csse_covid_19_daily_reports',
                        action='store',
                        default='./COVID-19/csse_covid_19_data/csse_covid_19_daily_reports')

    parser.add_argument('-c', '--country_region', help='Filer on 2 letter Country Region. Example: "US" ',
                        action='store')

    parser.add_argument('-p', '--province_state', help='Filer on Province State. Example: "California" ',
                        action='store')

    parser.add_argument('-s', '--specific_day', help='File for specific day. Example:  04-01-2020',
                        action='store')

    parser.add_argument('-f', '--fips', help='FIPS County Code Example: 06037 (Los Angeles County)',
                        action='store')

    parser.add_argument('-w', '--who_data_file', help='Analyze the WHO data file provided',
                        action='store_true', default=False)

    parser.add_argument('-t', '--today_csse', help='Analyze todays file in the CSSE repo',
                        action='store_true', default=False)

    parser.add_argument('-n', '--new_york_times', help='Analyze the New York Times Data',
                        action='store_true', default=False)
    arguments = parser.parse_args()
    main()
