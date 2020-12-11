# nifi_flow
  https://nifi.apache.org/

### Problem Statement
  - Read `(firstName,lastName)` from a CSV.
  - Send this data to a `flask-API`.
  - This `API` would return the full name.
  - The result would be stored in a different file.
  - The workflow is to be implemented using `Apache-NiFi`.

### Directory Structure
  - **nifi.png**: Screenshot of the workflow
  - **NiFi_Flow.json**: `JSON` representation of the workflow
  - **flask_app.py**: A small `flask` application for handling `API` calls
