# GitHub Organization Repository Details to CSV

## Overview
This script fetches detailed information about all repositories within a specified GitHub organization and outputs the information into a CSV file. The information includes repository metadata, collaborators, teams with access, and branch details.

## Prerequisites
- Python 3.x
- `requests` library
- GitHub Personal Access Token

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install the `requests` library:
    ```bash
    pip install requests
    ```

## Usage
1. Save the script to a file, e.g., `github_repo-info_csv.py`.
2. Run the script:
    ```bash
    python github_repo-info_csv.py
    ```
3. Enter the required information when prompted:
    - **GitHub organization name**: The name of the GitHub organization you want to query.
    - **GitHub Personal Access Token**: Your personal access token for authenticating API requests.

## Example CSV Output
The CSV file includes the following columns:
- `Repo Name`
- `Full Name`
- `Description`
- `Private`
- `HTML URL`
- `Created At`
- `Updated At`
- `Pushed At`
- `Language`
- `Collaborators`
- `Teams`
- `Number of Branches`
- `Branch Names`
- `Last Updated Branches`

## Notes
- Ensure your GitHub Personal Access Token has sufficient permissions to access repository, collaborators, teams, and branch information.
- The script handles pagination to fetch all available data for repositories, collaborators, teams, and branches.

## Example
```plaintext
Enter the GitHub organization name: your_org_name
Enter your GitHub Personal Access Token: your_personal_access_token
Repository details with access information have been written to your_org_name_repo_details.csv

