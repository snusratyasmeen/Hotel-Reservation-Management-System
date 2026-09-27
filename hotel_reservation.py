print("🏨 Hotel Reservation Management System")

reservations = []

while True:
    print("\n1. Add Reservation")
    print("2. View Reservations")
    print("3. Search Reservation")
    print("4. Update Reservation")
    print("5. Cancel Reservation")
    print("6. Count Reservations")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Reservation
    if choice == "1":
        reservation_id = input("Enter reservation ID: ")
        guest_name = input("Enter guest name: ")
        room_number = input("Enter room number: ")
        check_in = input("Enter check-in date: ")
        check_out = input("Enter check-out date: ")

        reservation = {
            "id": reservation_id,
            "guest": guest_name,
            "room": room_number,
            "check_in": check_in,
            "check_out": check_out
        }

        reservations.append(reservation)

        print("✅ Reservation added successfully!")

    # View Reservations
    elif choice == "2":
        if len(reservations) == 0:
            print("❌ No reservations found.")
        else:
            print("\n📋 Reservation Details")
            print("--------------------------")

            for reservation in reservations:
                print("Reservation ID:", reservation["id"])
                print("Guest Name:", reservation["guest"])
                print("Room Number:", reservation["room"])
                print("Check-in Date:", reservation["check_in"])
                print("Check-out Date:", reservation["check_out"])
                print("--------------------------")

    # Search Reservation
    elif choice == "3":
        search_id = input("Enter reservation ID to search: ")

        found = False

        for reservation in reservations:
            if reservation["id"] == search_id:
                print("\n✅ Reservation Found")
                print("Reservation ID:", reservation["id"])
                print("Guest Name:", reservation["guest"])
                print("Room Number:", reservation["room"])
                print("Check-in Date:", reservation["check_in"])
                print("Check-out Date:", reservation["check_out"])

                found = True
                break

        if not found:
            print("❌ Reservation not found.")

    # Update Reservation
    elif choice == "4":
        update_id = input("Enter reservation ID: ")

        found = False

        for reservation in reservations:
            if reservation["id"] == update_id:

                new_room = input("Enter new room number: ")
                new_check_in = input("Enter new check-in date: ")
                new_check_out = input("Enter new check-out date: ")

                reservation["room"] = new_room
                reservation["check_in"] = new_check_in
                reservation["check_out"] = new_check_out

                print("✅ Reservation updated successfully!")

                found = True
                break

        if not found:
            print("❌ Reservation not found.")

    # Cancel Reservation
    elif choice == "5":
        cancel_id = input("Enter reservation ID to cancel: ")

        found = False

        for reservation in reservations:
            if reservation["id"] == cancel_id:
                reservations.remove(reservation)

                print("✅ Reservation cancelled successfully!")

                found = True
                break

        if not found:
            print("❌ Reservation not found.")

    # Count Reservations
    elif choice == "6":
        print("🏨 Total Reservations:", len(reservations))

    # Exit
    elif choice == "7":
        print("Thank you for using Hotel Reservation Management System! 🏨")
        break

    else:
        print("❌ Invalid choice!")
