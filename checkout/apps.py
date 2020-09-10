from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Activate signals once ready
    def ready(self):
        import checkout.signals
