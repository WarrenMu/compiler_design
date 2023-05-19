# testing/unit_tests.py

# Implement unit tests for individual components here
# testing/unit_tests.py

import unittest
from lexer.lexer import Lexer
from parser.parser import Parser
from semantic_analysis.analyzer import SemanticAnalyzer
from intermediate_representation.ir_generator import IRGenerator
from code_generation.code_generator import CodeGenerator

class CompilerUnitTests(unittest.TestCase):
    # ...

    def test_language_syntax(self):
        # Test the language syntax definition
        source_code = """
            function greet(name) {
                print("Hello, " + name + "!");
            }
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        # Add assertions to check the correctness of the parsed AST

    def test_language_features(self):
        # Test specific language features
        # Example: Test if conditional statements work as expected
        source_code = """
            function max(a, b) {
                if (a > b) {
                    return a;
                } else {
                    return b;
                }
            }
        """
        compiled_code = compile(source_code)
        result = execute(compiled_code)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
