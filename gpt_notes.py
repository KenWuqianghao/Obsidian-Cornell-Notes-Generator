import openai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()
openai.api_key  = os.getenv('OPENAI_API_KEY')

def split_prompt(text):
    prompt = '''
Write cascaded bullet point Cornell notes for the following text; each cue should have a TLDR after the cue, followed by supporting bullet points. You can imagine it like a csv file with three columns consisting of cue, TLDR, and bullet points.

Remember, every cue should be it's own section in the format like below
Cue:
TLDR:
    '''

    instruction = '''
    The total length of the content that I want to send you is too large to send in only one piece.
        
For sending you that content, I will follow this rule:
        
[START PART 1/10]
this is the content of the part 1 out of 10 in total
[END PART 1/10]
        
Then you just answer: "Received part 1/10"
        
And when I tell you "ALL PARTS SENT", then you can continue processing the data and answering my requests.

    '''

    split_length = 2048 - len(prompt)

    if split_length <= 0:
        raise ValueError("Max length must be greater than 0.")

    num_parts = -(-len(text) // split_length)

    file_data = [
        {'role': 'system', 'content': instruction}
    ]

    for i in range(num_parts):
        start = i * split_length
        end = min((i + 1) * split_length, len(text))

        if i == num_parts - 1:
            content = f'[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
            content += '\nALL PARTS SENT. Now you can continue processing the request.'
            file_data.append({
                'role' : 'user',
                'content' : content
            })

            response = 'All parts have been received. How can I help you further?'
            file_data.append({
                'role' : 'assistant',
                'content' : response
            })
            
        else:
            content = f'Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part {i + 1}/{num_parts} received" and wait for the next part.\n[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
            content += f'\nRemember not answering yet. Just acknowledge you received this part with the message "Part {i + 1}/{num_parts} received" and wait for the next part.'
            file_data.append({
                'role' : 'user',
                'content' : content
            })

            response = 'Part {}/{} received. Please proceed with the next part.'.format(i + 1, num_parts)
            file_data.append({
                'role' : 'assistant',
                'content' : response
            })

    file_data.append({
        'role' : 'user',
        'content' : prompt
    })

    return file_data

def response_formatter(input):
    notes = '''```timeline
[spaced-paragraph]
    '''

    previous_line_was_quick_explanation = False

    for line in input.splitlines():
        if line.startswith('Cue: '):
            notes = notes + '+##' + line[4:] + '\n'
            previous_line_was_quick_explanation = False
        elif line.startswith('TLDR: '):
            notes = notes + '+TLDR: ' + line[6:] + '\n'
            previous_line_was_quick_explanation = True
        else:
            if previous_line_was_quick_explanation:
                notes = notes + '+' + line + '\n'
                previous_line_was_quick_explanation = False
            else:
                notes = notes + line + '\n'
    
    notes = notes + '```'

    return notes

def generate_notes(text):
    notes = ''
    messages = split_prompt(text)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = response['choices'][0]['message']['content']
    
    notes = response_formatter(response)

    return notes