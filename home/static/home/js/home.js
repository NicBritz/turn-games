// Flickity script
$('.carousel').flickity({
    // options
    cellAlign: 'left',
    contain: true,
    imagesLoaded: true,
    autoPlay: 5000,
    wrapAround: true,
});

// Back to top script
$('#top-button').click(function () {
    window.scrollTo(0, 0)
})
