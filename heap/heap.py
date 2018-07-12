class Heap:
    
    def __init__(self,data=None):
        self.data = data if data else []
        if data:
            self.build_min_heap()
    
    def __len__(self):
        return len(self.data)
    
    parent = lambda self, i : (i-1)//2
    left = lambda self, i: 2*i + 1
    right = lambda self, i: 2*i + 2

    def __getitem__(self,i):
        return self.data[i]

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def heapify(self,i): #O(lgN)
        if i > len(self):
            return

        left, right = self.left(i), self.right(i)
        smallest = i
        if  left>=0 and left < len(self) and self[i] > self[left]:
            smallest = left

        if right>=0 and right < len(self) and self[i] > self[right]:
            smallest = right    

        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest],self.data[i]
            self.heapify(smimporallest)
 
    def heappop(self): # O(1)
        data = self.data.pop(0)
        self.heapify(0)
        return data
    
    def heappush(self,i):
        self.data.append(i)
        self.build_min_heap()

    def build_min_heap(self): #O(N)
        for i in range((len(self)-1)//2,-1,-1):
            self.heapify(i)
    

if __name__ == '__main__':
    h = Heap([1,3,7,6,4,9,6,12,45,23,78,56])
    print(h)
