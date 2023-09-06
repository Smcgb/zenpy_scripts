import requests

# Configuration
SUBDOMAIN = 'your_subdomain'
EMAIL = 'your_email'
API_TOKEN = 'your_api_token'
API_ENDPOINT = f"https://{SUBDOMAIN}.zendesk.com/api/v2/suspended_tickets"

def recover_suspended_tickets():

    """
    Recovers all suspended tickets in a Zendesk account.

    This function retrieves all suspended tickets from a specified Zendesk 
    account (defined by the SUBDOMAIN, EMAIL, and API_TOKEN global variables). 
    It then attempts to recover each of these tickets using the Zendesk API.

    Authentication is handled using the email and API token method. The
    EMAIL global variable should be the email associated with the Zendesk 
    account, and the API_TOKEN should be a generated API token from the Zendesk 
    Admin settings.

    The function prints the status of recovery for each ticket, either 
    indicating success or failure.

    Note:
        It's crucial to ensure that the EMAIL and API_TOKEN are set correctly
        and securely before running the function. Misuse can lead to unintended 
        changes in the Zendesk account.

    Returns:
        None
    """

    # Authentication
    auth = (EMAIL + "/token", API_TOKEN)

    # Get the list of suspended tickets
    response = requests.get(API_ENDPOINT + ".json", auth=auth)
    if response.status_code != 200:
        print("Failed to retrieve suspended tickets!")
        return

    tickets = response.json().get("suspended_tickets", [])
    if not tickets:
        print("No suspended tickets found.")
        return

    # Recover each suspended ticket
    for ticket in tickets:
        ticket_id = ticket["id"]
        recover_response = requests.put(API_ENDPOINT + f"/{ticket_id}/recover.json", auth=auth)

        if recover_response.status_code == 200:
            print(f"Successfully recovered ticket {ticket_id}")
        else:
            print(f"Failed to recover ticket {ticket_id}")

if __name__ == "__main__":
    recover_suspended_tickets()
