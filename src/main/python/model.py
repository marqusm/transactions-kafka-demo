class Transaction:
    def __init__(self, transaction_id, src_account_id, dst_account_id, amount, timestamp):
        self.transaction_id = transaction_id
        self.src_account_id = src_account_id
        self.dst_account_id = dst_account_id
        self.amount = amount
        self.timestamp = timestamp
