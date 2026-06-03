# 🌿 GS 2026.1 – Building Data Driven Applications

**Disciplina:** Building Data Driven Application  
**Professor(a):** Patrícia Angelini  
**Instituição:** FIAP  
**Semestre:** 2026.1  

---

## 📋 Descrição

Programa em Python que coleta, armazena e analisa dados de **eventos ambientais** (desmatamento, queimadas, etc.), gerando um relatório completo com estatísticas e identificação do evento mais crítico.

---

## ⚙️ Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa é necessária (apenas recursos nativos do Python)

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/<SEU_USUARIO>/<NOME_DO_REPO>.git
   cd <NOME_DO_REPO>
   ```

2. Execute o script:
   ```bash
   python gs_datadrivenapp.py
   ```

---

## 📥 Entradas Esperadas

| Campo         | Tipo    | Restrição                  |
|---------------|---------|----------------------------|
| Tipo de evento | texto  | não pode estar vazio       |
| País          | texto   | não pode estar vazio       |
| Região        | texto   | não pode estar vazio       |
| Cidade        | texto   | não pode estar vazio       |
| Área (km²)    | float   | deve ser **> 0**           |
| Intensidade   | inteiro | deve estar entre **1 e 10**|
| Ocorrências   | inteiro | deve ser **≥ 1**           |

---

## 📤 Exemplo de Uso

```
Insira a quantidade de eventos: 2

--- Evento 1 ---
Tipo: desmatamento
País: Brasil
Região: Norte
Cidade: Manaus
Área (km²): 100
Intensidade (1 a 10): 8
Ocorrências: 20

--- Evento 2 ---
Tipo: queimadas
País: Brasil
Região: Centro-Oeste
Cidade: Cuiabá
Área (km²): 50
Intensidade (1 a 10): 6
Ocorrências: 10
```

**Saída gerada:**

```
========================================
        RELATÓRIO DE ANÁLISE
========================================
Total de eventos registrados: 2
----------------------------------------
Resumo Geral
----------------------------------------
Área total afetada: 150 km²
Média de intensidade: 7.0
----------------------------------------
Análises
----------------------------------------
Região com maior número de ocorrências: Norte
Quantidade de eventos acima da média de intensidade: 1
Densidade média de ocorrências: 0.20 ocorrências/km²
----------------------------------------
Evento Mais Crítico
----------------------------------------
Tipo: desmatamento
Local: Manaus, Norte, Brasil
Intensidade: 8
Área afetada: 100 km²
========================================
Total de desastres registrados: 2
```

---

## 🧱 Estrutura do Projeto

```
📂 repositório
├── gs_datadrivenapp.py   # Código-fonte principal
└── README.md             # Este arquivo
```

---

## 📌 Regras Técnicas Aplicadas

- Apenas estruturas nativas: `if/else`, `for`, `while`, `list`
- Uso de `max()` e `index()` para localizar extremos
- Validação de entradas com laços `while`
- Sem uso de funções definidas pelo usuário (`def`)
- Sem uso de bibliotecas externas (ex: `pandas`)

---

## 📝 Licença

Projeto acadêmico – FIAP 2026.1
