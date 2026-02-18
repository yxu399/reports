# Reports Generator Microservice
# report generation

# use pandas to process data and generate reports
import pandas as pd
from pandas import json_normalize

# pandas settings
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)    # Display all rows


def generateReport(data):
    """ Receive data json object.

    Determine operation from operation field.

    Call appropriate pandas function to process the data

    and generate the report.
    """
    if data['report']['operation'] == "sum":
        return reportSum(data)


def reportSum(data):
    """ Receive data json object.

    Filter for filter field.

    Perform sum operation on specified column using pandas.

    Return results.
    """
    # create dataframes for report specs and data from json object

    # dataframe for "report specs"
    dfSpecs = pd.DataFrame([data['report']])
    # split date_range into two fields and concatenate back to dfSpecs
    dfDateRange = pd.json_normalize(data['report']['date_range'])
    dfSpecs = pd.concat([
        dfSpecs.drop('date_range', axis=1), dfDateRange], axis=1)

    # dataframe for "data", normalize to split nested fields
    dfData = pd.json_normalize(data['data'])

    # test print(dfSpecs)
    print(dfSpecs)
    # test print(dfData)
    print(dfData)

    # filter dataframe based on filter field

    # perform sum operation on specified column

    # Create json object containing report data

    # return results
    return
