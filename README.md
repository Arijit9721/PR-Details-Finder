## PR-Details-Finder
Overview

PR-Details-Finder is a Python script that retrieves and displays the details of pull requests from a specified GitHub repository. It leverages the GitHub REST API to fetch pull request data, prints details of each pull request, and counts the number of pull requests made by each user.
Features

    Retrieves pull request data from a GitHub repository using the GitHub REST API.
    Displays details of all pull requests, including:
        Serial number
        Login name of the user who made the pull request
        User ID
        Pull request URL
        Pull request ID
    Calculates and displays the total number of pull requests made by each user.

Prerequisites

    Python: Ensure you have Python 3.6 or higher installed.
    Libraries: The script uses the requests library, which can be installed with:

    pip install requests

How to Use

    Clone or Download the Repository: Clone the repository containing the script or copy the script code into a Python file (e.g., pr_details_finder.py).

    Run the Script:
        Open a terminal or command prompt.
        Navigate to the folder containing the script.
        Execute the script with:

        python pr_details_finder.py

    Output:
        The script will print the details of each pull request in the repository.
        At the end, it will display the total number of pull requests made by each user.


