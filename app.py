from fastapi import FastAPI
from tradutor import traduzir


app = FastAPI()


@app.post("/tradutor")
def _traduzir(text:str, linguagem_text:str="en", linguage_final:str="pt"):
    """ esse metodo serve para traduxir textos """

    traducao = traduzir(text, linguagem_text, linguage_final)
    
    if traducao:
        data = {
            "message": "Texto Traduzido com sucesso",
            "sucess": True,
            "data": {
                "original": text,
                "traduzido": traducao
            }
        }
        
        return data
    else:
        return {
            "erro": "Não foi possivel traduzir o texto",
            "sucess": False
        }




