class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        diglogs = [log for log in logs if log[-1].isdigit()]
        letlogs = [log for log in logs if log[-1].isalpha()]
        
        letrev = []
        for log in letlogs:
            sptlst = log.split()
            rev = ' '.join(sptlst[1:]) + " " + sptlst[0]
            letrev.append(rev)
        sortedlet = sorted(letrev)
        
        actual = []
        for log in sortedlet:
            lst = log.split()
            rev = lst[-1] + ' ' + ' '.join(lst[:-1])
            actual.append(rev)
        return actual + diglogs