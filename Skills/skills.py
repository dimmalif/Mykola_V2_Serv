import re


class BFunction:
    def __init__(self, text_data=None):
        self.text_data = text_data

        self.__validator()

    def reject(self):
        result_data = re.findall(r'\w+\s(\w+|\w+\s?\w+)\s?[будь ласка]*\s(.+)', self.text_data)
        return result_data

    def __validator(self):
        if not isinstance(self.text_data, str | None):
            raise TypeError('Only str')
        else:
            self.command = self.reject()[0]
            self.request = self.reject()[-1]

    def __repr__(self):
        return f'Command: {self.reject()[0][0]}\nRequest: {self.reject()[0][-1]}'


