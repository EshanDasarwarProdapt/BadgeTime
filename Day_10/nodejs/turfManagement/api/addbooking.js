// export async function addBooking(booking){
//     const response = await fetch("http://localhost:3000/bookings/hell",{

//     method: "POST",
//     headers: {
//         "Content-type": "application/json"
//     },
//     body: JSON.stringify(booking)

//     });
//     return await response.json();
// }


export async function addBooking(booking) {
  try {
    const response = await fetch("http://localhost:3000/bookings", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(booking),
    });

    if (!response.ok) {
      throw new Error(`Failed to add booking. Status: ${response.status}`);
    }

    const data = await response.json();

    console.log("Booking added successfully:", data);

    return data;
  } catch (error) {
    console.error("Error adding booking:", error);
    throw error;
  }
}