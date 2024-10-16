
class Jar():
    def __init__(self, cookies=0, capacity=12):
        if capacity < 0:
            raise ValueError
    
        self._capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return self.cookies*"🍪"
    
    def deposit(self, num_cookies):
        if num_cookies + self.cookies > self.capacity:
            raise ValueError
        else:
            self.cookies += num_cookies

    def withdraw(self, num_cookies):
        if num_cookies > self.cookies:
            raise ValueError
        else:
            self.cookies -= num_cookies

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self.cookies
    

def main():
    j = Jar()

    print(j)


if __name__ == "__main__":
    main()