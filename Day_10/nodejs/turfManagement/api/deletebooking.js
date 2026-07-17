//delete booking api

export async function deletebooking(idbooking) {
  try {
    const response = await fetch(`http://localhost:3000/bookings/${idbooking}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error deleting booking:", error);
    throw error;
  }
}