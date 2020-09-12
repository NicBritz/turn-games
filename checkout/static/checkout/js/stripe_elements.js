// Get the keys from the context passed json
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// init stripe
var stripe = Stripe(stripePublicKey);
// init the stripe elements
var elements = stripe.elements();
// update the cards styling to match the site
var style = {
  base: {
    color: '#000',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#dbdbdb'
    }
  },
  invalid: {
    color: '#f14668',
    iconColor: '#f14668'
  }
};
// create a card element
var card = elements.create('card', {style: style});
// mount the card element to the div in the payment view
card.mount('#card-element');
