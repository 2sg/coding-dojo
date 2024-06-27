class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        알고리즘 접근 방식은 처음부터 진행되는 순방향과 마지막부터 진행되는 역방향, 2개를 활용해서
        연산을 통해 가장 높은 넓이를 구하는 것입니다.
        '''
        left = 0 # 순방향 시작
        right = len(height)-1 # 역방향 시작
        max_area = 0
        while (right-left>0) :
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
                
            if height[left]>=height[right]: # 순방향이 역방향보다 빠름
                right-=1
            else:
                left+=1
            
        return max_area
        return maxi