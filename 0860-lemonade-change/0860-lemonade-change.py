class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # $5와 $10 지폐의 개수
        five, ten = 0, 0
        
        for bill in bills:
            if bill == 5:
                # $5 받으면 거스름돈이 필요 없음
                five += 1
            elif bill == 10:
                # $10 받으면 $5 하나 거스름
                if five == 0:
                    # $5 없다면 거스름돈을 줄 수 없으므로 false
                    return False
                five -= 1
                ten += 1 
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
