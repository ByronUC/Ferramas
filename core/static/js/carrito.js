document.addEventListener('DOMContentLoaded', function () {
    const addToCartButton = document.getElementById('add-to-cart-button');

    if (addToCartButton) {
        addToCartButton.addEventListener('click', function (event) {
            event.preventDefault();
            addToCart();
        });
    }

    function addToCart() {
        const productName = document.querySelector('.product__details__text h3').textContent;
        const productPrice = document.querySelector('.product__details__price').textContent;
        const productImage = document.getElementById('product-image').getAttribute('src');
        const productQuantity = parseInt(document.querySelector('input[name="quantity"]').value);

        let cart = JSON.parse(localStorage.getItem('cart')) || {};

        if (cart[productName]) {
            cart[productName].quantity += productQuantity;
        } else {
            cart[productName] = {
                name: productName,
                price: productPrice,
                image: productImage,
                quantity: productQuantity
            };
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        alert('Product added to cart');
    }
});
