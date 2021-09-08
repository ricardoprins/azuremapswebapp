# Azure Maps Web App + WAQI API

This repository contains code used in a workshop given on August, 2020.

This web app uses Azure Maps SDK to visualize spatial data on an interactive map on a webpage. It also loads pollution data from the World Air Quality Index API, displaying its data on the map.

(_Este aplicativo web usa o Azure Maps SDK para visualizar dados espaciais em um mapa interativo numa página da web. Ele também carrega dados de poluição do World Air Quality Index API, exibindo esses dados no mapa._)

## Requirements / Requisitos

- An [Azure Maps](./APIKEY.md) account + Client ID (_uma conta Azure Maps + Client ID_)
- Python 3.6 or higher (_Python 3.6 ou superior_)
- Requirements are controlled via Poetry (o Poetry está sendo utilizado para controlar as dependências)

To have this webapp working, you'll need an API key from the [World Air Quality Index](https://aqicn.org/data-platform/token/#/). Click on the link, enter your email and name, and after an email confirmation, you'll be able to get the API key from their website.

_Para que este webapp funcione, você precisará de uma chave API do World Air Quality Index. Clique no link acima, insira seu nome e email, e após uma confirmação por email, você poderá obter a chave API pelo site._

## Features / Características

- FastAPI/Python based backend // Backend em FastAPI/Python
- JavaScript for interaction with Azure Maps // JavaScript para interação com Azure Maps
