export async function addBooking(booking){
    const response = await fetch("http://localhost:3000/bookings/hell",{

    method: "POST",
    headers: {
        "Content-type": "application/json"
    },
    body: JSON.stringify(booking)

    });
    return await response.json();
}