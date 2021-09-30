{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "# Exemplo: Lista de Produtos em uma Fábrica"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "from barcode import EAN13\r\n",
    "from barcode.writer import ImageWriter #gera imagem em png\r\n",
    "\r\n",
    "codigo_barra = EAN13(\"123123123123\", writer=ImageWriter())\r\n",
    "codigo_barra.save(\"codigo_barra\")"
   ],
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'codigo_barra.png'"
      ]
     },
     "metadata": {},
     "execution_count": 4
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "codigos_produtos = {\r\n",
    "    \"Feijao\": \"551746511111\",\r\n",
    "    \"Arroz\": \"665789011111\",\r\n",
    "    \"Macarrao\": \"665887111111\",\r\n",
    "    \"Azeite\": \"998556211111\"}\r\n",
    "\r\n",
    "for produto in codigos_produtos:\r\n",
    "    codigo = codigos_produtos[produto]\r\n",
    "    codigo_barra = EAN13(codigo, writer=ImageWriter())\r\n",
    "    codigo_barra.save(f\"codigo_barra_{produto}\")"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "markdown",
   "source": [
    "### Exemplo: Lista de Produtos de um E-commerce"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "import qrcode\r\n",
    "\r\n",
    "imagem_qrcode = qrcode.make(\"https://excelparaestagio.klickpages.com.br/inscricao-basico-cta-att?origemurl=hashtag_yt_org_minibasico2_videoqrcode\")\r\n",
    "imagem_qrcode.save(\"qrcode_python.png\")"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "source": [
    "links_produtos = {\r\n",
    "    \"Adição e Subtração\": \"https://www.youtube.com/watch?v=gyrUUMeS3-g&t=8s\",\r\n",
    "    \"Comparação de frações\": \"https://www.youtube.com/watch?v=Pd6sv6EV4xc&t=5s\",\r\n",
    "    \"Potenciação\": \"https://www.youtube.com/watch?v=87P7HmWzW2g&t=25s\"    \r\n",
    "}\r\n",
    "\r\n",
    "for produto in links_produtos:\r\n",
    "    link = links_produtos[produto]\r\n",
    "    imagem_qrcode = qrcode.make(link)\r\n",
    "    imagem_qrcode.save(f\"qrcode_{produto}.png\")\r\n",
    "    "
   ],
   "outputs": [],
   "metadata": {}
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9.1 64-bit"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  },
  "interpreter": {
   "hash": "63fd5069d213b44bf678585dea6b12cceca9941eaf7f819626cde1f2670de90d"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}