curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://discoveryengine.googleapis.com/v1alpha/projects/121968733869/locations/global/collections/default_collection/engines/neuravibeapp_1738849257936/assistants/default_assistant/agents -d '
{
  "name": "phone_plan_shopper_agent",
  "displayName": "A2A Phone Plan Shopper",
  "description": "Shop phone plans and devices with EPP discounts",
  "a2aAgentDefinition": {
    "jsonAgentCard": "{\"name\": \"phone_plan_shopper_agent\", \"description\": \"This agent find phone plans and devices for employees with EPP discounts\", \"defaultInputModes\": [\"text/plain\"], \"defaultOutputModes\": [\"application/json\"], \"skills\": [{\"id\": \"shop_phone_plan\", \"name\": \"Shop discounted phone plans\", \"description\": \"Find EPP discounted phone plans and devices.\", \"tags\": [\"phone plan\", \"mobile phone\"]}],\"provider\": {\"url\": \"https://phone-plan-shopper-agent-121968733869.us-central1.run.app/a2a/phoneplan_shopper\"}, \"capabilities\": {}, \"version\": \"1.0.0\"}"
  }

}
'
