from ollama import chat
from ollama import ChatResponse

def retreive_entity():
    response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
        'role': 'user',
        # 'content': f"""Write python code to generate a solid sphere in freeCAD software.
        'content': f"""What is photosynthesis?
        """
    },
    ])
    # print(response['message']['content'])
    # or access fields directly from the response object
    r = response.message.content
    return r

print(retreive_entity()+'some special thing')
