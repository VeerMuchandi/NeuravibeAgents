# Provider Search Agent

This agent helps UnitedHealth Group members find in-network doctors and specialists.

## Overview

This is a conversational agent that guides a user through the process of finding a healthcare provider. It asks for the type of doctor, the user's location, and an optional gender preference before providing a list of matching doctors from a mock database.

### Features

- **Conversational Flow:** Guides the user step-by-step.
- **Information Gathering:** Collects necessary details like doctor type, location, and gender.
- **Tool Use:** Utilizes a mock `find_providers` tool to fetch doctor information.
- **State Management:** Uses in-memory state to track the conversation.

## Setup and Installation

### Prerequisites

- Python 3.11+
- The Agent Development Kit (ADK).

### Installation

1. Ensure you are in the root of the `agent-framework-samples` directory.
2. Install the required dependencies for this agent. It's recommended to do this within the project's virtual environment.

    ```bash
    # From the root of agent-framework-samples
    pip install -e uhg_provider_search/
    ```

## Running the Agent

You can interact with the agent using the ADK's command-line interface or the Streamlit web UI.

### Using `adk run` (CLI)

1. From the root of the `agent-framework-samples` directory, run the agent:

    ```bash
    adk run uhg_provider_search
    ```

2. You can now chat with the agent in your terminal.

    **Example Interaction:**

    > **Agent:** Hello! I can help you find a doctor or specialist in your UnitedHealth Group network. What type of doctor are you looking for today? (e.g., Primary Care, Cardiologist, Dermatologist, Pediatrician)
    >
    > **You:** I need a Dermatologist
    >
    > **Agent:** Okay, a Dermatologist. What is your preferred city and state, or your ZIP code?

### Using `adk streamlit` (Web UI)

1. Start the ADK Streamlit server:

    ```bash
    adk streamlit
    ```

2. Open the provided URL in your web browser.
3. Select "uhg_provider_search" from the agent dropdown menu to start a new session.