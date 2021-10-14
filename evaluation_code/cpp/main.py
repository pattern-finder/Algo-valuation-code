
from evalNbLigneFonction import excecEvalNbLigneFonction
from evalCommentaire import excecEvalCommentaire
from evalRedondance import excecEvalRedondance
from evalVariableName import excecEvalVariableName



if __name__ == '__main__':
    code= "int main() {"\
          "//COUCOU"\
        "std::cout <<\"Hello World!\";"\
        "return 0;"\
    "}"

    payload = {
        "eval variable name":excecEvalVariableName(code),
        "eval redondance": excecEvalRedondance(code),
        "eval nb ligne fonction": excecEvalNbLigneFonction(code),
        "eval commentaire": excecEvalCommentaire(code)
    }

    print(payload)



