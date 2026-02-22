# Reports Generator Microservice

A Flask-based microservice for generating reports from JSON data using pandas operations.

## Features

- Sum operations on numeric fields
- Field-based filtering (partial string matching)
- Date range filtering
- RESTful API interface

## Requirements

```bash
pip install flask pandas requests
```

## Quick Start

1. **Start the service:**
   ```bash
   python main.py
   ```
   Service runs on `http://localhost:5001`

2. **Run tests:**
   ```bash
   python test.py
   ```
## UML Diagram
<img width="794" height="652" alt="image" src="https://github.com/user-attachments/assets/7d2bc9e2-9761-4307-8baa-ed6f41428b26" />

## API Usage / Example Call

**Endpoint:** `POST /report`

**Request:**
```json
test_data = {
  "report": {
    "title": "Cost Summary",
    "operation": "sum",
    "operation_field": "Cost",
    "filter_field": "Task Name",
    "filter_value": "HVAC",
    "date_field": "Last Performed Date",
    "date_range": {
      "from": "2025-01-01",
      "to": "2025-12-31"
    }
  },
  "data": [
    {
      "Task Name": "HVAC Maintenance",
      "Cost": "220",
      "Last Performed Date": "2025-06-01"
    }
  ]
}
```
**Example Request**
```
response = requests.post(f"{(http://localhost:5001)}/report", json=test_data)
```

**Response:**
```json
{
  "title": "Cost Summary",
  "operation": "sum",
  "operation_field": "Cost",
  "filter_field": "Task Name",
  "filter_value": "HVAC",
  "date_field": "Last Performed Date",
  "date_range": {
    "from": "2025-01-01",
    "to": "2025-12-31"
  },
  "result": 220
}
```


## Filtering Options

- **Field Filter**: Leave `filter_value` empty to include all records
- **Date Filter**: Leave `date_field` empty to skip date filtering
- Filters are combined with AND logic when both are specified

## Files

- `main.py` - Flask API server
- `reportGeneration.py` - Report generation logic
- `test.py` - Test suite with examples

## Error Codes

- `200` - Success
- `400` - Bad request (missing required fields)
- `500` - Server error
