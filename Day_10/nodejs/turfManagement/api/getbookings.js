// //I need the get booking api like the add booking api

// export async function getbooking(idbooking,booking) {
//   try {
//     const response = await fetch(`http://localhost:3000/bookings/${idbooking}`, {
//       method: "GET",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(booking),
//     });

//     if (!response.ok) {
//       throw new Error(`Failed to get booking. Status: ${response.status}`);
//     }

//     const data = await response.json();

//     console.log("Booking retrieved successfully:", data);

//     return data;
//   } catch (error) {
//     console.error("Error getting booking:", error);
//     throw error;
//   }
// }



export async function getbooking() {
  try {
    const response = await fetch("http://localhost:3000/bookings");

    if (!response.ok) {
      throw new Error(`Failed to get bookings. Status: ${response.status}`);
    }

    const data = await response.json();

    console.log("Bookings retrieved successfully");

    return data;
  } catch (error) {
    console.error("Error getting bookings:", error);
    throw error;
  }
}