# Using Pandas to look at Pandemic Data


The script and supporting files in this repository are intended to show how the Python Pandas module can be used to analyze data, in particular COVID-19 data.

Im going to recommend 3 data sets to "investigate":

- [WHO](https://who.sprinklr.com/) (Download from 06 April 2020)
- [CSSEGISandData on GitHub](https://github.com/CSSEGISandData)
- [New York Times US Data GitHub Repository](https://github.com/nytimes/covid-19-data)



## WHO Data

The repository comes with the WHO data file from 06 April 2020 (WHO-COVID-19-global-data.csv).   

To download the latest file go to the [Who Overview Map](https://who.sprinklr.com) and download the Map Data from the link on the lower right hand side.

This CSV file will need clean up.  Remove spaces from column titles.  Some rows have spaces in the country names and so spaces have shifted columns (Belize and Palestine).  You will need to combine the name and shift the data back to the correct columns.  Welcome to the world of data.

![who_download_2020-04-06_11-45-54](./images/who_download_2020-04-06_11-45-54.jpg)









## Script

The ***todays_totals.py*** script will give you an idea of how to load pandemic data into a Pandas data frame and interrogate the data.  Executing it with the ***-h*** option will give you help on the options.

```python
(pandas) Claudias-iMac:pandas_for_pandemic_data claudia$ python todays_totals.py -h
usage: todays_totals.py [-h] [-d DAILY_REPORTS_FOLDER] [-c COUNTRY_REGION]
                        [-p PROVINCE_STATE] [-s SPECIFIC_DAY] [-f FIPS] [-w]
                        [-t] [-n]

Script Description

optional arguments:
  -h, --help            show this help message and exit
  -d DAILY_REPORTS_FOLDER, --daily_reports_folder DAILY_REPORTS_FOLDER
                        Set path to CSSE Dailty Report folder
                        csse_covid_19_daily_reports. Default is ./COVID-19/css
                        e_covid_19_data/csse_covid_19_daily_reports
  -c COUNTRY_REGION, --country_region COUNTRY_REGION
                        Filer on 2 letter Country Region. Example: "US"
  -p PROVINCE_STATE, --province_state PROVINCE_STATE
                        Filer on Province State. Example: "California"
  -s SPECIFIC_DAY, --specific_day SPECIFIC_DAY
                        File for specific day. Example: 04-01-2020
  -f FIPS, --fips FIPS  FIPS County Code Example: 06037 (Los Angeles County)
  -w, --who_data_file   Analyze the WHO data file provided
  -t, --today_csse      Analyze todays file in the CSSE repo
  -n, --new_york_times  Analyze the New York Times Data

Usage: 'python todays_totals'

```





Running the script without any parameters yields some information on the WHO data set from 6 April which is part of the repository.   This information includes:

A description of the data frame including some statistical data on the numeric values.

The rows and 



```
(pandas) Claudias-iMac:pandas_for_pandemic_data claudia$ python todays_totals.py


====================  DATA FRAME CHECK ====================
====================  WHO Data Frame from WHO-COVID-19-global-data.csv ====================


== Describe the Data Frame: 
            Deaths  CumulativeDeaths     Confirmed  CumulativeConfirmed
count  6786.000000       6786.000000   6786.000000          6786.000000
mean      9.971412        104.946360    178.487179          2313.689213
std      73.268455        761.569677   1183.935476         12918.006118
min       0.000000          0.000000      0.000000             1.000000
25%       0.000000          0.000000      0.000000             4.000000
50%       0.000000          0.000000      2.000000            26.000000
75%       0.000000          3.000000     25.000000           235.000000
max    2003.000000      15889.000000  33510.000000        307318.000000

== Shape of the Data Frame: 
(6786, 8)

== SAMPLE (first and last 5 rows):
       day Country  CountryName Region  Deaths  CumulativeDeaths  Confirmed  CumulativeConfirmed
0  2/25/20      AF  Afghanistan   EMRO       0                 0          1                    1
1  2/26/20      AF  Afghanistan   EMRO       0                 0          0                    1
2  2/27/20      AF  Afghanistan   EMRO       0                 0          0                    1
3  2/28/20      AF  Afghanistan   EMRO       0                 0          0                    1
4  2/29/20      AF  Afghanistan   EMRO       0                 0          0                    1
         day Country CountryName Region  Deaths  CumulativeDeaths  Confirmed  CumulativeConfirmed
6781  4/2/20      ZW    Zimbabwe   AFRO       0                 1          0                    8
6782  4/3/20      ZW    Zimbabwe   AFRO       0                 1          0                    8
6783  4/4/20      ZW    Zimbabwe   AFRO       0                 1          1                    9
6784  4/5/20      ZW    Zimbabwe   AFRO       0                 1          0                    9
6785  4/6/20      ZW    Zimbabwe   AFRO       0                 1          0                    9

== Column Headings of the data set: 
['day' 'Country' 'CountryName' 'Region' 'Deaths' 'CumulativeDeaths'
 'Confirmed' 'CumulativeConfirmed']


== Column default data type: 
day                    object
Country                object
CountryName            object
Region                 object
Deaths                  int64
CumulativeDeaths        int64
Confirmed               int64
CumulativeConfirmed     int64
dtype: object


== Number of MISSING values in each column:
day                     0
Country                85
CountryName             0
Region                 62
Deaths                  0
CumulativeDeaths        0
Confirmed               0
CumulativeConfirmed     0
dtype: int64

== Sum just the numeric columns in the Data Frame:
Deaths                    67666
CumulativeDeaths         712166
Confirmed               1211214
CumulativeConfirmed    15700695
dtype: int64
(pandas) Claudias-iMac:pandas_for_pandemic_data claudia$ 

```

