# test file for reportGeneration.py
# create json object and try reportSum function
# this test does not use REST API
# it just calls the function directly with test data to verify functionality

from reportGeneration import reportSum

# test data
data = {
    "report":
    {
        "title": "Report Title",
        "operation": "sum",
        "operation_field": "Cost",
        "filter_field": "Task Name",
        "filter_value": "HVAC",
        "date_field": "Last Performed Date",
        "date_range": {
            "from": "2026-02-01",
            "to": "2026-02-14"
        }
    },
    "data": [
        {
            "id": "task-001",
            "Task Name": "Sprinkler Winterization",
            "Task Description": "Drain lines and shut off water",
            "Vendor": "Eugene Sprinkler Service",
            "Part details": "",
            "Frequency": "annual",
            "Cost": "75",
            "Last Performed Date": "2025-10-15"
        },
        {
            "id": "task-002",
            "Task Name": "Sprinkler Service Spring",
            "Task Description": "Turn on water and check for damage",
            "Vendor": "Eugene Sprinkler Service",
            "Part details": "",
            "Frequency": "annual",
            "Cost": "100",
            "Last Performed Date": "2025-04-15"
        },
        {
            "id": "task-003",
            "Task Name": "HVAC Maintenance",
            "Task Description": "Service HVAC system",
            "Vendor": "Marshall's",
            "Part details": "",
            "Frequency": "annual",
            "Cost": "220",
            "Last Performed Date": "2025-06-01"
        },
        {
            "id": "task-004",
            "Task Name": "HVAC Filter Change",
            "Task Description": "Change HVAC filter",
            "Vendor": "AprilAire",
            "Part details": "M113",
            "Frequency": "biannual",
            "Cost": "60",
            "Last Performed Date": "2025-05-01"
        },
        {
            "id": "task-005",
            "Task Name": "Fireplace Maintenance",
            "Task Description": "Service fireplace",
            "Vendor": "Marshall's",
            "Part details": "",
            "Frequency": "annual",
            "Cost": "200",
            "Last Performed Date": "2025-02-01"
        },
        {
            "id": "task-006",
            "Task Name": "Hot Water on Demand Maintenance",
            "Task Description": "Service hot water on demand unit",
            "Vendor": "Marshall's",
            "Part details": "",
            "Frequency": "annual",
            "Cost": "120",
            "Last Performed Date": "2025-02-01"
        },
        {
            "id": "task-007",
            "Task Name": "Roof and Gutter Cleaning",
            "Task Description": "Blow off roof, apply moss treatment, "
            "clean gutters",
            "Vendor": "Fly By Might",
            "Part details": "",
            "Frequency": "annual",
            "Cost": "450",
            "Last Performed Date": "2025-10-01"
        }
    ]
}

# test reportSum function
print(reportSum(data))
