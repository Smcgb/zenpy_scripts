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
    
    # Fetch all suspended ticket IDs
    response = requests.get(API_ENDPOINT + ".json", auth=auth)
    if response.status_code != 200:
        print("Failed to retrieve suspended tickets!")
        return

    ticket_ids = [ticket["id"] for ticket in response.json().get("suspended_tickets", [])]
    if not ticket_ids:
        print("No suspended tickets found.")
        return
    
    # Construct the recover_many URL
    ids_str = ",".join(map(str, ticket_ids))
    recover_url = f"{API_ENDPOINT}/recover_many?ids={ids_str}"

    # Recover tickets in bulk
    headers = {
        "Content-Type": "application/json",
    }
    recover_response = requests.put(recover_url, auth=auth, headers=headers)
    
    if recover_response.status_code == 200:
        print(f"Successfully recovered tickets: {ids_str}")
    else:
        print(f"Failed to recover tickets: {ids_str}")
        print(recover_response.text)  # Print the response to debug issues

if __name__ == "__main__":

    while True:
        print("Recovering suspended tickets...")
        recover_suspended_tickets()
        print("Sleeping for 2 minutes...")
        time.sleep(60 * 2)
