# Azure Maps Web App

This web app uses Azure Maps SDK to visualize spatial data on an interactive map on a webpage.
(_Este aplicativo web usa o Azure Maps SDK para visualizar dados espaciais em um mapa interativo numa página da web_)

## Requirements

- An [Azure Maps](./APIKEY.md) account + Client ID (_uma conta Azure Maps + Client ID_)
- Python 3.6 or higher (_Python 3.6 ou superior_)
- For the Python library requirements, please check the _requirements.txt_ file (_Consulte o arquivo requirements.txt para ver as bibliotecas necessárias no Python_)

## Stack

This web app uses [FastAPI](https://fastapi.tiangolo.com/) - a modern, fast web framework for building APIs with Python. For templating, [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is being used - it is a simple web app, so this implementation doesn't contain any sophisticated front end Javascript framework.

_Este web app usa FastAPI - um framework web moderno e veloz para a construção de APIs com Python. Para os templates, foi utilizado Jinja - como se trata de um web app simples, esta implementação não conta com nenhum framework em Javascript sofisticado para o front end._

The web app is hosted on [Azure](https://portal.azure.com/).

_Este web app está hospedado no Azure._

To complete all steps in this tutorial, you'll need an API key from the [Air Quality Open Data Platform](https://aqicn.org/data-platform/token/#/). Click on the link, enter your email and name, and after an email confirmation, you'll be able to get the API key from their website.

_Para completar todos os passos desse tutorial, você precisará de uma chave API do Air Quality Open Data Platform. Clique no link, insira seu nome e email, e após uma confirmação por email, você poderá obter a chave API pelo site._
