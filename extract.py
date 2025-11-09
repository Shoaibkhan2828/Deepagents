
import json

def extract_json(data: dict) -> tuple:
    """
    Extracts agent outputs from the 'structured_response' key.

    Args:
        data: The complete dictionary returned by the agent runner.

    Returns:
        A tuple containing the research output and synthesis output (as dicts).
    """
    research_dict = None
    synthesis_dict = None

    # Check if the 'structured_response' key exists and is not None
    if 'structured_response' in data and data['structured_response']:
        structured_res = data['structured_response']

        # Access the research sub-agent object and convert it to a dictionary
        if hasattr(structured_res, 'research_sub_agent'):
            # vars() is a clean way to convert a simple object's attributes to a dict
            research_dict = vars(structured_res.research_sub_agent)

        # Access the synthesis sub-agent object and convert it to a dictionary
        if hasattr(structured_res, 'synthesis_sub_agent'):
            synthesis_dict = vars(structured_res.synthesis_sub_agent)

    return research_dict, synthesis_dict