# Job Insights
### Autor: Matheus Eduardo de Sousa Azevedo

Este projeto foi desenvolvido por mim e faz parte do acervo de atividades executadas na escola de programação Trybe. A formação ao longo de 1 ano em Desenvolvimento Web desta instituição  conta com mais de 1.500 horas de aulas e aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias ágeis e habilidades comportamentais. Tudo voltado totalmente para o mercado de trabalho com intuito de entregar um profissional adequado para a realidade atual. 

# Sobre o projeto

Job Insights é um projeto que consiste em implementar análises de dados a partir de um conjunto de dados sobre empregos, disponibilizado pelo Kaggle e extraído do site Glassdoor. As implementações serão incorporadas a um aplicativo Web desenvolvido com Flask, um framework web muito popular na comunidade Python. Além disso, será necessário escrever testes para a implementação de uma análise de dados e como bônus, escrever uma rota e view para um recurso novo usando Flask. Serão trabalhadas habilidades como utilização do terminal interativo do Python, estruturas condicionais e de repetição, funções built-in do Python, tratamento de exceções, manipulação de arquivos, escrita de funções e testes com Pytest, além de criar e importar módulos em outros códigos.

# O que foi desenvolvido

1.  Função read - Implementada em src/insights/jobs.py, responsável por abrir um arquivo CSV e retornar seus dados no formato de uma lista de dicionários.
    
2.  Função get_unique_job_types - Implementada em src/insights/jobs.py, responsável por identificar os tipos de empregos existentes nos dados fornecidos.
    
3.  Função get_unique_industries - Implementada em src/insights/industries.py, responsável por identificar as indústrias existentes nos dados fornecidos.
    
4.  Função get_max_salary - Implementada em src/insights/salaries.py, responsável por encontrar o maior valor de todas as faixas salariais para cada emprego exibido nos dados fornecidos.
    
5.  Função get_min_salary - Implementada em src/insights/salaries.py, responsável por encontrar o menor valor de todas as faixas salariais para cada emprego exibido nos dados fornecidos.
    
6.  Função filter_by_job_type - Implementada em src/insights/jobs.py, responsável por filtrar empregos por tipo de emprego.
    
7.  Função filter_by_industry - Implementada em src/insights/industries.py, responsável por filtrar empregos por indústria.
    
8.  Função matches_salary_range - Implementada em src/insights/salaries.py, responsável por conferir que o salário procurado está dentro da faixa salarial daquele emprego. Também confere se a faixa salarial faz sentido.
