jQuery(function ($) {

    $('.form-search span').click(function () {
        $('.form-search form').slideToggle();
    });
    $('.responsive-list').click(function () {
        $('.mega-menu .container > ul').slideToggle();
    });

    $('.thumbnails-image img').click(function () {
        var src = $(this).attr('src');
        $('.large-image img').attr('src', src).fadeOut('fast').fadeIn('fast');
    });

    $("#slider-one").owlCarousel({
        navigation: false, // Show next and prev buttons
        slideSpeed: 300,
        dots: true,
        paginationSpeed: 400,
        singleItem: true,
        items: 1,
        autoplay: 500,
        center: true,
        autoplayHoverPause: true,
        loop: true
    });
    $(document).ready(function () {
        var basketInfo = localStorage.getItem("basket");
        if (basketInfo) {
            var basket = JSON.parse(basketInfo);
            Object.keys(basket).forEach(async function (element) {
                var product = await getSingleProductInfo(element);
                var toAppend = `<li>
                <img class="border-radius" src="/media/${product?.product_picture}">
                <div class="left-basket">
                  <a href="">${product?.name} <span class="border-radius"> ${basket[element]}</span></a>
                </div>
            </li>`;
                $("#basket-list").append(toAppend);
            });
        }
    });
});

async function getSingleProductInfo(id) {
    var data = await $.ajax("/product?id=" + id);
    return data;
}