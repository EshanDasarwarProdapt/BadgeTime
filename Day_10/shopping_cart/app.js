const products = require('./products');

// console.log('\nActivity1 - Display Product names')

// products.forEach(product=>{
//     console.log(`${product.name} - ₹${product.price}`)
// })


// console.log('\nActivity2 - Calculate Total Price')

// const totalPrice = products.map(product=>({
//     name : product.name,
//     totalprice: product.price * product.quantity
// }));

// console.log(totalPrice);


//Activity 3 - Find available products
// console.log('\nActivity3 - Find available products')

// const availableproducts = products.filter(product=>product.inStock)
// console.log(availableproducts)

//Activity 4 - Find expensive product
// console.log('\nActivity4 - Find expensive product')
// const expensiveproduct = products.filter(product=> product.price > 5000)
// console.log(expensiveproduct)

//Activity 5 - Find product by id
// console.log('\nActivity5 - Find product by id')
// const productid = products.find(product=> product.id==103)
// console.log(productid)


// //Activity 6 - Check product availibility
// console.log("\nActivity6 - check product availibility")
// const checkavailable = products.some(product => !product.inStock)
// console.log(checkavailable)

//Activity 7 - Verify stock status
// console.log("\nActivity 7 - Verify stock status")

// const allavailable = products.every(product => product.inStock)

// console.log(allavailable)

// console.log("\nActivity 8 - Calculate Grand Total")
// const grandTotal = products.reduce((total,product) => {
//     return total + (product.price * product.quantity)
// }, 0)

// console.log(grandTotal)


// console.log("\nActivity 9 - sort products by price")
// const sortprod = [...products].sort((a,b) => a.price-b.price)
// sortprod.forEach(product=>{
//     console.log(product.name)
// })

//Activity 10 - Display Only Product Names (map)

// console.log("\nActivity 10 - Display only product names")
// const displayProduct = products.map(product=>product.name)
// console.log(displayProduct)

//Activity 11 - Find product position
// const index = products.findIndex(product=> product.name === "Office Chair")
// console.log(index)

//Activity 12 - Remove out of stock products

// const availableremove = products.filter(product=>product.inStock)
// console.log(availableremove)

//Activity 13 - Add GST - 18%

// const productWithGST = products.map(product=>({
//     ...product,
//     gst: product.price * 0.18
// }))

// console.log(productWithGST)


//Top cheapest products

// const cheapestProd = [...products]
// .sort((a,b)=>a.price-b.price)
// .slice(0,3)

// console.log(cheapestProd)

// cheapestProd.forEach(product=>{
//     console.log(`${product.name} - ₹${product.price}`)
// })

//Generate Bill summary
console.log("\nGeneration of bills")

const billSummary = products.reduce(
    (summary,product) =>{
        summary.totalProducts++,
        summary.totalPrice += product.price,
        summary.totalAmount += product.price * product.quantity
        return summary
    },
    {
        totalProducts: 0,
        totalPrice: 0,
        totalAmount: 0
    }
)

console.log(billSummary)