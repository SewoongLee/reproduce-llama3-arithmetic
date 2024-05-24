import random

def nshot_prompt(data: list, n: int, question: str) -> str:
    prompt = ''
    for qna in random.sample(data, n):
        prompt += f'''
        <s>[INST]{qna["question"]}[/INST]
        Assistant: {qna["answer"]}</s>
        '''

    return prompt + '<s>[INST]' + question + '[/INST]'  # no end tag </s> here!

def parse_into_num_ans(full_answer: str) -> int:
    delimiter = '####'
    if delimiter not in full_answer:
        return None
    
    return int(full_answer.split(delimiter)[1].replace(',',''))