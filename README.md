# Dashboard de Inteligência de Dados: Análise Epidemiológica do Tabagismo

Este projeto consiste em um sistema de monitoramento epidemiológico que transforma dados brutos sobre o tabagismo no Brasil em um painel interativo, dinâmico e de fácil leitura. O foco principal é cruzar a série histórica de óbitos com o impacto de políticas públicas e da carga tributária (IPI) ao longo dos anos.

## Demonstração

📹 **Vídeo de apresentação do dashboard:**

https://drive.google.com/file/d/1tmFymtmTpfKuZu9WmCFNVQQ0t4kjSnaI/view?usp=sharing

## Sobre a Implementação

O sistema foi estruturado seguindo o padrão arquitetural **MVT (Model-View-Template)**, dividindo as tarefas de forma clara entre o processamento analítico no backend e a renderização reativa no frontend:

### 1. No Servidor (Backend)
* **Python:** Linguagem base utilizada para construir o motor de processamento, priorizando a legibilidade e o isolamento através de funções puras.
* **Flask:** Micro-framework encarregado de gerenciar as rotas HTTP, capturar os parâmetros dos filtros globais de tempo (ano mínimo e máximo) e tratar exceções.
* **Jinja2:** Motor do Flask responsável por realizar a injeção dinâmica de contextos e dados tratados direto no HTML da aplicação.
* **Pandas:** Biblioteca de alta performance utilizada para carregar a base estruturada local (`multiplas_causas.csv`), realizar a indexação booleana dupla nas séries temporais e executar os agrupamentos (`groupby`) com somatórios numéricos otimizados.
* **Functools (`lru_cache`):** Implementação de cache nativa configurada com tamanho máximo fixado em 1. Ela mantém o DataFrame tratado diretamente na memória RAM, evitando leituras redundantes de entrada e saída (I/O) no disco rígido após o primeiro carregamento.

### 2. Na Interface (Frontend)
* **HTML5 & CSS3 Nativos:** Estruturação baseada em contêineres semânticos como `main`, `aside`, `section` e `footer`. O layout utiliza sistemas de **CSS Grid** (bidimensional) e **Flexbox** (unidimensional) para garantir responsividade total em computadores e celulares, eliminando o uso de frameworks externos pesados. O painel opera em *Dark Mode* nativo para reduzir a fadiga visual.
* **Chart.js (via CDN):** Biblioteca gráfica baseada na API HTML5 Canvas, utilizada para renderizar múltiplos gráficos simultâneos (linhas temporais, barras verticais e roscas proporcionais) com transições fluidas e eixos automatizados.



## Impactos Representados sobre a Temática

O grande diferencial deste dashboard é a sua capacidade de ilustrar e correlacionar visualmente o reflexo direto das ações governamentais na saúde pública:

* **O Efeito do IPI versus Prevalência:** Através do gráfico analítico avançado de dispersão conectada, o painel cruza o aumento histórico da alíquota do IPI (que evoluiu de 41.25% em 1989 para 78.0% no período recente) diretamente contra a taxa de fumantes ativos, exibindo eixos cartesianos inteiramente lineares e independentes do tempo. Fica visualmente evidente como o aumento da carga tributária atua na redução da prevalência populacional.
* **Marcos Regulatórios e a Linha de Base:** Ao sobrepor eventos históricos (como leis antifumo, restrições publicitárias e tratados internacionais da OMS) à série temporal de mortes absolutas, o pesquisador consegue analisar os impactos na redução ou estabilização de óbitos por patologias severas, como o *"Câncer de traqueia, brônquios e pulmão"*.
* **Resposta Dinâmica a Períodos Críticos:** A esteira rígida de processamento do sistema permite que, a cada alteração dos seletores temporais "De" ou "Até" pelo usuário, o backend valide o intervalo, ignore dados nulos ou corrompidos e recalcule instantaneamente o somatório matemático completo (`sum`) sobre o período escolhido. Isso expõe com clareza quais intervalos responderam melhor às ações de controle.



## Uso de Inteligência Artificial como Apoio

Em conformidade com as boas práticas de desenvolvimento e diretrizes institucionais, ferramentas de **IA Generativa** foram empregadas como assistentes de suporte técnico (*co-pilot*) durante o ciclo de vida do projeto.

* **Frentes de Atuação:** O uso concentrou-se no apoio à otimização de sintaxes lógicas no Pandas, parametrização de eixos lineares estritos para o Chart.js e suporte no refinamento estético e padronização textual desta documentação técnica.
* **Governança:** Toda a tomada de decisão arquitetural, validação de segurança, higienização de dados e modelagem das regras de negócio epidemiológicas foram conduzidas, revisadas e homologadas integralmente de forma humana pelos desenvolvedores responsáveis.



## Visualização Final e Resultados (Perspectiva de Pesquisa)

Como ferramenta de extensão voltada para a comunidade técnica, acadêmica e de saúde pública, o dashboard alcançou resultados expressivos:

* **Democratização dos Dados:** Transformou arquivos e planilhas complexas em gráficos dinâmicos e fluidos, permitindo que qualquer pesquisador filtre e cruze dados históricos em poucos segundos.
* **Apoio a Políticas Públicas:** A velocidade e a autonomia oferecidas pelo painel agilizam o desenho de panoramas epidemiológicos reais, servindo de evidência prática para apoiar decisões na saúde pública e pesquisas científicas.

## Integrantes

* Artur Feitoza de Lima Rodrigues || RA: 22401202
* Francisco Barbosa Ribeiro || RA: 22408832
