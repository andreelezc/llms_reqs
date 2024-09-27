# Regular propmt with no further instructions or clarifications (i.e, as you would input it in the web interface)

basic_prompt = """Analyze the following app screen and list its functional requirements (FR) in detail.
Format your answer as: FR#{i}: The system must {requirement}. Provide only the list of requirements.
"""
# First sg_prompt
# sg_prompt = """Generate a scene graph for this app mockup, identifying the objects (UI components) and
# their relationships. Provide this as a structured JSON output without additional text."
# """

# Enhanced SG prompt (need to try)
sg_prompt = """
Generate a scene graph for this app mockup by identifying the objects (UI components) and their relationships. Summarize repeated elements and only provide unique attributes for each occurrence. Provide the output as a structured JSON object in the exact format shown below:

{
    "sceneGraph": {
        "objects": [
        ],
        "relationships": {
            "ComponentType1": "relationship description",
        }
    }
}

Do not include any additional text or explanations outside the JSON object.

"""

# Improved prompt to be passed with SG #1
improved_prompt = """Analyze the following app screen and its accompanying scene graph. For each UI component, 
list the functional requirements that describe both the system's behavior and the user actions enabled by that 
component.

Format your answer as:
FR#{i}: The system must {requirement}. 
Provide only the list of requirements.
"""
# Improved prompt to be passed with SG #2
improved_functional_prompt = """Analyze the following app screen and its accompanying scene graph
and list its functional requirements (FR) in detail. The focus should be on the underlying functional logic of UI 
elements and the user actions enabled by that. 

Format your answer as:
FR#{i}: The system must {requirement}. 
Provide only the list of requirements without additional text.
"""

# Improved prompt to be passed with SG #3 (current)
two_step_prompt = """
    Step 1: Here is a list of functional requirements (FR) generated based on the app screen:

    {first_output}

    Step 2: Now, refine this list by reviewing the accompanying scene graph. Add any missing details, correct relationships, 
    or specify user interactions that the scene graph reveals.

    Scene Graph:
    {scene_graph}

    Format your final answer as:
    FR#{'{i}'}: The system must {{requirement}}.
    Provide only the refined list of requirements without additional text.
"""
