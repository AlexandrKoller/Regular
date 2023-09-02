from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

def clean_contact_list(some_list):
    clean_contact_all = []
    for contact in some_list:
        clean_contact = []
        for line in contact:
            if len(line) >= 1:
                clean_contact.append(line)
        clean_contact_all.append(name_organization(clean_contact))
    return clean_contact_all


def name_organization(list):
    new_list_contact = []
    for value in list:
        if value.istitle() is True:
            name_contact = value.split()
            new_list_contact.extend(name_contact)
        else:
            new_list_contact.append(value)
    return new_list_contact


def new_contact_list(some_list):
    new_contact_list = []
    name_list = []
    for value in some_list:
        i = 0
        for data_1 in some_list:
            contact = []
            if data_1[0] == value[0] and value != data_1:
                contact.extend(value)
                for data_2 in data_1:
                    if contact.count(data_2) != 1 and data_2.upper() == True:
                        contact.append(data_2)
                    if (contact.count(data_2) != 1 and data_2.istitle() != True) and data_2.upper() != True:
                        contact.insert(4, data_2)

                name_list.append(value[0])
                if name_list.count(data_1[0]) == 1:
                    new_contact_list.append(contact)
        if name_list.count(value[0]) == 0:
            new_contact_list.append(value)

    return new_contact_list

def phone_number_refactor(some_list):
    complit_list = []
    subst_pattern = r"\+7 (\2) \3-\4-\5\6\7"
    pattern = re.compile(
        r"(\+7|8)\s?\(?(\d{3})\)?[\s|\-]?(\d{3})[\s|\-]?(\d{2})[\s|\-]?(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*")
    for kist in some_list:
        num_list = []
        for value in kist:
            result = pattern.sub(subst_pattern, value)
            num_list.append(result)
        complit_list.append(num_list)
    return complit_list



with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

b = clean_contact_list(contacts_list)
p = new_contact_list(b)

phone_list = phone_number_refactor(p)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(phone_list)
