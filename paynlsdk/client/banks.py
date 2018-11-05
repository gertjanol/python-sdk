
class Banks(object):
    @staticmethod
    def get_list():
        """
        Gets the list of banks.

        Please note this method is a mapping from the paynlsdk.client.transaction.Transaction.get_banks() method,
        that returns the internal List object of banks.
        :return: List of banks
        :rtype: list
        """
        from paynlsdk.client.transaction import Transaction
        return Transaction.get_banks().banks

    @staticmethod
    def get_list_response():
        """
        Get a get_banks :class:`paynlsdk.api.transaction.getbanks.Response` instance

        Please note this method is a mapping from the paynlsdk.client.transaction.Transaction.get_banks() method,
        that returns the internal List object of banks.
        :return: Response object
        :rtype: paynlsdk.api.transaction.getbanks.Response
        """
        from paynlsdk.client.transaction import Transaction
        return Transaction.get_banks()

