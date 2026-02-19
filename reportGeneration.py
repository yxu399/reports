# Reports Generator Microservice
# report generation

# use pandas to process data and generate reports
import pandas as pd

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
# end generateReport


def prepareDataframes(data):
    """ Receive data json object.

    Create dataframes for report specs and data from json object.

    Return dataframes.
    """
    # dataframe for "report specs"
    dfSpecs = pd.DataFrame([data['report']])
    # split date_range into two fields and concatenate back to dfSpecs
    dfDateRange = pd.json_normalize(data['report']['date_range'])
    dfSpecs = pd.concat([
        dfSpecs.drop('date_range', axis=1), dfDateRange], axis=1)

    # dataframe for "data", normalize to split nested fields
    dfData = pd.json_normalize(data['data'])

    return dfSpecs, dfData
# end prepareDataframes


def filterData(dfData, dfSpecs):
    """ Receive data and specs dataframes.

    Filter data dataframe based on filter field and value from specs dataframe.

    Return filtered dataframe.
    """
    # filter dataframe based on filter field
    #   if there's a value in filter_value,
    #   create dfFiltered dataframe containing filtered rows
    if len(dfSpecs['filter_value'][0]) > 0:
        filterField = dfSpecs['filter_field'][0]
        filterValue = dfSpecs['filter_value'][0]
        dfFiltered = dfData[
            dfData[filterField].astype(str).str.contains(
                filterValue, na=False)
        ]
    #   if field is empty, don't filter,
    #       copy original dataframe to dfFiltered for sum operation
    else:
        dfFiltered = dfData

    return dfFiltered
# end filterData


def reportSum(data):
    """ Receive data json object.

    Filter for filter field.

    Perform sum operation on specified column using pandas.

    Return results.
    """
    # get dataframes for report specs and data from json object
    dfSpecs, dfData = prepareDataframes(data)

    # for development phase:
    #   print dataframes to verify
    #   test print(dfSpecs)
    print(dfSpecs)
    #   test print(dfData)
    print(dfData)

    # add date range filter here

    # filter data based on filter field
    dfFiltered = filterData(dfData, dfSpecs)

    # perform sum operation on column specified in operation_field
    sumField = dfSpecs['operation_field'][0]
    sumValue = (dfFiltered[sumField].astype(int).sum())

    # Create json object containing report data
    reportData = {
        "report": dfSpecs.iloc[0].to_dict(),
        # "filtered_data": dfFiltered.to_dict('records'),
        "sum": str(sumValue)
    }

    # return results
    return reportData
# end reportSum
