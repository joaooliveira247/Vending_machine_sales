# 🏪 Vending Machine Sales

## ℹ️ About:

This project was doing with purpose be a portfolio.

So it didn't have a wrote challenge, I had to use my imagination.

1º Do all data cleaning:
  - Remove null fields.
  - Infer types of columns.

2º Put it inside a class named Pipeline.
  - Provide methods to get different types of analytics and plot graphics.

## ⚠️ you can see all data rendered:

  - [Most Sell](./vending_machine_sales/render/most_sell.ipynb)

## 💻 Requirements:

### `Python >= 3.10`

### `Poetry`

This project uses a packaging and dependency management called [`poetry`](https://python-poetry.org/).

- Installation:

  `(osx / linux / bash on windows) install instructions`

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

  `windows(Powershell) install instructions`

  ```bash
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```

- Running

  ```bash
  poetry install
  ```

  - To install all dependencies of the project.

  ####

  ```bash
  poetry shell
  ```

  - To give a shell with environment activate.

This project uses a dataset's from [Kaggle](https://www.kaggle.com/).

<details>
  <summary style="font-size: 20px;"> Vending Machine Sales DataSet Informations</summary>

<br>

- [Vending Machine Sales](https://www.kaggle.com/datasets/awesomeasingh/vending-machine-sales)


|Status|Represents if the machine data is successfully processed|
|:---:|:---:|
|Device ID|Unique electronic identifier ( also called as ePort) for the vending machine. A machine is allocated a unique ePrt * device|
|Location|Indicates location of the vending machine|
|Machine|User-friendly machine name|
|Product|Product vended from the machine|
|Category| Carbonated / Food / Non-carbonated / Water|
|Transaction| Unique identifier for every transaction|
|TransDate | The Date & time of transaction|
|Type | Type of transaction ( Cash / Credit )|
|RCoil | Coil # used to vend the product|
|RPrice | Price of the Product|
|RQty | Quantity sold. This is usually one but machines can be configured to sell more items in a single transaction|
|MCoil | Mapped coil # used to vend the product ( from toucan )|
|MPrice | Mapped price of the Product|
|MQty | Mapped quantity sold. This is usually one but machines can be configured to sell more items in a single transaction|
|LineTotal | Total sale per transaction|
|TransTotal | Represents total of all transactions that will show up on the Credit Card. A user could vend a drink for $3 and a snack for $1.5 making a total of $4.50|
|Prcd Date | Date when the transaction was processed by SeedLive ( an entity that is used to aggregate all transactions electronically )|

</details>