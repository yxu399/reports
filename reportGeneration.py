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
    filter_value = dfSpecs['filter_value'][0]

    # filter dataframe based on filter field
    #   if there's a value in filter_value,
    #   create dfFiltered dataframe containing filtered rows
    if filter_value and len(str(filter_value)) > 0:
        filter_field = dfSpecs['filter_field'][0]
        dfFiltered = dfData[
            dfData[filter_field].astype(str).str.contains(
                str(filter_value), na=False)
        ]
    #   if field is empty, don't filter,
    #       copy original dataframe to dfFiltered for sum operation
    else:
        dfFiltered = dfData

    return dfFiltered
# end filterData

def filterByDateRange(dfData, dfSpecs):
    """ Filter data by date range. """
    date_field = dfSpecs['date_field'][0]
    
    # Only filter if date_field is specified
    if pd.notna(date_field) and len(str(date_field)) > 0:
        date_from = pd.to_datetime(dfSpecs['from'][0])
        date_to = pd.to_datetime(dfSpecs['to'][0])
        
        # Convert date column to datetime
        dfData[date_field] = pd.to_datetime(dfData[date_field])
        
        # Filter by range
        dfData = dfData[
            (dfData[date_field] >= date_from) & 
            (dfData[date_field] <= date_to)
        ]
    
    return dfData

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

    # apply date range filter
    dfFiltered = filterByDateRange(dfFiltered, dfSpecs)

    # perform sum operation on column specified in operation_field
    sumField = dfSpecs['operation_field'][0]
    sumValue = (dfFiltered[sumField].astype(int).sum())

    # Create json object containing report data
    reportData = {
        "title": dfSpecs['title'][0],
        "operation": dfSpecs['operation'][0],
        "operation_field": sumField,
        "filter_field": dfSpecs['filter_field'][0],
        "filter_value": dfSpecs['filter_value'][0],
        "date_field": dfSpecs['date_field'][0],
        "date_range": {
            "from": dfSpecs['from'][0],
            "to": dfSpecs['to'][0]
        },
        "result": int(sumValue)  # Changed from "sum" to "result" for consistency
    }

    # return results
    return reportData
# end reportSum
