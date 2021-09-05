# SimpleStatusClient
A helper Client library in Python for the SimpleStatus project

## Getting Started

Ensure you have pulled [SimpleStatusServer](https://github.com/bravosierra99/SimpleStatus) and are running it (preferably straight from docker)

- clone library [SimpleStatusClient](https://github.com/bravosierra99/SimpleStatusClient)
- cd SimpleStatusClient
- python -m pip install . _(this should be the python environment in which your stasus needing code runs)
- Within the code that you wish to send statuses do the following
  - `from SimpleStatusClient import APIClient`
  - `client = APIClient("http://*server_ip*/api")` server_ip should be the ip address of your docker container
  - `client.setConfig()`
  - `client.setStatus()`

Voila, you should be able to view your status on the dashboard.