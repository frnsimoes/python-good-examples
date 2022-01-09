# HB, OOP

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __truediv__(self, scalar: int):
        return self.__class__(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class Rect:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def center(self):
        return (self.top_left + self.bottom_right) / 2

    @staticmethod
    def two_plus_two():
        return 2 + 2

    def __repr__(self):
        return f'{self.__class__.__name__}({self.top_left!r}, {self.bottom_right!r})'


def test_rect():
    r = Rect(Point(1, 1), Point(3, 3))

    assert isinstance(r, Rect)
    assert r.top_left == Point(1, 1)
    assert r.bottom_right == Point(3, 3)
    assert r.center() == Point(2, 2)
    assert repr(r) == 'Rect(Point(1, 1), Point(3, 3))'

def test_point():

    p = Point(2, 4)
    assert isinstance(p, Point)
    assert p.x == 2
    assert p.y == 4


if __name__ == '__main__':
    r = Rect(Point(1, 1), Point(3, 3))
    print(r.center)  # <bound method Rect.center of Rect(Point(1, 1), Point(3, 3))>
    print(Rect.center)  # <function Rect.center at 0x1015a38b0>
    """
    O bound method é um método que tem a referência completa da função que ele vai executar e da instância associada.

    Quando chamo `r.center`, O python pergunta para o `r` se ele conhece o `center`, executando: `getattr(r, 'center')`

    o `r` olha para si mesmo e se pergunta: será que conheço o center?
    E ele não conhece.

    >>> r.__dict__
    {'top_left': Point(1, 1), 'bottom_right': Point(3, 3)}

    O r só sabe quem é o top_left e o bottom_right.
    O r conhece o que está no __init__ do Rect.

    Se o r não conhece o center, como, ao chamar r.center, há mensagem de retorno que referencia Rect.center?

    Ao chamar o center, o Python pergunta se o center está no r. Não está. Então ele sobe a hierarquia, até chegar no object,
    classe da qual todas as classes derivam.

    Se o python não encontrar o center na hierarquia dos objetos, ocorrerá um erro.
    No nosso caso, o python encontrou o center.

    Assim, o python instancia um objeto 'método' referenciando ao mesmo tempo a instância e a função.

    r.center é um bound method, voltando.

    >>> c = r.center
    >>> c
    <bound method Rect.center of Rect(Point(1, 1), Point(3, 3))>
    >>> c()
    Point(2.0, 2.0)

    >>> c.__self__
    Rect(Point(1, 1), Point(3, 3))
    >>> c.__func__
    <function Rect.center at 0x100bf6e50>


    c() já é um objeto, já passou pelo processo de encontrar a mensagem. Internamente no estado desse objeto encontram-se
    o c.__self__ e o c.__func__. c.__self__ é o `r`. c.__func__ é o objeto função referenciado pelo center em Rect.

    Não é simplesmente uma chamada de função. Internamente, c() equivale a c.__call__().

    >>> c.__func__(c.__self__)
    Point(2.0, 2.0)

    __call__ faz exatamente: c.__func__(c.__self__). É uma passagem de mensagem. É um processo de indireção, de descoberta de qual
    é o código adequado para se chamar. Isso acontece em tempo de execução, em oposição a Java e outras linguagens que acontece em tempo
    de compilação.

    Chamada de método não é apenas uma chamada de uma função.
    Isso se chama polimorfismo.

    """
class Test
    def __init_(self):
        pass
