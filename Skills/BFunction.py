import re


class BFunction:
    def __init__(self, text_data=None):
        self.text_data = text_data
        self.__validator()

    def reject(self):
        result_data = re.findall(r'\w+\s(\w+|\w+\s?\w+)\s?[будь ласка]*\s(.+)', self.text_data)
        return result_data

    def __validator(self):

        # Через необхідність обов'язкової текст дати(без неї по кд ерори лізуть при перетворенні мп4 в мп3) наступна
        # умова, треба тестити інші ф-ї.
        if self.text_data is None:
            self.request = None
            return None

        if not isinstance(self.text_data, str | None):
            raise TypeError('Only str')
        else:
            # self.command = self.reject()[0] ('скечей', 'гимн панков') - команда, ('скечей', 'гимн панков') - запит,
            # [('скечей', 'гимн панков')] - загал self.request = self.reject()[-1]
            self.command = self.reject()[0][0]
            self.request = self.reject()[0][-1]

        # видалення зайвих слів з запиту:
        to_del = re.findall(r'пісню', self.request)
        if to_del:
            self.request = self.request.replace(to_del[0], '') # так і не зрозумів чому без self.request = ... не працює
            # print(f"{self.request} - del words")

        # print(f"{self.command} - команда")
        # print(f"{self.request} - запит")
        # print(f"{self.reject()} - загал")

    def __repr__(self):
        return f'Command: {self.reject()[0][0]}\nRequest: {self.reject()[0][-1]}'


