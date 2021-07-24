# https://leetcode.com/problems/design-hashmap/
class MyHashMap:
    PRIME = 31  # 문제의 키가 정수로만 넘어와서 사실 필요 없는 변수
    TABLE_SIZE = 300

    class ListNode:
        def __init__(self, key = 0, value=0, next=None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self.hash_table = [None] * self.TABLE_SIZE

    """
    index와 key는 다르다!
    """
    def put(self, key: int, value: int) -> None:
        index = self.get_index(key)
        head = self.hash_table[index]
        if head is None:
            self.hash_table[index] = self.ListNode(key, value)
            return None
        else:
            # 새로운 리스트 노드를 앞에 붙여야 할까? 아니면 뒤에 붙여야 할까?
            while head is not None:
                if head.key == key:
                    # 키가 같으면 넘어온 값으로 치환하고 종료
                    head.value = value
                    return None
                if head.next is not None:
                    head = head.next
                else:
                    break
            # next에 붙여 나갈 생각을 했는데, 오히려 가장 앞에 붙이는 게 더 편하다
            # 새로운 노드를 "가장 앞"에 추가하여 hash_table에 삽입
            self.hash_table[index] = self.ListNode(key, value, self.hash_table[index])

            return None

    def get(self, key: int) -> int:
        head = self.hash_table[self.get_index(key)]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        return -1

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        head = self.hash_table[index]
        if head is None:
            return None
        else:
            # key에 해당 하는 노드 제거
            # 이전 노드와 다음 노드를 이어준다
            # 첫번째 헤드에 해당하면 바로 다음 노드로 덮어 쓴다
            if head.key == key:
                self.hash_table[index] = head.next
                return None
            # https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
            while head is not None:
                if head.key == key:
                    break
                node_prev = head
                head = head.next

            # AttributeError: 'NoneType' object has no attribute 'next'
            # key에 해당하는 게 없으면 None일 수 있으므로, None 아닌 경우에만 삭제 처리
            if head is not None:
                node_prev.next = head.next

            return None

    # 정수만 들어오므로 테이블 크기로 모듈러 연산만 한다
    def get_index(self, key: int):

        return key % self.TABLE_SIZE