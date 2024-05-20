def parse_into_num_ans(full_answer: str) -> int:
    delimiter = '####'
    if delimiter not in full_answer:
        return None
    
    return int(full_answer.split(delimiter)[1].replace(',',''))

def nshot_prompt(data: list, n: int, question: str) -> str:
    prompt = ''
    for i in range(n):
        prompt += f'''
        <s>[INST]{data[i]["question"]}[/INST]
        Assistant: {data[i]["answer"]}</s>
        '''

    return prompt + '<s>[INST]' + question + '[/INST]'  # no end tag </s> here!