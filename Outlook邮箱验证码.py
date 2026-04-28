from exchangelib import Credentials, Account, Configuration, DELEGATE
import re

credentials = Credentials('WWzjbbzj11@outlook.com', 'Kytxbbxx123')

try:
    # 尝试使用自动发现功能创建 Account 对象
    account = Account(primary_smtp_address='WWzjbbzj11@outlook.com', credentials=credentials, autodiscover=True)
except Exception as e:
    # 自动发现失败时，使用手动配置创建 Account 对象
    config = Configuration(server='outlook.office365.com', credentials=credentials)
    account = Account(primary_smtp_address='WWzjbbzj11@outlook.com', config=config, autodiscover=False, access_type=DELEGATE)

for item in account.inbox.all().order_by('-datetime_received')[:1]:
    login_code = item.text_body
    code = re.search(r'Your Poe verification code is:\s+(\d+)', login_code).group()
    code_ = re.search(r'\d+', code).group()
    print(code_)
    # login_code = item.subject
    # code_ = re.search(r'\d+', login_code).group()
    # print(code_)
