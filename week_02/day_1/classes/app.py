from modules.bank_account import *

bank_account = BankAccount("john", -100, "personal")
bank_account1 = BankAccount("Bob", -500, "personal")

bank_account.pay_monthly_fee()
print(bank_account.balance)
bank_account1.pay_monthly_fee()
print(bank_account1.balance)

# print(bank_account.holder_name)
# # print(bank_account.balance)
# # print(bank_account.type)

# bank_account.holder_name = "Azzizal"
# print(bank_account.holder_name)

# bank_account.pay_in(100000)
# print(bank_account.balance)
# bank_account1.pay_in(50)
# print(bank_account1.balance)

# bank_account.pay_monthly_fee()
# print(bank_account.balance)

# account = {
#     "holder_name": "John",
#     "balance": 500,
#     "type": "business",
# }

# print(get_account_name(account))


