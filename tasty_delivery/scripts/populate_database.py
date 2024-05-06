from datetime import datetime
from uuid import uuid4

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

# from security.base import get_password_hash
from adapter.database.db import get_db


def populate():
    try:
        session = next(get_db())

        product_1_id = uuid4()
        product_2_id = uuid4()
        product_3_id = uuid4()
        product_4_id = uuid4()
        product_5_id = uuid4()
        product_6_id = uuid4()
        product_7_id = uuid4()
        product_8_id = uuid4()

        session.execute(
            text(
                f'''
                        INSERT INTO products (id, name, description, price, is_active, is_deleted, created_at, updated_at)
                        VALUES 
                            ('{product_1_id}', 'Whopper', 'Pão com gergelim, maionese, alface, tomate, cebola, ketchup, picles, queijo derretido e um suculento hambúrguer de pura carne bovina. Todos esses ingredientes são cuidadosamente armazenados e preparados, para você se deliciar com um sanduíche fresquinho e de alta qualidade' , 21.90,true, false, '{datetime.utcnow()}', null),
                            ('{product_2_id}', 'Big Mac', 'Dois hambúrgueres (100% carne bovina), alface americana, queijo sabor cheddar, molho especial, cebola, picles e pão com gergelim.', 19.90,true, false, '{datetime.utcnow()}', null),
                            ('{product_3_id}', 'Cheddar', 'Um hambúrguer (100% carne bovina), molho lácteo cremoso sabor cheddar, cebola ao molho shoyu e pão escuro com gergelim.', 17.90,true, false, '{datetime.utcnow()}', null),
                            ('{product_4_id}', 'McFritas Média', 'A batata frita mais famosa do mundo. Deliciosas batatas selecionadas, fritas, crocantes por fora, macias por dentro, douradas, irresistíveis, saborosas, famosas, e todos os outros adjetivos positivos que voê quiser dar.', 8.9, true, false, '{datetime.utcnow()}', null),
                            ('{product_5_id}', 'Coca-Cola', 'Refrescante e geladinha. Uma bebida assim refresca a vida. Você pode escolher entre Coca-Cola, Coca-Cola Zero, Sprite sem Açúcar, Fanta Guaraná e Fanta Laranja.', 7.90,true, false, '{datetime.utcnow()}', null),
                            ('{product_6_id}', 'Guaraná', 'Refrescante e geladinha. Uma bebida assim refresca a vida. Você pode escolher entre Coca-Cola, Coca-Cola Zero, Sprite sem Açúcar, Fanta Guaraná e Fanta Laranja', 7.90,true, false, '{datetime.utcnow()}', null),
                            ('{product_7_id}', 'Casquinha', 'A sobremesa que o Brasil todo adora. Uma casquinha supercrocante, com bebida láctea mista (sabor baunilha e chocolate) que vai bem a qualquer hora.', 5.50, true, false, '{datetime.utcnow()}', null),
                            ('{product_8_id}', 'Torta de maçã', 'Boa demais. Parece a receita lá de casa. Massa quentinha e crocante envolvendo deliciosos recheios de banana ou maçã com gostinho de doce caseiro', 10.9, true, false, '{datetime.utcnow()}', null)
                        '''
            )
        )
        session.commit()

        session.close()

    except IntegrityError:
        pass
