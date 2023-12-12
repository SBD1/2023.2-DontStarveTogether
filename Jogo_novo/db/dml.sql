\c dontstarve;
INSERT INTO mapa VALUES (DEFAULT, '1997-08-24', 25, 'p');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 1, 5, 'floresta');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.2, 10, 'pantano');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.4, 20, 'deserto');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.6, -20, 'Tundra');
INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.0, 0, 'Ponte');
INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 1.0, 0, 'Rio');

INSERT INTO posicao VALUES (10,1, 3, NULL, NULL, 11, NULL, 'Nada além de escuridão e resolve não seguir por ali',5,0);
INSERT INTO posicao VALUES (11,1, 3, NULL, NULL, 12, NULL, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',5,0);
INSERT INTO posicao VALUES (12,1, 3, NULL, NULL, 13, NULL, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',5,0);
INSERT INTO posicao VALUES (13,1, 3, NULL, NULL, 14, NULL, 'ao oeste existe uma ponte velha, pode ser que aguente você passar',5,0);
INSERT INTO posicao VALUES (14,1, 5, NULL, NULL, NULL, 15, 'nesta posição existe uma ponte que não está em boas condições, seja rapido!',0,0);
INSERT INTO posicao VALUES (15,1, 5, NULL, NULL, 16, NULL, 'ao leste existe uma ponte velha, pode ser que aguente você passar',2,2);
INSERT INTO posicao VALUES (16,1, 4, NULL, NULL, 17, NULL, 'O gelo toma conta de tudo ao seu redor.',2,2);
INSERT INTO posicao VALUES (17,1, 4, NULL, NULL, 18, NULL, 'O gelo toma conta de tudo ao seu redor.',2,2);
INSERT INTO posicao VALUES (19,1, 3, 10, NULL, NULL, NULL, 'Somente escuridao',20,20);
INSERT INTO posicao VALUES (28,1, 3, 19, NULL, NULL, NULL, 'Somente escuridao',2,1);
INSERT INTO posicao VALUES (37,1, 3, 28, NULL, NULL, NULL, 'Somente escuridao',2,0);
INSERT INTO posicao VALUES (46,1, 3, 37, NULL, NULL, NULL, 'Somente escuridao',1,1);
INSERT INTO posicao VALUES (55,1, 3, 46, NULL, NULL, NULL, 'Somente escuridao',2,0);
INSERT INTO posicao VALUES (64,1, 3, 55, NULL, NULL, NULL, 'Somente escuridao, ao sul existe um ponte que talvez possa passar',2,2);
INSERT INTO posicao VALUES (73,1, 5, 64, NULL, NULL, NULL, 'nesta posição existe uma ponte que não está em boas condições, seja rapido!',0,0);
INSERT INTO posicao VALUES (82,1, 2, 73,NULL, NULL, NULL, 'Somente escuridao mas ao norte existe um ponte velha que atravessa o rio',0,4);
INSERT INTO posicao VALUES (91,1, 2, 82, NULL, NULL, NULL, 'Somente escuridao',1,5);
INSERT INTO posicao VALUES (100,1, 2, 91, NULL, NULL, NULL, 'Somente escuridao',0,3);
INSERT INTO posicao VALUES (109,1, 2, 100, NULL, NULL, NULL, 'Somente escuridao',1,5);
INSERT INTO posicao VALUES (110,1, 2, NULL, NULL, NULL, 109, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,5);
INSERT INTO posicao VALUES (111,1, 2, NULL, NULL, NULL, 110, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,5);
INSERT INTO posicao VALUES (112,1, 2, NULL, NULL, NULL, 111, 'A leste se encontra um ponta velha talvez possa passar por lá',1,5);
INSERT INTO posicao VALUES (113,1, 5, NULL, NULL, NULL, 112, 'nesta posição existe uma ponte que não está em boas condições, seja rapido!',1,5);
INSERT INTO posicao VALUES (114,1, 1, NULL, NULL, NULL, 113, 'A oeste é possivel ver uma ponte velha talvez dê para passar por ali',11,14);
INSERT INTO posicao VALUES (115,1, 1, NULL, NULL, NULL, 114, 'voçê se encontrar em uma floresta fechada',11,14);
INSERT INTO posicao VALUES (116,1, 1, NULL, NULL, NULL, 115, 'voçê se encontrar em uma floresta fechada',11,14);
INSERT INTO posicao VALUES (125,1, 1, 116, NULL, NULL, NULL, 'voçê se encontrar em uma floresta fechada',6,9);
INSERT INTO posicao VALUES (134,1, 1, 125, NULL, NULL, NULL, 'voçê se encontrar em uma floresta fechada',10,14);
INSERT INTO posicao VALUES (135,1, 1, NULL, NULL, NULL, 134, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',10,14);
INSERT INTO posicao VALUES (151,1, 1, 142, NULL, 152, 150, 'Ao sul é possivel encontrar uma montanha intransponível é melhor ir por outra direção ',9,13);


INSERT INTO arma VALUES (DEFAULT, 'Espada de Pedra', 4, 'Espada fraca criada apartir de 15 pedras e 15 madeiras, é essencial para sobreviver a encontro de inimigos');
INSERT INTO arma VALUES (DEFAULT, 'Espada de Ferro', 10, 'Espada Forte craida apartir de 5 ferro, 40 madeiras , é uma espada incrivelmente versatil para batalhas contra inimigos fortes');
INSERT INTO arma VALUES (DEFAULT, 'Espada Suprema', 20, 'Espada Suprema craida apartir de 10 ferro, 80 madeiras , é uma espada incrivelmente versatil para batalhas contra inimigos fortes');


INSERT INTO ferramenta VALUES (DEFAULT, 'Machado Quebrado', 'pegar_madeira(jogador, 1)', 'Esse Machado aparenta está em pessimas condições mas ainda é possivel obter madeira de arvores');
INSERT INTO ferramenta VALUES (DEFAULT, 'Machado Fraco', 'pegar_madeira(jogador, 2)', 'Machado fraco contruido apartir de 15 pedras, 15 madeiras ');
INSERT INTO ferramenta VALUES (DEFAULT, 'Machado de Ferro', 'pegar_madeira(jogador, 3)', 'Machado de Ferro contruido apartir de 3 ferros , 30 madeiras ');


INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta Detreriorada', 'pegar_pedra(jogador, 1)', 'Essa picareta está quase completamente detreriorada mas ainda é posssivel obter pedras de rochas');
INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta de Madeira', 'pegar_pedra(jogador, 2)', 'Picareta de Madeira contruido apartir de 15 pedras, 15 madeiras e ');
INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta de Ferro', 'pegar_pedra(jogador, 3)', 'Picareta de Ferro contruido apartir de 3 ferros , 30 madeiras ');


INSERT INTO ferramenta VALUES (DEFAULT, 'Workbench', 'colocar_na_pos(jogador, 11)', 'workbench é o principal item para criação de novas ferramentas e armas');


INSERT INTO roupa VALUES (DEFAULT, 'Roupa gasta', 1,2,'Roupa gasta mas ajuda levemente na proteção');
INSERT INTO roupa VALUES (DEFAULT, 'Roupa reforçada', 3,4,'Roupa reforçada, ajuda levemente na proteção termica e proteção fisica');
INSERT INTO roupa VALUES (DEFAULT, 'Casaco de guerra', 7,6,'Casco utilizado pela guerrilha, tem grande proteção fisica e termica');
INSERT INTO roupa VALUES (DEFAULT, 'Roupa do Batman', 10,10,'O melhor do melhor, criado pelo cavaleiro das trevas para enfrentar os males do mundo');



INSERT INTO ingrediente VALUES (DEFAULT, 'madeira', 'ingrediente', 'Um pedaço de madeira!');
INSERT INTO ingrediente VALUES (DEFAULT, 'pedra', 'ingrediente', 'Uma unidade de pedra!');


INSERT INTO instancia_item  VALUES (DEFAULT,1, 'a'); 
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'f'); 
INSERT INTO instancia_item  VALUES (DEFAULT,2, 'f'); 
INSERT INTO instancia_item  VALUES (DEFAULT,4, 'r'); 
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'i'); 

INSERT INTO monstro VALUES (DEFAULT,'Sapo',2,'Sapo está irritado com sua presença, ele se prepara pra lhe atacar',10,1,125);
INSERT INTO monstro VALUES (DEFAULT,'Sucuri',4,'Uma jovem sucuri lhe encontra e está preste a lhe atacar',20,2,82);
INSERT INTO monstro VALUES (DEFAULT,'Jacare',8,'Um grande jacare faminto pronto pra atacar qualquer um que encontrar',35,4,115);
INSERT INTO monstro VALUES (DEFAULT,'Lagarto',2,'Um largarto pequeno e extrassado pronto para atacar todos',3,1,64);
INSERT INTO monstro VALUES (DEFAULT,'escorpiao',6,'Um dos monstro ferozes do deserto, sua baixa vida compensa ao seu alto dano',15,6,37);
INSERT INTO monstro VALUES (DEFAULT,'Camelo',4,'Camelo mutante do deserto,após anos de andarilho esse camelo criou uma proteção quase que inquebravel com uma vida enorme',50,9,55);
INSERT INTO monstro VALUES (DEFAULT,'Vermes da areia(BOSS)',15,'é o rei do deserto, sua enorme boca consegue devorar até o maior dos seres',80,15,11);
INSERT INTO monstro VALUES (DEFAULT,'galinha',1,'ele está numa paz não se nega a atacar',10,1,28);


INSERT INTO mochila VALUES (DEFAULT);
INSERT INTO mochila VALUES (DEFAULT);



INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);

INSERT INTO craft VALUES (DEFAULT, 5, 3, NULL, NULL, NULL, NULL, 'false', 'Uma corda nao tao natual!');
