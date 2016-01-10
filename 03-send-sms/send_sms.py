import requests


send_phonenumber = '01022205736'


def register_sender_phonenumber(phonenumber, comment):
    # 발신번호 사전 등록 API

    base_url = "http://api.openapi.io/ppurio/1/sendnumber/save/dobestan"

    headers = {
        'x-waple-authorization': 'YOUR-X-WAPLE-AUTHORIZATION',
    }

    payload = {
        'sendnumber': phonenumber.replace('-', ''),
        'comment': comment,
    }

    response = requests.post(
        base_url,
        data=payload,
        headers=headers,
    )


def send_sms(send_phone, dest_phone, content, subject=None):
    """
    (주)케이티하이텔 에서 서비스하는 API STORE 에서 제공하는
    대용량 SMS 서비스를 이용하고 있습니다.

    관련 문서는 아래의 링크에서 찾아보실 수 있습니다 :

    - http://www.apistore.co.kr/api/apiProviderGuide.do?service_seq=151
    - http://www.apistore.co.kr/file/docDownloadSeq.do?doc_seq=124&service_seq=151
    """

    base_url = "http://api.openapi.io/ppurio/1/message/sms/dobestan"

    headers = {
        'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg==',
    }

    payload = {
        'send_phone': send_phone,  # 단, 발신번호 사전 등록제 시행에 따라 사전 등록된 휴대폰 번호로만 발송하실 수 있습니다.
        'dest_phone': dest_phone,
        'msg_body': content,
        'subject': subject,
    }

    response = requests.post(
        base_url,
        data=payload,
        headers=headers,
    )


f = open('phonenumber.sample.csv', 'r')


# 발신번호를 미리 등록하셔야 SMS가 발송됩니다.
register_sender_phonenumber(
    send_phonenumber,
    '업무 자동화를 위한 파이썬 입문 CAMP',
)


for line in f.readlines():
    phonenumber = line.strip()
    content = "안녕하세요. 다방 보고 연락드렸습니다. 전화주세요."

    print("Send SMS to {phonenumber}".format(phonenumber=phonenumber))
    send_sms(
        send_phonenumber, # 이 번호는 사전 등록된 번호입니다.
        phonenumber,
        content,
    )


f.close()
