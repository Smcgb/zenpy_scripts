## Zendesk Suspended Tickets Recovery Tool

This Python script is designed to automate the recovery of suspended tickets within a Zendesk account. It utilizes the Zendesk API to fetch and recover all tickets that have been suspended, streamlining the management of your support tickets.
Features

    Automated Recovery: Effortlessly recover all suspended tickets in your Zendesk account.
    Bulk Operations: Process multiple tickets at once for efficient management.
    Authentication: Securely authenticate using your Zendesk account email and an API token.
    Status Reporting: Get instant feedback on the recovery process with detailed status reports.

### Prerequisites

Before you can use this script, make sure you have the following:

1. Python 3: Ensure Python 3 is installed on your machine.

2. Requests Library: The script uses the requests library to make HTTP requests. Install it using pip:
`pip install requests`

3. Zendesk Account: You'll need a Zendesk account with administrative privileges to generate an API token.

### Configuration

To use the script, you need to configure it with your Zendesk account details:

1. Subdomain: Replace 'your_subdomain' with your Zendesk account's subdomain.
2. Email: Set 'your_email' to the email associated with your Zendesk account. This email role will need proper permissions assigned to their role (Admin for basic roles or a custom role with API access)
3. API Token: Generate an API token from your Zendesk admin settings and replace 'your_api_token'.

### Usage

To run the script, simply execute it from your command line:

`python zendesk_recover_suspended_tickets.py`

The script will continuously run, attempting to recover suspended tickets every 2 minutes. To stop the script, use the keyboard interrupt command, typically Ctrl + C.
### Limitations

Support Account Tickets: Tickets that were originally created from support accounts cannot be recovered using this script. These tickets require additional handling that is not currently supported.

Recovery Validation: The script does not perform any validation to determine whether a ticket should be recovered. It attempts to recover all suspended tickets indiscriminately. Users should manually review tickets if there are concerns about which tickets are appropriate for recovery.

#### Security Note

Ensure your API token and email are stored securely and not exposed in public repositories or shared environments. Misuse of these credentials can lead to unauthorized access to your Zendesk account.
Troubleshooting

If you encounter any issues during the recovery process, the script will output detailed error messages to assist in debugging. Ensure your credentials are correct and that your Zendesk account has the necessary permissions for ticket recovery.



