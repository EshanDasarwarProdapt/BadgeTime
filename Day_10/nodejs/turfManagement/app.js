import {getbooking} from './api/getbookings.js';

async function main() {
    console.log("Fetching latest bookings ...");
    const bookings = await getbooking();
    console.table(bookings);
}

main()
