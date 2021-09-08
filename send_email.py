#coding=utf8
import os
import yagmail
from Read_main.read_config import handle_ini

report_dir = '/Users/tanlinhai/PycharmProjects/pythonProject2/TestReport/'
sendEmail = handle_ini.get_value('send_email', 'email')
password = handle_ini.get_value('password', 'email')
smtp = handle_ini.get_value('smtp', 'email')
toEmail = handle_ini.get_value('to_email', 'email')

def sendMail():
    # 将测试报告文件夹下的所有文件名作为一个列表返回
    lists = os.listdir(report_dir)

    # 对所有测试报告按照生成时间进行排序
    lists.sort(key=lambda filename: os.path.getmtime(report_dir+filename))

    # 获取最新的测试报告
    recent = lists[-1]

    # 指定最新的测试报告路径
    report_file = os.path.join(report_dir, recent)

    # 填写登录信息
    yag = yagmail.SMTP(sendEmail, password, smtp)

    # 将测试报告作为附件发送
    yag.send(toEmail, subject="自动化测试报告", contents=report_file)
    print('----------\n\033[1;31m发送邮件成功!\033[1;31;0m\n----------')

if __name__ == '__main__':
    sendMail()
