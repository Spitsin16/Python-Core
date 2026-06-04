class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def show_transactions(self):
        if not self.transactions:
            print('Transaction history is empty')
        else:
            print('Your transactions')
            for transaction in self.transactions:
                print(
                    f'Operation: {transaction['type']}, coin: {transaction['coin']}, coin amount: {transaction['coin_amount']},'
                    f'usdt amount: {transaction['usdt_amount']}, course: {transaction['course']}')

    def add_transaction(self, operation_type, coin_name, coin_amount, usdt_amount, course):
        transaction = {
            'type': operation_type,
            'coin': coin_name,
            'coin_amount': coin_amount,
            'usdt_amount': usdt_amount,
            'course': course
        }
        self.transactions.append(transaction)

