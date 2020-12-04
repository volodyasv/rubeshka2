class CustomQueue:
    def __init__(self):
        self.items = []
        self.popedVeterans = 0

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if item == 'veteran':
            self.items.insert(self.size(),item)
        else:
            self.items.insert(0,item)
        print('push ' + item)

    def pop(self):
        if self.popedVeterans == 3:
            print('----')
            self.popedVeterans = 0
            for i in range(self.size() - 1, 0, -1):
                if self.items[i] == 'citizen':
                    print('pop ' + self.items[i])
                    return self.items.pop(i)
            print('pop ' + self.items[self.size() - 1])
            return self.items.pop()
        else:
            print('++++')
            if self.items[self.size() - 1] == 'veteran':
                print('====')
                self.popedVeterans += 1
            print('pop ' + self.items[self.size() - 1])
            return self.items.pop()

    def size(self):
        print('size ' + str(len(self.items)))
        return len(self.items)


q = CustomQueue()

q.size()
q.push('veteran')
q.size()
q.push('veteran')
q.size()
q.push('veteran')
q.size()
q.push('veteran')
q.size()
q.push('citizen')
q.size()
q.push('veteran')
q.size()
q.push('citizen')
q.size()

q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()