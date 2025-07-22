# telecom_api_simulator.py
"""
Simulated API functions for a telecom provider to demonstrate ADK tool usage.
"""
import asyncio
import json
import os
import random
from typing import Any, Dict, List, Literal, Optional

def get_epp_plan_recommendations(
    data_usage_category: Literal["Light", "Medium", "Heavy"],
    international_calling: bool = False,
) -> Dict[str, Any]:
    """Retrieves exclusive partner program (EPP) mobile plan recommendations
    based on data usage and international calling needs for Neuravibe employees.
    """
    # In a real-world scenario, this would query a database or an API endpoint.
    # Here, we simulate the plan data with pre-applied EPP discounts.
    print(
        f"\n>>> [TOOL CALL] get_epp_plan_recommendations("
        f"data_usage='{data_usage_category}', "
        f"international={international_calling})\n"
    )

    if data_usage_category not in ["Light", "Medium", "Heavy"]:
        return {"error": f"Sorry, I don't recognize '{data_usage_category}' as a valid data usage category. Please choose from Light, Medium, or Heavy."}

    # Base plans with EPP pricing
    epp_plans = {
        "Light": {
            "name": "Neuravibe EPP Connect 15",
            "data_gb": 15,
            "price": 45.00,
            "original_price": 55.00,
            "features": ["Unlimited Talk & Text", "5G Access"],
        },
        "Medium": {
            "name": "Neuravibe EPP Power 50",
            "data_gb": 50,
            "price": 60.00,
            "original_price": 75.00,
            "features": ["Unlimited Talk & Text", "5G+ Speeds", "Hotspot Access"],
        },
        "Heavy": {
            "name": "Neuravibe EPP Ultimate 100",
            "data_gb": 100,
            "price": 75.00,
            "original_price": 90.00,
            "features": ["Unlimited Talk & Text", "5G+ Speeds", "15GB Hotspot", "HD Streaming"],
        }
    }

    plan = epp_plans[data_usage_category]

    # Simulate adding an international calling package
    if international_calling:
        plan["name"] += " with Global Talk"
        plan["price"] += 10.00  # Add a fee for the international package
        plan["features"].append("Preferred International Rates")

    return plan

def get_device_offers(plan_name: Optional[str] = None) -> str:
    """Provides details on available device offers for a specific mobile plan,
    considering EPP discounts. It can also be used to get general device offers.
    """
    print(f"\n>>> [TOOL CALL] get_device_offers(plan_name='{plan_name}')\n")

    # Determine the directory of the current script to locate the JSON file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, "devices.json")

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            all_devices = json.load(f)["devices"]
    except (FileNotFoundError, json.JSONDecodeError):
        return "I'm sorry, I'm having trouble fetching device offers at the moment."

    # Determine which tiers of devices to offer based on the plan name
    eligible_tiers: List[str]
    if plan_name and "Ultimate" in plan_name:
        eligible_tiers = ["premium", "high-end", "mid-range"]
        message_intro = (
            f"With the {plan_name}, you're eligible for our full range of devices, from premium to affordable:"
        )
    elif plan_name and "Power" in plan_name:
        eligible_tiers = ["high-end", "mid-range"]
        message_intro = (
            f"The {plan_name} comes with some great high-end device offers:"
        )
    elif plan_name and "Connect" in plan_name:
        eligible_tiers = ["mid-range"]
        message_intro = (
            f"For the {plan_name}, we have some excellent and affordable devices for you:"
        )
    else:
        # Fallback for unrecognized plans or general queries to show all devices
        eligible_tiers = ["premium", "high-end", "mid-range"]
        message_intro = "We have great deals on a wide range of phones, and here are a few options from our full lineup:"
    # Filter devices by the selected tiers
    eligible_devices = [
        device for device in all_devices if device.get("tier") in eligible_tiers
    ]

    if not eligible_devices:
        return "I couldn't find any specific device offers for that plan right now, but we have many great options available."

    # Select up to 3 random devices from the eligible list
    num_to_offer = min(len(eligible_devices), 3)
    selected_devices = random.sample(eligible_devices, num_to_offer)

    # Format the offers into a string
    offer_strings = [
        f"- The {device['name']} for an additional ${device['monthly_price']}/month."
        for device in selected_devices
    ]

    return f"{message_intro}\n" + "\n".join(offer_strings)


def generate_order_link(plan_details: Dict[str, Any], device_offer: Optional[str] = None) -> str:
    """Generates a direct link to the telecom's EPP portal to finalize the
    order for a selected plan and optional device.
    """
    print(f"\n>>> [TOOL CALL] generate_order_link(plan_details={plan_details}, device_offer='{device_offer}')\n")

    # Create a simplified identifier for the plan in the URL
    plan_id = "".join(filter(str.isalnum, plan_details.get("name", "customplan"))).lower()

    # Construct the base URL
    base_url = "https://epp.neuravibe-telecom-partner.com/order"
    
    # Add query parameters
    query_params = [f"plan={plan_id}"]
    if device_offer:
        # Simulate a simple device identifier
        device_id = "latestphone"
        if "Pro model" in device_offer:
            device_id = "prophone"
        query_params.append(f"device={device_id}")

    return f"{base_url}?{'&'.join(query_params)}"


async def request_manager_discount(
    plan_details: Dict[str, Any], device_name: Optional[str] = None
) -> str:
    """Submits a request to a manager for an additional one-time discount on a
    plan and/or device. This simulates a manager approving a random discount.
    """
    print(
        "\n>>> [TOOL CALL] request_manager_discount("
        f"plan_details={plan_details}, device_name='{device_name}')\n"
    )

    # Simulate waiting for manager approval
    await asyncio.sleep(3)

    # Simulate manager approval with a random discount
    possible_discounts = [5, 10, 15, 20, 25]
    approved_discount_percent = random.choice(possible_discounts)
    discount_multiplier = 1 - (approved_discount_percent / 100.0)

    original_plan_price = plan_details["price"]
    new_plan_price = round(original_plan_price * discount_multiplier, 2)
    plan_details["price"] = new_plan_price  # Update the plan details with the new price

    response_parts = [
        f"Great news! My manager has approved an additional {approved_discount_percent}% discount for you.",
        f"Your new discounted price for the {plan_details['name']} is now ${new_plan_price:.2f}/month."
    ]

    if device_name:
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_file_path = os.path.join(current_dir, "devices.json")
            with open(json_file_path, "r", encoding="utf-8") as f:
                all_devices = json.load(f)["devices"]

            device_details = next(
                (d for d in all_devices if d["name"] == device_name), None
            )

            if device_details:
                original_device_price = device_details["monthly_price"]
                new_device_price = round(original_device_price * discount_multiplier, 2)
                response_parts.append(
                    f"The {device_name} will now be an additional ${new_device_price:.2f}/month."
                )

        except (FileNotFoundError, json.JSONDecodeError):
            response_parts.append(
                "I had some trouble applying the discount to the device, but your plan discount is confirmed."
            )

    return " ".join(response_parts)
