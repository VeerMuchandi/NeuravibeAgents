from google.adk.agents import LlmAgent

from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


# Agents

phone_plan_shopper_agent = RemoteA2aAgent(
    name="phone_plan_shopper_agent",
    description="Agent that helps shop for EPP discounted phone plans an devices.",
    agent_card=(
        "phone_plan_shopper.json"
    ),
)
root_agent = LlmAgent(
            model='gemini-2.0-flash-001',
            name='phoneplan_a2a_tester',
            description='An agent that tests the remote A2A agent.',
            #after_tool_callback=self._handle_auth_required_task,
            instruction="""
                Cleary explain to the user that you are representing the Phone Plan shopper A2A agent.
                Interact with the user and act as an intermediary in the conversations with the remote agent.
                """,
	# Add the sub_agents parameter below
            sub_agents=[phone_plan_shopper_agent],

        )
