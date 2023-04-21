import random

class Lotteri: 

        def __init__(self):
            self.list_vinster = [
                "Solstol",
                "Svettig strumpa",
                "Gethorn",
                "Leksaks Polisbil",
                "Skateboard",
                "Hårspänne",
                "Linjal",
                "2 l Tvål",
                "Mössa",
                "En biltvätt på OK/Q8",
                "En Volvo",
                "En röd Ferari",
                "2 Kg gädda",
                "Servetter",
                "Penskrin",
                "Ficklampa",
                "Munkhuve jacka",
                "Snowboard",
                "Skoter RMk 800",
                "Motorcyckel",
                "Sockerkaka",
            ]



        def get_vinst(self):
            slumptal = random.randint(0, 19)
            return self.list_vinster[3]

