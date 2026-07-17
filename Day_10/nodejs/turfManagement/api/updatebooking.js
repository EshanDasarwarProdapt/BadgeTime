export async function updatebooking(idbooking,booking) {
  try {
    const response = await fetch(`http://localhost:3000/bookings/${idbooking}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(booking),
    });

    if (!response.ok) {
      throw new Error(`Failed to update booking. Status: ${response.status}`);
    }

    const data = await response.json();

    console.log("Booking updated successfully:", data);

    return data;
  } catch (error) {
    console.error("Error updating booking:", error);
    throw error;
  }
}