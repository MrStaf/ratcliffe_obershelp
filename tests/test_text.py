from ratcliff_obershelp import main, parse

class TestText:
    def setup(self):
        self.args = ['test', ';' , 'test']
        parser = parse()
        (options, args) = parser.parse_args(self.args)
        self.options = options
        self.args = args
    def test_text(self):
        assert main(self.options, self.args) == (1, None)

