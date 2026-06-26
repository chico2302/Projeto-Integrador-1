# [cite_start]Dashboard de Inteligência de Dados: Análise Epidemiológica do Tabagismo [cite: 4]

[cite_start]Este projeto consiste em um sistema de monitoramento epidemiológico que transforma dados brutos sobre o tabagismo no Brasil em um painel interativo, dinâmico e de fácil leitura[cite: 5]. [cite_start]O foco principal é cruzar a série histórica de óbitos com o impacto de políticas públicas e da carga tributária (IPI) ao longo dos anos[cite: 32, 44].

---

## Sobre a Implementação

[cite_start]O sistema foi estruturado seguindo o padrão arquitetural **MVT (Model-View-Template)** [cite: 11][cite_start], dividindo as tarefas de forma clara entre o processamento analítico e a renderização visual[cite: 6]:

### [cite_start]1. No Servidor (Backend) [cite: 13]
* [cite_start]**Python:** Linguagem base utilizada para construir o motor de processamento, priorizando a legibilidade e o isolamento através de funções puras[cite: 14].
* [cite_start]**Flask:** Micro-framework encarregado de gerenciar as rotas HTTP, capturar os parâmetros dos filtros globais de tempo e tratar exceções[cite: 16].
* [cite_start]**Jinja2:** Motor responsável por realizar a injeção dinâmica de contextos e dados tratados direto no HTML da aplicação[cite: 16].
* [cite_start]**Pandas:** Biblioteca de alta performance utilizada para carregar a base estruturada (`multiplas_causas.csv`), realizar a indexação booleana dupla e executar os agrupamentos (`groupby`) com somatórios numéricos otimizados[cite: 17, 33].
* [cite_start]**Functools (`lru_cache`):** Implementação de cache nativa configurada com tamanho máximo fixado em 1[cite: 18]. [cite_start]Ela mantém o DataFrame tratado diretamente na memória RAM, evitando leituras redundantes de entrada e saída (I/O) no disco rígido após o primeiro carregamento[cite: 19].

### [cite_start]2. Na Interface (Frontend) [cite: 20]
* **HTML5 & CSS3 Nativos:** Estruturação baseada em contêineres semânticos (`main`, `aside`, `section`, `footer`)[cite: 22]. O layout utiliza sistemas de **CSS Grid** (bidimensional) e **Flexbox** (unidimensional) para garantir responsividade total em computadores e celulares, eliminando o uso de frameworks externos pesados[cite: 23, 27]. O painel opera em *Dark Mode* nativo para reduzir a fadiga visual[cite: 21].
* [cite_start]**Chart.js (via CDN):** Biblioteca gráfica baseada na API HTML5 Canvas, utilizada para renderizar múltiplos gráficos simultâneos (linhas temporais, barras verticais e roscas proporcionais) com transições fluidas e eixos automatizados[cite: 28, 29, 30].

---

## Impactos Representados sobre a Temática

[cite_start]O grande diferencial deste dashboard é a sua capacidade de ilustrar e correlacionar visualmente o reflexo direto das ações governamentais na saúde pública[cite: 32]:

* **O Efeito do IPI versus Prevalência:** Através do gráfico analítico avançado de dispersão conectada, o painel cruza o aumento histórico da alíquota do IPI (que evoluiu de 41.25% em 1989 para 78.0% no período recente) diretamente contra a taxa de fumantes ativos, exibindo eixos cartesianos independentes do tempo[cite: 44, 57]. Fica visualmente evidente como o aumento da carga tributária atua na redução da prevalência populacional[cite: 43, 57].
* [cite_start]**Marcos Regulatórios e a Linha de Base:** Ao sobrepor eventos históricos (como leis antifumo, restrições publicitárias e tratados internacionais da OMS) à série temporal de mortes absolutas, o pesquisador consegue analisar os impactos na redução ou estabilização de óbitos por patologias severas, como o *"Câncer de traqueia, brônquios e pulmão"*[cite: 37, 38, 45].
* [cite_start]**Resposta Dinâmica a Períodos Críticos:** A esteira rígida de processamento do sistema permite que, a cada alteração dos seletores temporais "De" ou "Até" pelo usuário, o backend ignore dados nulos ou corrompidos e recalcule instantaneamente o somatório matemático completo (`sum`) sobre o intervalo escolhido[cite: 52, 55, 56]. [cite_start]Isso expõe com clareza quais períodos responderam melhor às ações de controle[cite: 56].

---

## Uso de Inteligência Artificial como Apoio

Em conformidade com as boas práticas de desenvolvimento e diretrizes institucionais, ferramentas de **IA Generativa** foram empregadas como assistentes de suporte técnico (*co-pilot*) durante o ciclo de vida do projeto.

* **Frentes de Atuação:** O uso concentrou-se no apoio à otimização de sintaxes lógicas no Pandas, parametrização de eixos lineares estritos para o Chart.js e suporte no refinamento estético e padronização textual desta documentação técnica.
* **Governança:** Toda a tomada de decisão arquitetural, validação de segurança, higienização de dados e modelagem das regras de negócio epidemiológicas foram conduzidas, revisadas e homologadas integralmente de forma humana pelos desenvolvedores responsáveis.

---

## Visualização Final e Resultados (Perspectiva de Pesquisa)

Como ferramenta de extensão voltada para a comunidade técnica, acadêmica e de saúde pública, o dashboard alcançou resultados expressivos:

* [cite_start]**Democratização dos Dados:** Transformou arquivos e planilhas complexas em gráficos dinâmicos e fluidos, permitindo que qualquer pesquisador filtre e cruze dados históricos em poucos segundos[cite: 30, 53].
* **Apoio a Políticas Públicas:** A velocidade e a autonomia oferecidas pelo painel agilizam o desenho de panoramas epidemiológicos reais, servindo de evidência prática para apoiar decisões na saúde pública e pesquisas científicas.

### Sugestões de Evolução do Projeto
Para futuras atualizações do sistema, identificou-se o valor de implementar:
1. **Filtros Regionais:** Inclusão de recortes por estados ou regiões geográficas para análises epidemiológicas localizadas.
2. **Exportação de Relatórios:** Um módulo para baixar os gráficos gerados e os dados filtrados diretamente em formatos como PNG ou CSV para agilizar o uso em artigos.
