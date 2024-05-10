# flood-rs

Essa ferramenta tem por objetivo predizer o nível de água de rios do RS. Considerando a gravidade das inundações que vem acometendo as cidades do Rio Grande Sul surgiu a ideia, do nosso grupo, de criar um modelo que acompanhasse as tendências de aumento ou queda do nível dos Rios. Com esses resultados por hora será possível estabelecer alertas com antecedência, permitindo a evacuação de pessoas em áreas de risco. Atualmente, o sistema está focado no rio São Gonçalo - Pelotas, que tem registrado um aumento em seu nível desde o dia 04/05/2024. No entanto, o sistema poderá ser adaptado para monitorar qualquer curso d'água que possuam relatórios diários disponíveis. Além disso, para a otimização do modelo está sendo utilizado a orientação do vento que é o principal fator de risco para nós aqui em Pelotas. Ventos que possuem sentido Sul ou Sudeste são os mais preocupantes, pois eles acabam empurrando a água para a cidade dificultando o escoamento para o oceano Atlântico. A obtenção dos dados referente a direção do vento estão sendo obtidas através do portal windy, utilizando um modelo com resolução de 9km

Próximos passos: 
- Automatizar a obtenção dos dados tanto o nível histórico quanto da direção do vento 
- Testar outros regressores como precipitação e talvez altitude (desafio maior)

Até o momento temos esse protótipo que foi cadastrado no programa de *Iniciativas internacionais vão integrar mapeamento de soluções para enfrentamento de desastres naturais*.

best_model.ipynb - melhor modelo obtido

main.py - aplicação online com o modelo serializado 