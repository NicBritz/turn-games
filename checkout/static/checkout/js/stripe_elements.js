// Get the keys from the context passed json
var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);

// init stripe
var stripe = Stripe(stripePublicKey);
// init the stripe elements
var elements = stripe.elements();
// update the cards styling to match the site
var style = {
    base: {
        color: "#000",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#dbdbdb",
        },
    },
    invalid: {
        color: "#f14668",
        iconColor: "#f14668",
    },
};
// create a card element
var card = elements.create("card", {style: style});
// mount the card element to the div in the payment view
card.mount("#card-element");

// Display realtime validation errors on the card element
card.addEventListener("change", function (event) {
    var errorDiv = document.getElementById("card-errors");
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
        $(errorDiv).addClass("help");
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submission
// src: documentation and course notes

var paymentForm = document.getElementById('payment-form');

paymentForm.addEventListener('submit', function (event) {
    // stop POST submit
    event.preventDefault();
    // stop multiple submits by disabling th element ans submit button
    card.update({'disabled': true});
    $('#submit-payment-button').addClass("is-loading");
    $('#submit-payment-button').attr('disabled', true);


    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,

        },
    }).then(function (result) {
        if (result.error) {
            // Show error to customer
            var errorDiv = document.getElementById('card-errors');
            var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // enable element and submit button
            card.update({'disabled': false});
            $('#submit-payment-button').removeClass('is-loading');
            $('#submit-payment-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                // successful - submit the form
                paymentForm.submit();
            }
        }
    })
})
