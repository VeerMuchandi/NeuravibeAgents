import datetime
import random


def find_providers(
    doctor_type: str, location: str, gender: str = "No Preference"
) -> list[dict]:
    """
    Finds in-network doctors based on type, location, and gender preference.

    Args:
        doctor_type: The specialty of the doctor to search for (e.g., "Primary Care").
        location: The city, state, or ZIP code to search in.
        gender: The preferred gender of the doctor ('Male', 'Female', or 'No Preference').

    Returns:
        A list of dictionaries, where each dictionary represents a provider.
    """
    all_providers = [
        {
            "name": "Dr. Jane Doe",
            "type": "Primary Care",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "123 Beacon St, Boston, MA 02116",
            "phone": "617-555-1234",
        },
        {
            "name": "Dr. John Smith",
            "type": "Primary Care",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "456 Commonwealth Ave, Boston, MA 02215",
            "phone": "617-555-5678",
        },
        {
            "name": "Dr. Emily White",
            "type": "Dermatologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "789 Newbury St, Boston, MA 02116",
            "phone": "617-555-9012",
        },
        {
            "name": "Dr. Michael Brown",
            "type": "Cardiologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "100 Medical Center Dr, Boston, MA 02118",
            "phone": "617-555-1111",
        },
        {
            "name": "Dr. Sarah Davis",
            "type": "Cardiologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "200 Health St, Boston, MA 02130",
            "phone": "617-555-2222",
        },
        {
            "name": "Dr. David Wilson",
            "type": "Neurologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "300 Brainy Way, Boston, MA 02114",
            "phone": "617-555-3333",
        },
        {
            "name": "Dr. Jessica Martinez",
            "type": "Neurologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "400 Nerve Center, Boston, MA 02115",
            "phone": "617-555-4444",
        },
        {
            "name": "Dr. Christopher Lee",
            "type": "Orthopedist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "500 Bone Rd, Boston, MA 02215",
            "phone": "617-555-5555",
        },
        {
            "name": "Dr. Amanda Garcia",
            "type": "Orthopedist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "600 Joint Ave, Boston, MA 02118",
            "phone": "617-555-6666",
        },
        {
            "name": "Dr. James Rodriguez",
            "type": "Pediatrician",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "700 Kids St, Boston, MA 02120",
            "phone": "617-555-7777",
        },
        {
            "name": "Dr. Linda Hernandez",
            "type": "Pediatrician",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "800 Child Ave, Boston, MA 02119",
            "phone": "617-555-8888",
        },
        {
            "name": "Dr. Robert Lopez",
            "type": "Gynecologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "900 Womens Way, Boston, MA 02115",
            "phone": "617-555-9999",
        },
        {
            "name": "Dr. Patricia Gonzalez",
            "type": "Gynecologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "1010 Lady St, Boston, MA 02116",
            "phone": "617-555-1010",
        },
        {
            "name": "Dr. Daniel Perez",
            "type": "Urologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "1100 Waterworks Rd, Boston, MA 02134",
            "phone": "617-555-1100",
        },
        {
            "name": "Dr. Jennifer Sanchez",
            "type": "Urologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "1200 Kidney Ave, Boston, MA 02135",
            "phone": "617-555-1200",
        },
        {
            "name": "Dr. William Rivera",
            "type": "Gastroenterologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "1300 Gut St, Boston, MA 02111",
            "phone": "617-555-1300",
        },
        {
            "name": "Dr. Elizabeth Torres",
            "type": "Gastroenterologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "1400 Stomach Rd, Boston, MA 02114",
            "phone": "617-555-1400",
        },
        {
            "name": "Dr. Joseph Ramirez",
            "type": "Pulmonologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "1500 Lung Ave, Boston, MA 02118",
            "phone": "617-555-1500",
        },
        {
            "name": "Dr. Susan Flores",
            "type": "Pulmonologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "1600 Breath St, Boston, MA 02120",
            "phone": "617-555-1600",
        },
        {
            "name": "Dr. Thomas Gomez",
            "type": "Oncologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "1700 Hope Rd, Boston, MA 02114",
            "phone": "617-555-1700",
        },
        {
            "name": "Dr. Karen Reyes",
            "type": "Oncologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "1800 Cure Ave, Boston, MA 02115",
            "phone": "617-555-1800",
        },
        {
            "name": "Dr. Richard Cruz",
            "type": "Radiologist",
            "location": "Boston, MA",
            "gender": "Male",
            "address": "1900 Xray St, Boston, MA 02118",
            "phone": "617-555-1900",
        },
        {
            "name": "Dr. Nancy Morales",
            "type": "Radiologist",
            "location": "Boston, MA",
            "gender": "Female",
            "address": "2000 Scan Rd, Boston, MA 02130",
            "phone": "617-555-2000",
        },
    ]

    # A simple location match for demonstration purposes
    location_match = "boston" in location.lower() or "021" in location

    filtered_providers = [
        p
        for p in all_providers
        if p["type"].lower() == doctor_type.lower() and location_match
    ]

    if gender.lower() in ["male", "female"]:
        filtered_providers = [p for p in filtered_providers if p["gender"].lower() == gender.lower()]

    return filtered_providers[:3]


def get_available_slots(doctor_name: str, doctor_address: str) -> list[str]:
    """
    Gets available 30-minute appointment slots for a given doctor for today.

    Args:
        doctor_name: The name of the doctor.
        doctor_address: The address of the doctor's office.

    Returns:
        A list of 3 available appointment time slots.
    """
    # For mocking, we'll just generate random slots for today.
    # In a real scenario, this would query a scheduling system.
    today = datetime.date.today()
    start_time = datetime.datetime.combine(today, datetime.time(8, 0))
    end_time = datetime.datetime.combine(today, datetime.time(16, 0))

    possible_slots = []
    time_cursor = start_time
    while time_cursor < end_time:
        # Use '%-I' on Linux/macOS to avoid leading zero, or '%#I' on Windows
        try:
            slot = time_cursor.strftime("%-I:%M %p")
        except ValueError:
            slot = time_cursor.strftime("%#I:%M %p")
        possible_slots.append(slot)
        time_cursor += datetime.timedelta(minutes=30)

    if len(possible_slots) < 3:
        return possible_slots

    # Sort to ensure a consistent order for the user, even if random
    return sorted(random.sample(possible_slots, 3))


def book_appointment(doctor_name: str, doctor_address: str, appointment_slot: str) -> str:
    """
    Books an appointment with a doctor for a given time slot.

    Args:
        doctor_name: The name of the doctor.
        doctor_address: The address of the doctor's office.
        appointment_slot: The chosen time slot for the appointment.

    Returns:
        A confirmation message for the booked appointment.
    """
    # In a real scenario, this would interact with a booking system.
    return (
        f"Your appointment with {doctor_name} at {doctor_address} for "
        f"{appointment_slot} today has been successfully booked."
    )