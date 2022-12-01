class Account:
    def __init__(self, account_number, account_owner, account_balance, credit_limit):
        self.__account_number = account_number
        self.__account_owner = account_owner
        self.__account_balance = account_balance
        self.__credit_limit = credit_limit

    def return_bank_extract(self):
        return {
            "titular": self.__account_owner,
            "saldo": self.__account_balance
        }

    def deposits_money(self, amount_deposited):
        self.__account_balance += amount_deposited

    def withdraws_money(self, withdrawn_amount):
        if not self.__can_withdraw_money(withdrawn_amount):
            return {"Valor de saque não pode ser maior que o saldo da conta. Saldo disponível: {}".format(
                self.__account_balance
            )}
        self.__account_balance -= withdrawn_amount

    def __can_withdraw_money(self, withdrawn_amount):
        withdrawal_greater_than_balance = self.__account_balance - withdrawn_amount < 0
        return not withdrawal_greater_than_balance

    def transfer_money(self, transfer_destination, amount_transferred):
        self.withdraws_money(amount_transferred)
        transfer_destination.deposits_money(amount_transferred)

    @property
    def account_balance(self):
        return self.__account_balance

    @property
    def credit_limit(self):
        return self.__credit_limit

    @credit_limit.setter
    def credit_limit(self, new_limit):
        self.__credit_limit = new_limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {
            "BB": "001",
            "Caixa": "104",
            "Bradesco": "237"
        }
