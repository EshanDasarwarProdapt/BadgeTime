const products = require('./products');

console.log('\nActivity1 - Display Product names')

products.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
})


console.log('\nActivity2 - Calculate Total Price')

const totalPrice = products.map(product=>({
    name : product.name,
    totalprice: product.price * product.quantity
}));

console.log(totalPrice);