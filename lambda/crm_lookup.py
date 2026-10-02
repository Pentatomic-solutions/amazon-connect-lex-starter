"""
Amazon Connect CRM Lookup & Contact Flow Data Connector
Maintained by Pentatomic Solutions (https://pentatomicsolutions.in)

Invoked synchronously by Amazon Connect contact flows to retrieve caller profile,
open support tickets, and account tier for personalized Lex IVR routing.
"""

import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Received Amazon Connect Event: %s", json.dumps(event))

    # Extract customer phone number from Connect contact attributes
    contact_data = event.get("Details", {}).get("ContactData", {})
    customer_endpoint = contact_data.get("CustomerEndpoint", {})
    caller_phone = customer_endpoint.get("Address", "")
    customer_id = contact_data.get("Attributes", {}).get("CustomerId", "")

    logger.info("Processing lookup for Caller: %s, CustomerId: %s", caller_phone, customer_id)

    # Simulated enterprise CRM data lookup (replace with DynamoDB / Salesforce API call)
    crm_record = lookup_crm_profile(caller_phone, customer_id)

    response = {
        "statusCode": 200,
        "customerFound": "true" if crm_record else "false",
        "customerName": crm_record.get("name", "Valued Customer"),
        "customerTier": crm_record.get("tier", "Standard"),
        "hasOpenTicket": crm_record.get("hasOpenTicket", "false"),
        "ticketId": crm_record.get("ticketId", ""),
        "preferredLanguage": crm_record.get("preferredLanguage", "en-US"),
        "routePriority": crm_record.get("routePriority", "10"),
    }

    logger.info("Returning Connect Attributes: %s", json.dumps(response))
    return response


def lookup_crm_profile(phone: str, customer_id: str) -> dict:
    """Mock CRM data connector. Connect to external REST API or AWS DynamoDB."""
    if not phone and not customer_id:
        return {}

    return {
        "name": "Jane Doe",
        "tier": "Enterprise VIP",
        "hasOpenTicket": "true",
        "ticketId": "TCK-94821",
        "preferredLanguage": "en-US",
        "routePriority": "1",
    }
