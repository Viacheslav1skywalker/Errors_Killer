import requests
import urllib3
import json
import base64
import uuid
import gigachat_config


def make_correct_credentials():
    credentials = f'{gigachat_config.client_id}:{gigachat_config.client_secret}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encoded_credentials

def get_token(scope='GIGACHAT_API_PERS'):
    rq_uid = str(uuid.uuid4())
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': f'{rq_uid}',
    'Authorization': f'Basic {make_correct_credentials()}'
    }
    payload = {
        'scope':scope
    }

    try:
        responce = requests.post(url,headers=headers,data = payload,verify=False)
        return responce
    except:
        print('Ошибка')
        return -1



def get_chat_message(user_message,token):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        'model':'GigaChat',
        'messages': [
            {
                'role':'user',
                'content':user_message
            }
        ],
        "temperature":1,
        "top_p":0.1,
        "n":1,
        'stream':False,
        "max_tokens":512,
        "repetition_penalty":1,
        "update_interval":0
    })
    headers = {
        'Content-Type':'application/json',
        'Accept':'application/json',
        'Authorization':f'Bearer {token}'
    }

    try:
        responce = requests.request('POST',url,headers=headers,data=payload,verify=False)
        return responce
    except:
        print('error')

# главная функция в модуле, которая вызывает остальные функции в модуле
def main(prompt):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    answer = get_chat_message(prompt, gigachat_config.token)
    if answer.json().get('message'):
        if answer.json()['message'] == 'Token has expired':
            response_get_token = get_token()
            if response_get_token != -1:
                new_token = response_get_token.json()['access_token']
                answer = get_chat_message(prompt,new_token)
                if str(answer) == "<Response [200]>":
                    gigachat_config.token = new_token
                    return answer.json()['choices'][0]['message']['content']
                else:
                    print('ошибка')
                    return -1
            else:
                return -1
        else:
            return 'неизвестная ошибка'
    return answer.json()['choices'][0]['message']['content']

