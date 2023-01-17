def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(2,4)
print(resultado)

import unittest

class purebas(unittest.TestCase):
    
    def test(self):
        self.assertEqual(multiplicar(2,4),8)
        self.assertEqual(multiplicar(2,4),8)
        
if __name__ == '__main__':
    unittest.main()