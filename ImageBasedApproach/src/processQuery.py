from ollama import chat
from ollama import ChatResponse
from updatedPrompts import get_error_prompt

object_physical_properties = {
    "general": {
        "name": "Unique identifier or label for the object (e.g., 'mug', 'bicycle', 'beam')",
        "category": "Broad classification (e.g., 'container', 'vehicle', 'structural element')",
        "sub_category": "More detailed classification (e.g., 'ceramic mug', 'mountain bike', 'I-beam')",
        "primary_function": "Main purpose or use of the object (e.g., 'holding liquids', 'transportation')",
        "material_composition": ["List of materials (e.g., 'ceramic', 'aluminum', 'carbon fiber')"]
    },
    "geometric_properties": {
        "overall_shape": "General form (e.g., 'cylindrical', 'spherical', 'rectangular')",
        "base_shape": "Shape of the base (e.g., 'flat', 'rounded', 'pointed')",
        "opening_shape": "Shape of any openings (e.g., 'circular', 'elliptical', 'rectangular')",
        "symmetry": "Type of symmetry (e.g., 'radial', 'bilateral', 'asymmetrical')",
        "aspect_ratio": "Ratio of height to width to depth, where applicable",
        "bounding_box": "Minimum enclosing volume dimensions (length, width, height)",
        "curvature": "Degree of curvature on surfaces (e.g., 'flat', 'convex', 'concave')"
    },
    "structural_features": {
        "protrusions": "Any outward extensions (e.g., 'handle', 'antenna', 'wing')",
        "indentations": "Concave features (e.g., 'grooves', 'slots', 'dimples')",
        "hollow_sections": "Areas that are not solid (e.g., 'tube', 'frame')",
        "connections": "How different parts are joined (e.g., 'welded', 'bolted', 'hinged')",
        "supports": "Structural reinforcements (e.g., 'legs', 'braces', 'pillars')"
    },
    "surface_features": {
        "texture": "Surface quality (e.g., 'smooth', 'rough', 'grained')",
        "reflectivity": "Degree of light reflection (e.g., 'matte', 'glossy', 'mirror-like')",
        "color": "Primary and secondary colors",
        "patterns": "Any repeating design (e.g., 'stripes', 'dots', 'engraved markings')"
    },
    "motion_and_mechanics": {
        "mobility": "Whether it moves (e.g., 'fixed', 'rotating', 'sliding')",
        "articulations": "Joints or moving parts (e.g., 'hinged', 'telescopic', 'ball joint')",
        "center_of_mass": "Position of the balance point",
        "load_capacity": "Maximum supported weight or force"
    },
    "functional_features": {
        "input_interfaces": "How it interacts with users or environment (e.g., 'button', 'lever', 'touchscreen')",
        "output_interfaces": "What it produces (e.g., 'displays', 'openings', 'liquid flow')",
        "power_source": "How it operates (e.g., 'manual', 'electric', 'hydraulic')"
    }
}

def retreive_entity(user_query):
    response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': f"""From the given query, please extract the entity which the user has specified dimensions for.
        Please limit your responses to the entity itself.
        User query: {user_query}
        """
    },
    ])
    # print(response['message']['content'])
    # or access fields directly from the response object
    return response.message.content

def describe_image(entity_path, user_query):
    response: ChatResponse = chat(model='granite3.2-vision', messages=[
    {
        'role': 'user',
        'content': f"""Please describe the given image in detail.
        Image: {entity_path}
        """
    },
        {
        'role': 'system',
        'content': f"""You are a helpful AI Agent designed to analyse images passed in by the user in detail.
        Describe the following properties of the object present inside the image: 
        {str(object_physical_properties)}
        Your response should contain a minimum of 150 words.
        """
    },
    ])
    # print(response['message']['content'])
    # or access fields directly from the response object
    finalResponse = response.message.content+user_query
    return response.message.content


def return_steps_to_build(stepsString):
    response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
        'role': 'user',
        'content': f"""{stepsString}
        """
    },
    ])
    # print(response['message']['content'])
    # or access fields directly from the response object
    return response.message.content

def get_working_code(collatedCodePrompt, errorMessage=None, initialAttempt=True, currentCode=None, max_iters=None):
    if initialAttempt:
        response: ChatResponse = chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': f"""{collatedCodePrompt}
            """
        },
        ])
        # print(response['message']['content'])
        # or access fields directly from the response object
        return response.message.content
    else:
        updated_code = gen_code
        if direct_code:
            for i in range(1, error_iter + 1):
                error_prompt = get_error_prompt(updated_code, error)
                updated_code = get_answers(model, api_key, error_prompt, temp, base_url)
                updated_code = remove_backticks(updated_code)
                macro_path = f"results/code/query_{query_idx}_direct_attempt_{i}.FCMacro"
                write_macro(updated_code, macro_path)
                # PyAutoGUI sequence
                img_path = f"results/images/query_{query_idx}_direct_attempt_{i}.png"
                error_msg = gui_sequence(macro_path, img_path)

                if error_msg is not None:
                    continue
                else:
                    break

        else:
            for i in range(1, error_iter + 1):
                error_prompt = get_error_prompt(updated_code, error)
                updated_code = get_answers(model, api_key, error_prompt, temp, base_url)
                updated_code = remove_backticks(updated_code)
                macro_path = f"results/code/query_{query_idx}_refined_{refined_idx}_attempt_{i}.FCMacro"
                write_macro(updated_code, macro_path)
                # PyAutoGUI sequence
                img_path = f"results/images/query_{query_idx}_refined_{refined_idx}_attempt_{i}.png"
                error_msg = gui_sequence(macro_path, img_path)

                if error_msg is not None:
                    continue
                else:
                    break

        return error_msg, i, updated_code