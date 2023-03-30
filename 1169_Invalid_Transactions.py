class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        newtrans = []
        names = []
        for i in range(len(transactions)):
            newtrans.append(transactions[i].split(','))
            names.append(newtrans[i][0])
        invalid = []
        keys = set()
        for i in range(len(newtrans)):
            if int(newtrans[i][2]) > 1000:
                keys.add(i)
            for k, value in enumerate(names):
                if (value == newtrans[i][0]) and (newtrans[k][3] != newtrans[i][3]) and (abs(int(newtrans[k][1])-int(newtrans[i][1])) <= 60) and (k != i):
                    keys.add(i)
                    keys.add(k)
        for key in keys:
            invalid.append(transactions[key])
        return invalid
