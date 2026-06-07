class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def show_transactions(self):
        if not self.transactions:
            print('Transaction history is empty')
        else:
            print('Your transactions')
            for transaction in self.transactions:
                operation_type = transaction['type']
                if operation_type =='buy' or operation_type =='sell':
                    print(
                        f'Operation: {transaction['type']}, coin: {transaction['coin']}, coin amount: {transaction['coin_amount']},'
                        f'usdt amount: {transaction['usdt_amount']}, course: {transaction['course']}')
                else:
                    print(
                        f'Operation: {transaction['type']}, coin: {transaction['coin']}, coin amount: {transaction['coin_amount']},'
                        f'uid: {transaction['recipient_uid_add']}')



    def add_transaction(self, operation_type, coin_name, coin_amount, usdt_amount, course):
        transaction = {
            'type': operation_type,
            'coin': coin_name,
            'coin_amount': coin_amount,
            'usdt_amount': usdt_amount,
            'course': course
        }
        self.transactions.append(transaction)

    def add_transaction_transfer(self,operation_type, coin_you_want_to_transfer, coin_value_you_want_to_transfer,recipient_uid_add):
        transaction = {
            'type': operation_type,
            'coin':  coin_you_want_to_transfer,
            'coin_amount': coin_value_you_want_to_transfer,
            'recipient_uid_add':recipient_uid_add
        }
        self.transactions.append(transaction)

