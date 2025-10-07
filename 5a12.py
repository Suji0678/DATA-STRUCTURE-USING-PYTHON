class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff  
        self.exp = exp      
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        result = []
        while current is not None:
            if current.coeff != 0:
                result.append(f"{current.coeff}x^{current.exp}")
            current = current.next
        print(" + ".join(result) if result else "0")

    def add(self, other):
        p1 = self.head
        p2 = other.head
        result = LinkedList()

        while p1 is not None and p2 is not None:
            if p1.exp == p2.exp:
                coeff_sum = p1.coeff + p2.coeff
                if coeff_sum != 0:
                    result.insert(coeff_sum, p1.exp)
                p1 = p1.next
                p2 = p2.next
            elif p1.exp > p2.exp:
                result.insert(p1.coeff, p1.exp)
                p1 = p1.next
            else:
                result.insert(p2.coeff, p2.exp)
                p2 = p2.next

        while p1 is not None:
            result.insert(p1.coeff, p1.exp)
            p1 = p1.next

        while p2 is not None:
            result.insert(p2.coeff, p2.exp)
            p2 = p2.next

        return result


def get_polynomial():
    poly = LinkedList()
    n = int(input("Enter number of terms: "))
    print("Enter terms in decreasing order of exponents:")
    for _ in range(n):
        coeff = int(input("Coefficient: "))
        exp = int(input("Exponent: "))
        poly.insert(coeff, exp)
    return poly


# Input from user
print("Enter first polynomial:")
poly1 = get_polynomial()

print("Enter second polynomial:")
poly2 = get_polynomial()

# Display input polynomials
print("\nPolynomial 1:")
poly1.display()
print("Polynomial 2:")
poly2.display()
# Add polynomials
result_poly = poly1.add(poly2)
print("\nSum of Polynomials:")
result_poly.display()
