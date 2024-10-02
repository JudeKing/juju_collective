from django.apps import AppConfig


class JujuStorefrontConfig(AppConfig):
    """Configuration class for the JUJU Storefront application.
        
        Attributes:
            default_auto_fields (str): The default field type.
            name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'juju_storefront'
