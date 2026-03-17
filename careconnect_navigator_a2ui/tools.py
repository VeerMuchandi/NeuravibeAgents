import json
import uuid
import datetime
import random
from google.adk.tools.tool_context import ToolContext
from typing import Optional, Dict, Any, List

def _generate_mock_data():
    providers = []
    availability = {}
    zip_codes = ["60601", "60602", "60603"]
    specialties = ["pediatrician", "family practice", "cardiologist", "dermatologist"]
    
    first_names_f = ["Sarah", "Emily", "Jessica", "Ashley", "Amanda", "Elizabeth"]
    first_names_m = ["Michael", "David", "Christopher", "Matthew", "Joshua", "James"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
    
    random.seed(42)  # Deterministic mock data
    
    provider_id_counter = 1
    for zip_code in zip_codes:
        for specialty in specialties:
            # 3 In-Network and 3 Out-of-Network docs per specialty per zip
            for network_status in ["In-Network", "Out-of-Network"]:
                for _ in range(3):
                    gender = random.choice(["Female", "Male"])
                    if gender == "Female":
                        fname = random.choice(first_names_f)
                    else:
                        fname = random.choice(first_names_m)
                    
                    lname = random.choice(last_names)
                    pid = f"prov_{provider_id_counter}"
                    
                    doc = {
                        "provider_id": pid,
                        "name": f"Dr. {fname} {lname}",
                        "specialty": specialty.title(),
                        "gender": gender,
                        "network_status": network_status,
                        "location": f"{random.randint(100, 999)} State St",
                        "zip_code": zip_code
                    }
                    if network_status == "Out-of-Network":
                        doc["warning"] = "This provider is Out-of-Network. Higher out-of-pocket costs will apply."
                    
                    providers.append(doc)
                    availability[pid] = [f"{random.randint(8,11)}:00 AM", f"{random.randint(1,4)}:00 PM"]
                    provider_id_counter += 1
                
    return providers, availability

MOCK_PROVIDERS, MOCK_AVAILABILITY = _generate_mock_data()


def search_providers(specialty: str, location_zip: str, health_plan_id: str, tool_context: ToolContext, preferred_date: Optional[str] = None, preferred_time: Optional[str] = None) -> dict:
    """Finds doctors based on specialty, location, and health plan, prioritizing In-Network.
    
    If preferred_date and/or preferred_time are provided, it filters the results to those matching doctors.
    Returns network status (In-Network prioritizing, Out-of-Network as fallback).
    Requires 'health_plan_id' gathered from the user.
    """
    if not health_plan_id:
        return {"error": "Missing health_plan_id. Please ask the user to provide their plan details."}
        
    print(f"Searching for {specialty} near {location_zip} for plan {health_plan_id} (preferred date: {preferred_date}, preferred time: {preferred_time})")
    
    # Filter providers by specialty and zip code
    matched_providers = [
        p for p in MOCK_PROVIDERS 
        if specialty.lower() in p["specialty"].lower() and p["zip_code"] == location_zip
    ]
    
    # Optional time filtering
    if preferred_time or preferred_date:
        time_filtered_providers = []
        
        # Round the preferred_time to the nearest hour
        rounded_time = preferred_time
        if preferred_time:
            try:
                import re
                m = re.search(r'(\d{1,2}):(\d{2})\s*(am|pm)?', preferred_time, re.IGNORECASE)
                if m:
                    hr = int(m.group(1))
                    mn = int(m.group(2))
                    ampm = m.group(3)
                    
                    if mn >= 30:
                        hr += 1
                        
                    # basic 24 to 12 hour AM/PM converter
                    if not ampm:
                        if hr >= 24:
                            hr = 0
                            ampm = "AM"
                        elif hr >= 12:
                            ampm = "PM"
                            if hr > 12: hr -= 12
                        else:
                            ampm = "AM"
                            if hr == 0: hr = 12
                    else:
                        ampm = ampm.upper()
                        if hr == 13:
                            hr = 1
                            
                    rounded_time = f"{hr}:00 {ampm}"
            except Exception:
                pass
                
        # Format the exact requested slot for the UI
        exact_slot = f"{preferred_date} " if preferred_date else ""
        exact_slot += f"{rounded_time}" if rounded_time else ""
        exact_slot = exact_slot.strip()
        
        # To ensure the demo works seamlessly, we will artificially make a random 
        # subset of the matched providers available at the exactly requested time!
        for p in matched_providers:
            pid = p["provider_id"]
            if random.random() > 0.4: # ~60% chance to be available
                if pid not in MOCK_AVAILABILITY:
                    MOCK_AVAILABILITY[pid] = []
                
                # Add the explicitly requested slot to this provider's mock availability map
                if exact_slot and exact_slot not in MOCK_AVAILABILITY[pid]:
                    MOCK_AVAILABILITY[pid].append(exact_slot)
                    
                time_filtered_providers.append(p)
                
        # Fallback: if random chance filtered everyone out, just take the first two!
        if not time_filtered_providers and matched_providers:
            for p in matched_providers[:2]:
                pid = p["provider_id"]
                if exact_slot and exact_slot not in MOCK_AVAILABILITY[pid]:
                    MOCK_AVAILABILITY[pid].append(exact_slot)
                time_filtered_providers.append(p)
                
        matched_providers = time_filtered_providers
    
    if not matched_providers:
        return {"status": "success", "results": [], "network_status_found": "None"}
        
    network_status_found = "In-Network" if any(p["network_status"] == "In-Network" for p in matched_providers) else "Out-of-Network"
    return {"status": "success", "results": matched_providers, "network_status_found": network_status_found}


def get_availability(provider_ids: list[str], time_frame: str, tool_context: ToolContext) -> dict:
    """Fetches real-time, open time slots for a list of provider IDs and a general timeframe (e.g., 'Friday', 'tomorrow morning').
    
    Returns a dictionary mapping provider IDs to a list of available time slots.
    """
    if not provider_ids:
        return {"error": "No provider_ids provided."}
        
    print(f"Fetching availability for {provider_ids} around {time_frame}")
    
    availability = {}
    for pid in provider_ids:
        if pid in MOCK_AVAILABILITY:
            availability[pid] = MOCK_AVAILABILITY[pid]
             
    return {"status": "success", "availability": availability}


def book_appointment(provider_id: str, date_time: str, tool_context: ToolContext) -> dict:
    """Secures a specific time slot for the user with a chosen provider.
    
    Requires 'user_id' in the session state. 
    """
    # Assume user is already authenticated
    user_id = "authenticated_user"
        
    confirmation_number = f"CONF-{uuid.uuid4().hex[:8].upper()}"
    print(f"Booking {provider_id} at {date_time} for {user_id}. Confirmation: {confirmation_number}")
    
    tool_context.state["selected_provider_id"] = provider_id
    tool_context.state["booked_appointment_details"] = {
        "provider_id": provider_id,
        "date_time": date_time,
        "confirmation_number": confirmation_number
    }
    
    return {
        "status": "success", 
        "message": "Appointment booked successfully.",
        "confirmation_number": confirmation_number,
        "provider_id": provider_id,
        "date_time": date_time
    }
