# -*- coding: utf-8 -*-
# @Time    : 2020-06-25 11:37
# @Author  : liudongyang
# @FileName: schedule.py
# @Software: PyCharm
# 任务调度
import threading
import time
import os
from make_data import MakeData
from save_data import SaveFile
from parm import savenum, stifnum, filenum, zip_floder
from Common import CommonFunction
comm = CommonFunction()
savedata = SaveFile()
# 临时存储生成数据
orgs = []
persons = []
certs = []
addresses = []
contacts = []
relations = []
banks = []
trust_conts = []
beneficiarys = []
app_conts = []
contracts = []
trades = []
# data_path = os.path.join(zip_floder, 'data')
data_path = zip_floder

def __threads(all_data, all_table_name, file_date_time, order, sign):
    """抽出多线程部分"""
    threads = []
    for ind, dat in enumerate(all_data):
        if len(eval(dat)):
            thr = threading.Thread(target=savedata.write_to_csv, args=(
                eval(dat), all_table_name[ind], file_date_time, order, sign))
            thr.start()
            threads.append(thr)

    for t in threads:
        t.join()

def __control_file(file_name, file_date_time, file_num):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    file_full = os.path.join(data_path, 'D{}-T{}_00{}.txt'.format(
        file_date_time, currt_time, 1))
    filename = '{}-D{}-T{}_00{}.csv'.format(file_name, file_date_time, currt_time, file_num)
    with open(file_full, '+a', encoding="UTF-8") as f:
        f.write(','.join([filename, str(savenum)]) + "\n")

def person(num, file_date_time):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    makedata = MakeData('1')
    person = makedata.make_person(num)
    persons.append(person)
    cert = makedata.make_cert()
    certs.append(cert)
    address = makedata.make_address()
    addresses.append(address)
    contact = makedata.make_connect()
    contacts.append(contact)
    relation = makedata.make_relation()
    relations.append(relation)
    bank = makedata.make_account()
    banks.append(bank)
    trust_cont = makedata.make_trust_contract(num)
    trust_conts.append(trust_cont)
    beneficiary = makedata.make_beneficiary()
    beneficiarys.append(beneficiary)
    app_cont = makedata.make_apply_contract(num)
    app_conts.append(app_cont)
    contract = makedata.make_contract_balance()
    contracts.append(contract)
    trade = makedata.make_transaction()
    trades.append(trade)

    # 存储文件
    data_list = [persons, certs, addresses, contacts, relations, banks, trust_conts, beneficiarys, app_conts,
                 contracts, trades]
    name_list = ["person", "cert", "addresse", "contact", "relation", "account", "trust_contract",
                 "beneficiary", "apply_contract", "contract_balance", "transaction"]
    if len(persons) % filenum == 0:
        savetxt = SaveFile()
        for inde, data in enumerate(data_list):
            savetxt.write_to_txt(data, name_list[inde], file_date_time)


def org(num, file_date_time):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    makedata = MakeData('2')
    org = makedata.make_org(num)
    orgs.append(org)
    cert = makedata.make_cert()
    certs.append(cert)
    address = makedata.make_address()
    addresses.append(address)
    contact = makedata.make_connect()
    contacts.append(contact)
    relation = makedata.make_relation()
    relations.append(relation)
    bank = makedata.make_account()
    banks.append(bank)
    trust_cont = makedata.make_trust_contract(num)
    trust_conts.append(trust_cont)
    beneficiary = makedata.make_beneficiary()
    beneficiarys.append(beneficiary)
    app_cont = makedata.make_apply_contract(num)
    app_conts.append(app_cont)
    contract = makedata.make_contract_balance()
    contracts.append(contract)
    trade = makedata.make_transaction()
    trades.append(trade)

    # 存储文件
    data_list = [orgs, certs, addresses, contacts, relations, banks, trust_conts, beneficiarys, app_conts,
                 contracts, trades]
    name_list = ["organization", "cert", "addresse", "contact", "relation", "account", "trust_contract",
                 "beneficiary", "apply_contract", "contract_balance", "transaction"]
    if len(orgs) % filenum == 0:
        savetxt = SaveFile()
        for inde, data in enumerate(data_list):
            savetxt.write_to_txt(data, name_list[inde], file_date_time)


def main(beg, end, stif_time, file_date_time):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    # 日期格式转换
    stif_time = comm.turn_date10(stif_time)
    for num in range(beg, end):
        org(num, file_date_time)
        person(num, file_date_time)
