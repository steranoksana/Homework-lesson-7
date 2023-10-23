# import re
#
# li = ['0876-32 -33-66', '044-876-88-09', '+38-097-765-99-34', '+38-096-754-97-18', 'jkjhgffghkj',
#       '099-765-99-99', '0667658876']
#
# for val in li:
#     if re.findall(r'^[+]?[0-9]{2}-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$', val) and 10 <= len(val) <= 17:
#         print(val)
#
#     elif re.findall(r'^[0]{1}[0-9]{9}$', val) and len(val) == 10:
#         print(val)
#
#     else:
#         print("incorrect")

#
# import re
# test_data = ["Vasyliuk Oksana Petrivna", "Vasyliuk, oksana petrivna", "vasyliuk oksana oksana petrivna"]
# regex = re.compile(r'^[A-ZA-ЯЕЇІГЄ]{1}[a-za-яеїігє]{2,10}\s[A-ZA-ЯЕЇІГЄ]{1}[a-za-яеїігє]{2,10}\s[A-ZA-ЯЕЇІГЄ]{1}[a-za-яеїігє]{2,10}$')
# for item in test_data:
#     print(regex.match(item))