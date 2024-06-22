class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)  # 루트 노드를 스택에 추가
                current = current.left  # 왼쪽 자식이 있으면 계속 왼쪽으로 이동
            
            current = stack.pop()  # 가장 왼쪽의 노드부터 처리
            result.append(current.val)  # 현재 노드 값을 결과 리스트에 추가
            current = current.right  # 오른쪽 자식 처리
        
        return result
