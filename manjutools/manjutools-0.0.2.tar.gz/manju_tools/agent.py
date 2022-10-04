from fake_useragent import UserAgent

class RandomUserAgentMiddlware:
    def getRandom(self):
        return UserAgent().random

demo = RandomUserAgentMiddlware()
str = demo.getRandom()
print(f'ramdomAgent: {str}')
