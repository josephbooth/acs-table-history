## Starting a new python project "Table History" that uses the US Census Bureau's public API.

## Problem:
It is difficult to determine the history of groups (tables) that appear in the API. Meaning, if I want to research when a table first appeared or was added to the API I have to manually go through the datasets to determine this information.

## Idea: 
To use Python to access API endpoints to gather information programmatically and produce an HTML file or series of linked HTML files to use as a research tool. The content in the HTML file will allow a user to click on a group (table) name and to see the history of the table such as; year first appeared in API, year table does not appear, description content variations and a list of all years the table appears. It might be useful to have an HTML page that presents a table with each year as a header column and rows with the description from the /groups.json data.

## User Journey:
A user opens up an HTML page named "Table History" and is presented with a text input box that allows for entry of a single US Census Bureau group (table) id; such as B18104 or S2419.

On this page - a user is also presented with two check box controls. One check box is labeled "1 Year" and the other is labeled as "5 Year".

The user has traveled to this page because they need information about:

 - The number of years this table appears in the api
 - What are the different "name" values this table has over time
 - What are the different "description" values this table has over time
 - A list of all years this table does appear
 - A list of all years this table does not appear

## Scope of years to scan:
In this document you will see {YEAR} as a variable in the api endpoint url. I am assuming that the python code will loop through all available datasets for acs1 or acs5 year.

Just a note: the api uses c_vintage for "year". This document uses "year" interchangeably with "c_vintage".

At this API endpoint: https://api.census.gov/data.json 

Using https://api.census.gov/data.json provides all of the information about the dataset (acs1 or acs5) and all of the years that data is published. This solution must use all available years in order to provide the user with history information.

If a dataset year is missing, the code should gracefully skip it rather than fail. There are some cases where a dataset will not have a year available.

It appears that this endpoint provides a list of dictionaries for all of the datasets in the entire census api. Use the properties: "c_vintage", "c_dataset", "c_groupsLink", "title" and "distribution" has an "accessURL" in the dictionary that can be useful for this project.

 - c_vintage provides the year for the data product
 - c_dataset a dictionary to look for "acs1" or "acs5". And the data product name is in here.
 - c_groupsLink lists of all the groups (tables) in the 
 - title provides the name of the data product
 - distribution [accessURL] is the root endpoint for the data product within the api

.json snippets for different data products:

  Detailed Tables are:
      "c_dataset": [
        "acs",
        "acs1"
      ]

  Comparison Profiles are:
      "c_dataset": [
        "acs",
        "acs1",
        "cprofile"
      ]

  Data Profiles are:
      "c_dataset": [
        "acs",
        "acs1",
        "profile"
      ]

  Selected Population Profiles are:
      "c_dataset": [
        "acs",
        "acs1",
        "spp"
      ]

  Subject Tables are:
      "c_dataset": [
        "acs",
        "acs1",
        "subject"
      ]

For some reason, the US Census Bureau does not label "Detailed Tables" in the c_dataset property. It is the only data product with an array with only two items in the list of strings. In order to check tables that are in Detailed Tables data products you need to know this caveat.


## Information about datasets:
In the api url there are parts of the path that indicate the dataset. Notice in the endpoints to target section that the /acs1 and /acs5 values. The acs1 is for the one year datasets and the acs5 is for five year datasets.

For this example: 

 - https://api.census.gov/data/{YEAR}/acs/acs1.json
 - https://api.census.gov/data/{YEAR}/acs/acs5.json

acs1 are datasets for one year data and acs5 are for five year data.

## Data Products within the 1 Year /acs1 dataset:

The ACS 1-year estimates are available for the nation, all states, the District of Columbia, Puerto Rico, all congressional districts and metropolitan statistical areas, and all counties and places (i.e., towns or cities) with populations of 65,000 or more.

 - Detailed Tables contain the most detailed estimates on all topics for all geographies. The data are presented as estimates.
 - Subject Tables provide a span of information on a particular ACS subject presented in the format of both estimates and percentages.
 - Data Profiles contain broad social, economic, housing, and demographic information. The data are presented as estimates and percentages.
 - Comparison Profiles are similar to Data Profiles but also include comparisons with past-year data. The current year data are compared with each of the last four years of data and include statistical significance testing.
 - Selected Population Profiles provide broad statistics for population subgroups by race, ethnicity, ancestry, tribal affiliation, and place of birth. The data are presented as estimates and percentages.

 - Detailed Tables endpoint: http://api.census.gov/data/{YEAR}/acs/acs1
 - Subject Tables endpoint: http://api.census.gov/data/{YEAR}/acs/acs1/subject
 - Data Profiles endpoint: http://api.census.gov/data/{YEAR}/acs/acs1/profile
 - Comparison Profiles endpoint: http://api.census.gov/data/{YEAR}/acs/acs1/cprofile
 - Selected Population Profiles endpoint: http://api.census.gov/data/{YEAR}/acs/acs1/spp

## Data Products within the 5 Year /acs5 dataset:

The ACS 5-year estimates are available for the nation, all states, the District of Columbia, Puerto Rico, all congressional districts and metropolitan statistical areas, counties, places (i.e., towns or cities), ZIP Code Tabulation Areas, census tracts, and block groups.

 - Detailed Tables contain the most detailed estimates on all topics for all geographies. The data are presented as estimates. Detailed Tables are available down to the block group level.
 - Subject Tables provide a span of information on a particular ACS subject presented in the format of both estimates and percentages. Subject Tables are available down to the census tract level.
 - Data Profiles contain broad social, economic, housing, and demographic information. The data are presented as estimates and percentages. Data Profiles are available down to the census tract level.
 - Comparison Profiles are similar to Data Profiles but also include comparisons with past-year data. The current 5-year data are compared with the preceding non-overlapping 5-year data (e.g. 2019-2023 ACS 5-year estimates compared to 2014-2018 ACS 5-year estimates) and include statistical significance testing. Comparison Profiles are available down to the places/county subdivisions level.

 - Detailed Tables endpoint: http://api.census.gov/data/{YEAR}/acs/acs5
 - Subject Tables endpoint: http://api.census.gov/data/{YEAR}/acs/acs5/subject
 - Data Profiles endpoint: http://api.census.gov/data/{YEAR}/acs/acs5/profile
 - Comparison Profiles endpoint: http://api.census.gov/data/{YEAR}/acs/acs5/cprofile

## Endpoint to find information about the groups (tables):

Example: 1 Year Subject Tables
Using this endpoint: http://api.census.gov/data/{YEAR}/acs/acs1/subject.json

There is a "dataset" property that contains a "c_groupsLink" property that provides an endpoint URL for the group (table) name and description. In this example the endpoint url is: http://api.census.gov/data/{YEAR}/acs/acs1/subject/groups.json

The /groups.json endpoint returns a dictionary of "groups" with "name" and "description" key: value paris.

## Content to be collected during the processing of the endpoints:

For each dataset (acs1 or acs5) collect the group (table) name and description for each data product.
