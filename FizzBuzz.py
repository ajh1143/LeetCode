class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        Listify = []
        for each in range(1,n+1):
            if each%(3*5) == 0:
                Listify.append("FizzBuzz"),
            elif each%3 == 0:
                Listify.append("Fizz"),
            elif each%5 == 0:
                Listify.append("Buzz"),
            else:
                Listify.append(str(each)),
        return (Listify)
