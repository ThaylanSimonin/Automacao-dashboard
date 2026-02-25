==================================
Documentação do Modelo: [Nome]
==================================

.. meta::
   :description: Detalhes técnicos e métricas de performance do modelo de propensão.
   :keywords: machine learning, xgboost, classificação

Esta seção descreve a arquitetura, o processo de treinamento e as métricas de avaliação do modelo de **[Exemplo: Propensão de Churn]**.

Visão Geral do Modelo
---------------------

O modelo utiliza o algoritmo **XGBoost** (Extreme Gradient Boosting) para prever a probabilidade de um cliente cancelar o serviço nos próximos 30 dias.

* **Tipo de Problema:** Classificação Binária.
* **Versão atual:** ``v2.1.0-stable``
* **Framework:** ``scikit-learn``, ``xgboost``

Arquitetura e Hiperparâmetros
-----------------------------

O modelo foi otimizado via *Bayesian Search*. Abaixo, os principais hiperparâmetros configurados:

.. list-table:: Hiperparâmetros Finais
   :widths: 30 70
   :header-rows: 1

   * - Parâmetro
     - Valor
   * - ``learning_rate``
     - 0.05
   * - ``max_depth``
     - 6
   * - ``n_estimators``
     - 500
   * - ``subsample``
     - 0.8

Pipeline de Dados
-----------------

O processamento dos dados segue o fluxo abaixo antes da inferência:

1. **Limpeza:** Tratamento de valores nulos via imputação por mediana.
2. **Encoding:** Aplicação de *Target Encoding* para variáveis categóricas de alta cardinalidade.
3. **Escalonamento:** *StandardScaler* aplicado às variáveis numéricas.

Métricas de Performance
