//   From Bulma Documentation: https://bulma.io/documentation/elements/notification/
document.addEventListener('DOMContentLoaded', () => {
    // Select all the relevant notification classes
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {

        let $notification = $delete.parentNode;

        $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
        });

        // remove notification after a few seconds
        setTimeout(function () {
                $notification.parentNode.removeChild($notification);
        }, 3000);


    });

    // Show mobile menu on click
    $(".navbar-burger").click(function () {
        $(".navbar-burger").toggleClass("is-active");
        $("#navbar-menu").toggleClass("is-active");
    });

    // Spin logo on mouse hover
    $(".main-logo-container").mouseenter(function () {
        if (!$('#logo-image').hasClass(".image-spin")) {
            $('#logo-image').addClass("image-spin")
        }
    }).mouseleave(function () {
            $('#logo-image').removeClass("image-spin");
        }
    )

    // Desktop Search Modal
    $("#search-button").click(function () {
        $('#search-modal').addClass("is-active");
        $("#search-field:text").focus();
    });

    $('.modal-close').click(function () {
        $("#search-modal").removeClass('is-active');
    })

});