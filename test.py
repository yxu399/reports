# test file for reportGeneration.py
# create json object and try reportSum function


from reportGeneration import reportSum
import requests
import json

BASE_URL = "http://localhost:5001"

# test data
test_data = {
    "report":
    {
        "title": "Report Title",
        "operation": "sum",
        "operation_field": "Cost",
        "filter_field": "Task Name",
        "filter_value": "",
        "date_field": "Last Performed Date",
        "date_range": {
            "from": "2025-01-01",
            "to": "2025-12-31"
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

print("=" * 60)
print("Testing Report Generator Microservice")
print("=" * 60)

# Test 1: Basic report (all data)
print("\nTest 1.0: Sum all costs")
response = requests.post(f"{BASE_URL}/report", json=test_data)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    total = result.get('result', 0)
    print(f"Result: ${total}")
    # 75 + 100 + 220 + 60 + 200 + 120 + 450 = 1225
    print(f"Expected: $1225")
    print("✓ PASS" if total == 1225 else "FAIL")
else:
    print(f"✗ FAIL - Error: {response.text}")

# Test 1.1: Basic report (all data) for mean
print("\nTest 1.1: Average all costs")
test_data['report']['operation'] = 'mean'
response = requests.post(f"{BASE_URL}/report", json=test_data)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    total = result.get('result', 0)
    print(f"Result: ${total}")
    # (75 + 100 + 220 + 60 + 200 + 120 + 450)/7 = 175
    print(f"Expected: $175")
    print("✓ PASS" if total == 175 else "FAIL")
else:
    print(f"✗ FAIL - Error: {response.text}")

# Test 2: Sum HVAC costs only (filtered)
print("\nTest 2: Sum HVAC costs only")
test_data['report']['filter_value'] = 'HVAC'
response = requests.post(f"{BASE_URL}/report", json=test_data)

if response.status_code == 200:
    result = response.json()
    total = result.get('result', 0)
    print(f"Result: ${total}")
    # HVAC Maintenance (220) + HVAC Filter Change (60) = 280
    print(f"Expected: $280")
    print("✓ PASS" if total == 280 else "FAIL")
else:
    print(f"✗ FAIL - Error: {response.text}")

# Test 3: Sum costs from May-June 2025 (date filter, no category filter)
print("\nTest 3: Sum costs from May-June 2025")
test_data['report']['filter_value'] = ''  # Remove category filter
test_data['report']['date_range'] = {
    "from": "2025-05-01",
    "to": "2025-06-30"
}
response = requests.post(f"{BASE_URL}/report", json=test_data)

if response.status_code == 200:
    result = response.json()
    total = result.get('result', 0)
    print(f"Result: ${total}")
    # HVAC Filter Change (60, May 1) + HVAC Maintenance (220, June 1) = 280
    print(f"Expected: $280")
    print("✓ PASS" if total == 280 else "FAIL")
else:
    print(f"✗ FAIL - Error: {response.text}")

# Test 4: Error handling - missing data field
print("\nTest 4: Error handling - missing data field")
bad_request = {"report": {"operation": "sum"}}  # Missing 'data'
response = requests.post(f"{BASE_URL}/report", json=bad_request)
print(f"Status Code: {response.status_code}")
print("✓ PASS" if response.status_code == 400 else "FAIL")




print("\n" + "=" * 60)
print("Testing Complete!")
print("=" * 60)
