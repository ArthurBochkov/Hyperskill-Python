class Editor:
    formatters = {
        'plain': ('text',),
        'bold': ('text',),
        'italic': ('text',),
        'header': ('level', 'text'),
        'link': ('label', 'url'),
        'inline-code': ('text',),
        'ordered-list': ('rows',),
        'unordered-list': ('rows',),
        'new-line': ()}

    def __init__(self):
        self.text = None
        self.level = None
        self.label = None
        self.url = None
        self.rows = None
        self.page = ''

    def get_text(self):
        self.text = input('Text:')

    def get_level(self):
        while True:
            answer = input('Level:')
            if not answer.isdigit() or not (1 <= int(answer) <= 6):
                print('The level should be within the range of 1 to 6')
                continue
            self.level = int(answer)
            break

    def get_label(self):
        self.label = input('Label:')

    def get_url(self):
        self.url = input('URL:')

    def get_rows(self):
        while True:
            n = int(input('Number of rows:'))
            if n <= 0:
                print('The number of rows should be greater than zero')
                continue
            self.rows = []
            for i in range(n):
                self.rows.append(input(f'Row #{i+1}'))
            break

    def add_page(self, s):
        self.page += s

    def print_page(self):
        print(self.page)

    def put_plain(self):
        self.add_page(self.text)

    def put_bold(self):
        self.add_page(f'**{self.text}**')

    def put_italic(self):
        self.add_page(f'*{self.text}*')

    def put_header(self):
        self.add_page(f'{"#" * self.level} {self.text}\n')

    def put_link(self):
        self.add_page(f'[{self.label}]({self.url})')

    def put_inline_code(self):
        self.add_page('`' + self.text + '`')

    def put_new_line(self):
        self.add_page('\n')

    def put_ordered_list(self):
        for i,x in enumerate(self.rows):
            self.add_page(f'{i+1}. {x}\n')

    def put_unordered_list(self):
        for x in self.rows:
            self.add_page(f'* {x}\n')

    def do_format(self, form):
        for x in Editor.formatters[form]:
            getattr(self, 'get_' + x)()
        getattr(self, 'put_' + form.replace('-','_'))()
        self.print_page()


    def start(self):
        while True:
            answer = input('Choose a formatter:')
            if answer == '!done':
                with open('output.md', 'w') as f:
                    f.write(self.page)
                break
            if answer == '!help':
                print('Available formatters: ', ' '.join(Editor.formatters.keys()))
                print('Special commands: !help !done')
                continue
            if answer not in Editor.formatters.keys():
                print('Unknown formatting type or command')
                continue
            self.do_format(answer)


if __name__ == '__main__':
    editor = Editor()
    editor.start()