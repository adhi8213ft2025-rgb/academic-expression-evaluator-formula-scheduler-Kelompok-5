# =========================
# NODE TREE
# =========================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# =========================
# NODE STACK LINKED LIST
# =========================
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# =========================
# STACK LINKED LIST
# =========================
class Stack:
    def __init__(self):
        self.top_node = None

    def is_empty(self):
        return self.top_node is None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if not self.is_empty():
            temp = self.top_node
            self.top_node = self.top_node.next
            return temp.data
        return None

    def top(self):
        if not self.is_empty():
            return self.top_node.data
        return None


# =========================
# GLOBAL VARIABLE
# =========================
variables = {}
defined_expression = ""


# =========================
# TOKENIZER (mendukung nama variabel multi-karakter seperti F1, F2, abc)
# =========================
def tokenize(expression):
    """
    Memecah ekspresi menjadi token. Mendukung:
    - Angka (bulat / desimal)
    - Nama variabel multi-karakter (huruf + angka, contoh: F1, F2, abc)
    - Operator: + - * / ^ 
    - Tanda kurung: ( )
    """
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]

        # Lewati spasi
        if ch == ' ':
            i += 1
            continue

        # Angka (termasuk desimal)
        if ch.isdigit() or (ch == '.' and i + 1 < len(expression) and expression[i+1].isdigit()):
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            tokens.append(expression[i:j])
            i = j

        # Variabel / nama (huruf diikuti huruf/angka, misal: F1, F2, a, b, abc)
        elif ch.isalpha():
            j = i
            while j < len(expression) and (expression[j].isalnum() or expression[j] == '_'):
                j += 1
            tokens.append(expression[i:j])
            i = j

        # Operator dan kurung
        elif ch in ('+', '-', '*', '/', '^', '(', ')'):
            tokens.append(ch)
            i += 1

        else:
            print(f"[PERINGATAN] Karakter tidak dikenal diabaikan: '{ch}'")
            i += 1

    return tokens


# =========================
# CEK TOKEN ADALAH ANGKA
# =========================
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


# =========================
# PRECEDENCE
# =========================
def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0


# =========================
# RIGHT ASSOCIATIVE
# =========================
def is_right_associative(op):
    return op == '^'


# =========================
# INFIX -> POSTFIX (menggunakan tokenizer baru)
# =========================
def infix_to_postfix(expression):
    stack = Stack()
    output = []
    tokens = tokenize(expression)

    for token in tokens:

        # Angka atau variabel (termasuk multi-karakter seperti F1, F2)
        if is_number(token) or token.isidentifier():
            output.append(token)

        elif token == '(':
            stack.push(token)

        elif token == ')':
            while not stack.is_empty() and stack.top() != '(':
                output.append(stack.pop())
            stack.pop()  # buang '('

        else:  # operator
            while (not stack.is_empty() and
                   stack.top() != '(' and
                   (
                       precedence(stack.top()) > precedence(token)
                       or
                       (
                           precedence(stack.top()) == precedence(token)
                           and not is_right_associative(token)
                       )
                   )):
                output.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        output.append(stack.pop())

    return output


# =========================
# EVALUASI POSTFIX
# =========================
def evaluate_postfix(postfix):
    stack = Stack()

    for token in postfix:

        if is_number(token):
            stack.push(float(token))

        elif token.isidentifier():
            if token not in variables:
                raise KeyError(f"Variabel '{token}' belum didefinisikan.")
            stack.push(float(variables[token]))

        else:  # operator
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Pembagian dengan nol!")
                stack.push(a / b)
            elif token == '^':
                stack.push(a ** b)

    return stack.pop()


# =========================
# BUILD EXPRESSION TREE
# =========================
def build_expression_tree(postfix):
    stack = Stack()
    operators = {'+', '-', '*', '/', '^'}

    for token in postfix:
        node = TreeNode(token)

        if token in operators:
            node.right = stack.pop()
            node.left = stack.pop()

        stack.push(node)

    return stack.pop()


# =========================
# TRAVERSAL
# =========================
def inorder(node):
    if node:
        if node.left:
            print("(", end=" ")
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)
        if node.right:
            print(")", end=" ")


def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


# =========================
# MAIN PROGRAM
# =========================
def jalankan_kalkulator_cli():

    print("=" * 50)
    print("  KALKULATOR EKSPRESI BERANTAI")
    print("=" * 50)
    print()
    print("Perintah yang tersedia:")
    print("  SET <var> <nilai>              — simpan nilai variabel")
    print("  ASSIGN <nama> = <ekspresi>     — hitung & simpan ekspresi")
    print("  EVAL <ekspresi>                — evaluasi ekspresi langsung")
    print("  TREE <ekspresi>                — tampilkan pohon ekspresi")
    print("  VARS                           — lihat semua variabel")
    print("  EXIT                           — keluar")
   

    while True:
        try:
            command = input(">> ").strip()
        except EOFError:
            break

        if not command:
            continue

        if command.upper() == "EXIT":
            print("Keluar dari program.")
            break

        parts = command.split()

        # =====================
        # SET
        # =====================
        if parts[0].upper() == "SET":
            if len(parts) < 3:
                print("[ERROR] Format: SET <var> <nilai>")
                continue
            var = parts[1]
            try:
                value = float(parts[2])
                variables[var] = value
                print(f"  {var} = {value}")
            except ValueError:
                print(f"[ERROR] Nilai '{parts[2]}' bukan angka.")

        # =====================
        # ASSIGN (F1 = ekspresi)
        # =====================
        elif parts[0].upper() == "ASSIGN":
            # Format: ASSIGN <nama> = <ekspresi>
            raw = " ".join(parts[1:])
            if "=" not in raw:
                print("[ERROR] Format: ASSIGN <nama> = <ekspresi>")
                continue

            eq_idx = raw.index("=")
            nama = raw[:eq_idx].strip()
            ekspresi = raw[eq_idx + 1:].strip()

            if not nama.isidentifier():
                print(f"[ERROR] Nama variabel '{nama}' tidak valid.")
                continue

            try:
                postfix = infix_to_postfix(ekspresi)
                hasil = evaluate_postfix(postfix)
                variables[nama] = hasil
                print(f"  Postfix  : {' '.join(postfix)}")
                print(f"  {nama} = {hasil}")
            except KeyError as e:
                print(f"[ERROR] {e}")
            except ZeroDivisionError as e:
                print(f"[ERROR] {e}")
            except Exception as e:
                print(f"[ERROR] {e}")

        # =====================
        # EVAL
        # =====================
        elif parts[0].upper() == "EVAL":
            expression = " ".join(parts[1:])
            try:
                postfix = infix_to_postfix(expression)
                result = evaluate_postfix(postfix)
                print(f"  Postfix : {' '.join(postfix)}")
                print(f"  Hasil   : {result}")
            except KeyError as e:
                print(f"[ERROR] {e}")
            except ZeroDivisionError as e:
                print(f"[ERROR] {e}")
            except Exception as e:
                print(f"[ERROR] {e}")

        # =====================
        # TREE
        # =====================
        elif parts[0].upper() == "TREE":
            expression = " ".join(parts[1:])
            try:
                postfix = infix_to_postfix(expression)
                root = build_expression_tree(postfix)
                print("  Inorder  : ", end="")
                inorder(root)
                print()
                print("  Preorder : ", end="")
                preorder(root)
                print()
                print("  Postorder: ", end="")
                postorder(root)
                print()
            except Exception as e:
                print(f"[ERROR] {e}")

        # =====================
        # VARS
        # =====================
        elif parts[0].upper() == "VARS":
            if not variables:
                print("  (belum ada variabel tersimpan)")
            else:
                print("  Variabel tersimpan:")
                for k, v in variables.items():
                    print(f"    {k} = {v}")

        else:
            print("  Perintah tidak dikenali.")


if __name__ == "__main__":
    jalankan_kalkulator_cli()