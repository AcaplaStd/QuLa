# -*- coding: utf-8 -*-

def sep_string(s: str) -> tuple:
    nums = ''
    assert s != ''
    for i, char in enumerate(s):
        if char.isdigit():
            nums += char
        elif char == '.' and nums[-1] != '.':
            if i < len(s) - 1 and s[i+1] != ' ':
                nums += '.'
            else:
                return nums, s[i+2:], 'question'
        elif char == ':' and nums[-1] != '.' and s[i+1] == ' ':
            return nums, s[i+2:], 'answer'
        else:
            break
    else:
        if char == '.' and nums[-1] != '.':
            return nums, s[i+2:], 'question'
        elif char == ':' and nums[-1] != '.':
            return nums, s[i+2:], 'answer'
    return '', s, 'continue'



def qula_dicts(filename: str) -> tuple:
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    questions = {'ignore': ''}
    answers = {'ignore': {}}
    current_question = 'ignore'
    current_answer = 'ignore'
    current_block = 'question'

    for line in lines:
        if line.isspace():
            continue
        num, txt, txt_type = sep_string(line.strip())
        if txt.startswith('/'):
            txt = txt[1:]
        if txt_type == 'question':
            current_question = num
            current_block = 'question'
            questions[num] = txt
        elif txt_type == 'answer':
            current_block = 'answer'
            if current_question in answers:
                answers[current_question].update({num: txt})
            else:
                answers[current_question] = {num: txt}
        else:
            if current_block == 'question':
                questions[current_question] += '\n' + txt
            elif current_block == 'answer':
                answers[current_answer].update({num: txt})
    return questions, answers


if __name__ == '__main__':
    from pprint import pprint
    questions, answers = qula_dicts('example.qula')
    print('QUESTIONS')
    pprint(questions)
    print('ANSWERS')
    pprint(answers)
