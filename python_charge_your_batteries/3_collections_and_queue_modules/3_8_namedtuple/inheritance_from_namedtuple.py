from collections import namedtuple


Transaction = namedtuple("Transaction", ["sender", "receiver", "date", "amount"])


class TransactionWithTimestamp(Transaction):
    @property
    def timestamp(self):
        return datetime.datetime.now()

    def __repr__(self):
        return f"TransactionWithTimestamp: {self.timestamp}, {self.date}"
