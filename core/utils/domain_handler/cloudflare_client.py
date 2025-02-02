from cloudflare import Cloudflare
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class CloudflareAPIClient:
    """
    A client wrapper for interacting with the Cloudflare API.
    """

    def __init__(self):
        try:
            # Initialize the Cloudflare client with the API token.
            self.cf = Cloudflare(
                api_email=settings.CLOUDFLARE_EMAIL,
                api_key=settings.CLOUDFLARE_API_KEY
            )
        except Exception as e:
            logger.error(f"Cloudflare API initialization failed: {e}")
            raise

    def get_account_id(self):
        try:
            account_id = self.cf.accounts.list().result[0].id
        except Exception as e:
            logger.error(f"Error get account id: {e}")
            raise
        return account_id
    
    def account_object(self):
        account_id = self.get_account_id()
        return {"id": account_id}
    
    def list_zones(self):
        """
        List zones, optionally filtering by name.
        """
        try:
            zones = self.cf.zones.list()
            return zones
        except Exception as e:
            logger.error(f"Error listing zones: {e}")
            raise

    def create_zone(self, name):
        """
        Create a new zone with the specified name.
        
        :param name: The zone name (e.g. example.com)
        """
        try:
            account_id = self.account_object()
            zone = self.cf.zones.create(account=account_id, name=name)
            return zone
        except Exception as e:
            logger.error(f"Error creating zone: {e}")
            raise

    def delete_zone(self, zone_id):
        """
        Delete a zone by its ID.
        """
        try:
            result = self.cf.zones.delete(zone_id)
            return result
        except Exception as e:
            logger.error(f"Error deleting zone: {e}")
            raise

    def get_zone_details(self, zone_id):
        """
        Retrieve details for a given zone.
        """
        try:
            zone = self.cf.zones.get(zone_id=zone_id)
            return zone
        except Exception as e:
            logger.error(f"Error fetching zone details: {e}")
            raise
    
    def is_zone_active(self, zone):
        """
        Checks whether the Cloudflare zone is active.

        :param zone: A Cloudflare zone object.
        :return: True if the zone is active, False otherwise.
        """
        # Option 1: Check based on the activated_on attribute.
        if zone.activated_on is not None:
            return True

        # Option 2: Alternatively, check if the zone status is 'active'
        if hasattr(zone, 'status') and zone.status.lower() == "active":
            return True

        return False

    def add_dns_a_record(self, zone_id, name, ip, ttl=1, proxied=False):
        """
        Add an A record to the specified zone using the current Cloudflare SDK.
        
        :param zone_id: The Cloudflare zone ID.
        :param name: The DNS record name. For the root domain, this should be the domain name itself.
        :param ip: The IPv4 address to assign to the A record.
        :param ttl: Time to live for the record. Use 1 for automatic.
        :param proxied: Whether the record should be proxied via Cloudflare.
        :return: The API response for the created record.
        """
        data = {
            "type": "A",
            "name": name,
            "content": ip,
            "ttl": ttl,
            "proxied": proxied,
        }
        try:
            # Use the new method from the updated SDK: client.dns.records.create
            result = self.cf.dns.records.create(zone_id=zone_id, **data)
            logger.info(f"A record created for {name}: {result}")
            return result
        except Exception as e:
            logger.error(f"Error adding A record for {name}: {e}")
            raise
