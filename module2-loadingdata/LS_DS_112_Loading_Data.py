{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "LS_DS_112_Loading_Data.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-c0vWATuQ_Dn",
        "colab_type": "text"
      },
      "source": [
        "# Lambda School Data Science - Loading, Cleaning and Visualizing Data\n",
        "\n",
        "Objectives for today:\n",
        "- Load data from multiple sources into a Python notebook \n",
        " - From a URL (github or otherwise)\n",
        " - CSV upload method\n",
        " - !wget method\n",
        "- \"Clean\" a dataset using common Python libraries\n",
        " - Removing NaN values \"Data Imputation\"\n",
        "- Create basic plots appropriate for different data types\n",
        " - Scatter Plot\n",
        " - Histogram\n",
        " - Density Plot\n",
        " - Pairplot (if we have time)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "grUNOP8RwWWt",
        "colab_type": "text"
      },
      "source": [
        "# Part 1 - Loading Data\n",
        "\n",
        "Data comes in many shapes and sizes - we'll start by loading tabular data, usually in csv format.\n",
        "\n",
        "Data set sources:\n",
        "\n",
        "- https://archive.ics.uci.edu/ml/datasets.html\n",
        "- https://github.com/awesomedata/awesome-public-datasets\n",
        "- https://registry.opendata.aws/ (beyond scope for now, but good to be aware of)\n",
        "\n",
        "Let's start with an example - [data about flags](https://archive.ics.uci.edu/ml/datasets/Flags)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wxxBTeHUYs5a",
        "colab_type": "text"
      },
      "source": [
        "## Lecture example - flag data"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nc-iamjyRWwe",
        "colab_type": "code",
        "outputId": "9b4cfab2-910a-4a67-eecf-9b1521f7fb92",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 3400
        }
      },
      "source": [
        "# Step 1 - find the actual file to download\n",
        "\n",
        "# From navigating the page, clicking \"Data Folder\"\n",
        "flag_data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data'\n",
        "\n",
        "# You can \"shell out\" in a notebook for more powerful tools\n",
        "# https://jakevdp.github.io/PythonDataScienceHandbook/01.05-ipython-and-shell-commands.html\n",
        "\n",
        "# Funny extension, but on inspection looks like a csv\n",
        "!curl https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data\n",
        "\n",
        "# Extensions are just a norm! You have to inspect to be sure what something is"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Afghanistan,5,1,648,16,10,2,0,3,5,1,1,0,1,1,1,0,green,0,0,0,0,1,0,0,1,0,0,black,green\n",
            "Albania,3,1,29,3,6,6,0,0,3,1,0,0,1,0,1,0,red,0,0,0,0,1,0,0,0,1,0,red,red\n",
            "Algeria,4,1,2388,20,8,2,2,0,3,1,1,0,0,1,0,0,green,0,0,0,0,1,1,0,0,0,0,green,white\n",
            "American-Samoa,6,3,0,0,1,1,0,0,5,1,0,1,1,1,0,1,blue,0,0,0,0,0,0,1,1,1,0,blue,red\n",
            "Andorra,3,1,0,0,6,0,3,0,3,1,0,1,1,0,0,0,gold,0,0,0,0,0,0,0,0,0,0,blue,red\n",
            "Angola,4,2,1247,7,10,5,0,2,3,1,0,0,1,0,1,0,red,0,0,0,0,1,0,0,1,0,0,red,black\n",
            "Anguilla,1,4,0,0,1,1,0,1,3,0,0,1,0,1,0,1,white,0,0,0,0,0,0,0,0,1,0,white,blue\n",
            "Antigua-Barbuda,1,4,0,0,1,1,0,1,5,1,0,1,1,1,1,0,red,0,0,0,0,1,0,1,0,0,0,black,red\n",
            "Argentina,2,3,2777,28,2,0,0,3,2,0,0,1,0,1,0,0,blue,0,0,0,0,0,0,0,0,0,0,blue,blue\n",
            "Argentine,2,3,2777,28,2,0,0,3,3,0,0,1,1,1,0,0,blue,0,0,0,0,1,0,0,0,0,0,blue,blue\n",
            "Australia,6,2,7690,15,1,1,0,0,3,1,0,1,0,1,0,0,blue,0,1,1,1,6,0,0,0,0,0,white,blue\n",
            "Austria,3,1,84,8,4,0,0,3,2,1,0,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,red\n",
            "Bahamas,1,4,19,0,1,1,0,3,3,0,0,1,1,0,1,0,blue,0,0,0,0,0,0,1,0,0,0,blue,blue\n",
            "Bahrain,5,1,1,0,8,2,0,0,2,1,0,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,white,red\n",
            "Bangladesh,5,1,143,90,6,2,0,0,2,1,1,0,0,0,0,0,green,1,0,0,0,0,0,0,0,0,0,green,green\n",
            "Barbados,1,4,0,0,1,1,3,0,3,0,0,1,1,0,1,0,blue,0,0,0,0,0,0,0,1,0,0,blue,blue\n",
            "Belgium,3,1,31,10,6,0,3,0,3,1,0,0,1,0,1,0,gold,0,0,0,0,0,0,0,0,0,0,black,red\n",
            "Belize,1,4,23,0,1,1,0,2,8,1,1,1,1,1,1,1,blue,1,0,0,0,0,0,0,1,1,1,red,red\n",
            "Benin,4,1,113,3,3,5,0,0,2,1,1,0,0,0,0,0,green,0,0,0,0,1,0,0,0,0,0,green,green\n",
            "Bermuda,1,4,0,0,1,1,0,0,6,1,1,1,1,1,1,0,red,1,1,1,1,0,0,0,1,1,0,white,red\n",
            "Bhutan,5,1,47,1,10,3,0,0,4,1,0,0,0,1,1,1,orange,4,0,0,0,0,0,0,0,1,0,orange,red\n",
            "Bolivia,2,3,1099,6,2,0,0,3,3,1,1,0,1,0,0,0,red,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Botswana,4,2,600,1,10,5,0,5,3,0,0,1,0,1,1,0,blue,0,0,0,0,0,0,0,0,0,0,blue,blue\n",
            "Brazil,2,3,8512,119,6,0,0,0,4,0,1,1,1,1,0,0,green,1,0,0,0,22,0,0,0,0,1,green,green\n",
            "British-Virgin-Isles,1,4,0,0,1,1,0,0,6,1,1,1,1,1,0,1,blue,0,1,1,1,0,0,0,1,1,1,white,blue\n",
            "Brunei,5,1,6,0,10,2,0,0,4,1,0,0,1,1,1,0,gold,0,0,0,0,0,0,1,1,1,1,white,gold\n",
            "Bulgaria,3,1,111,9,5,6,0,3,5,1,1,1,1,1,0,0,red,0,0,0,0,1,0,0,1,1,0,white,red\n",
            "Burkina,4,4,274,7,3,5,0,2,3,1,1,0,1,0,0,0,red,0,0,0,0,1,0,0,0,0,0,red,green\n",
            "Burma,5,1,678,35,10,3,0,0,3,1,0,1,0,1,0,0,red,0,0,0,1,14,0,0,1,1,0,blue,red\n",
            "Burundi,4,2,28,4,10,5,0,0,3,1,1,0,0,1,0,0,red,1,0,1,0,3,0,0,0,0,0,white,white\n",
            "Cameroon,4,1,474,8,3,1,3,0,3,1,1,0,1,0,0,0,gold,0,0,0,0,1,0,0,0,0,0,green,gold\n",
            "Canada,1,4,9976,24,1,1,2,0,2,1,0,0,0,1,0,0,red,0,0,0,0,0,0,0,0,1,0,red,red\n",
            "Cape-Verde-Islands,4,4,4,0,6,0,1,2,5,1,1,0,1,0,1,1,gold,0,0,0,0,1,0,0,0,1,0,red,green\n",
            "Cayman-Islands,1,4,0,0,1,1,0,0,6,1,1,1,1,1,0,1,blue,1,1,1,1,4,0,0,1,1,1,white,blue\n",
            "Central-African-Republic,4,1,623,2,10,5,1,0,5,1,1,1,1,1,0,0,gold,0,0,0,0,1,0,0,0,0,0,blue,gold\n",
            "Chad,4,1,1284,4,3,5,3,0,3,1,0,1,1,0,0,0,gold,0,0,0,0,0,0,0,0,0,0,blue,red\n",
            "Chile,2,3,757,11,2,0,0,2,3,1,0,1,0,1,0,0,red,0,0,0,1,1,0,0,0,0,0,blue,red\n",
            "China,5,1,9561,1008,7,6,0,0,2,1,0,0,1,0,0,0,red,0,0,0,0,5,0,0,0,0,0,red,red\n",
            "Colombia,2,4,1139,28,2,0,0,3,3,1,0,1,1,0,0,0,gold,0,0,0,0,0,0,0,0,0,0,gold,red\n",
            "Comorro-Islands,4,2,2,0,3,2,0,0,2,0,1,0,0,1,0,0,green,0,0,0,0,4,1,0,0,0,0,green,green\n",
            "Congo,4,2,342,2,10,5,0,0,3,1,1,0,1,0,0,0,red,0,0,0,0,1,0,0,1,1,0,red,red\n",
            "Cook-Islands,6,3,0,0,1,1,0,0,4,1,0,1,0,1,0,0,blue,1,1,1,1,15,0,0,0,0,0,white,blue\n",
            "Costa-Rica,1,4,51,2,2,0,0,5,3,1,0,1,0,1,0,0,blue,0,0,0,0,0,0,0,0,0,0,blue,blue\n",
            "Cuba,1,4,115,10,2,6,0,5,3,1,0,1,0,1,0,0,blue,0,0,0,0,1,0,1,0,0,0,blue,blue\n",
            "Cyprus,3,1,9,1,6,1,0,0,3,0,1,0,1,1,0,0,white,0,0,0,0,0,0,0,1,1,0,white,white\n",
            "Czechoslovakia,3,1,128,15,5,6,0,0,3,1,0,1,0,1,0,0,white,0,0,0,0,0,0,1,0,0,0,white,red\n",
            "Denmark,3,1,43,5,6,1,0,0,2,1,0,0,0,1,0,0,red,0,1,0,0,0,0,0,0,0,0,red,red\n",
            "Djibouti,4,1,22,0,3,2,0,0,4,1,1,1,0,1,0,0,blue,0,0,0,0,1,0,1,0,0,0,white,green\n",
            "Dominica,1,4,0,0,1,1,0,0,6,1,1,1,1,1,1,0,green,1,0,0,0,10,0,0,0,1,0,green,green\n",
            "Dominican-Republic,1,4,49,6,2,0,0,0,3,1,0,1,0,1,0,0,blue,0,1,0,0,0,0,0,0,0,0,blue,blue\n",
            "Ecuador,2,3,284,8,2,0,0,3,3,1,0,1,1,0,0,0,gold,0,0,0,0,0,0,0,0,0,0,gold,red\n",
            "Egypt,4,1,1001,47,8,2,0,3,4,1,0,0,1,1,1,0,black,0,0,0,0,0,0,0,0,1,1,red,black\n",
            "El-Salvador,1,4,21,5,2,0,0,3,2,0,0,1,0,1,0,0,blue,0,0,0,0,0,0,0,0,0,0,blue,blue\n",
            "Equatorial-Guinea,4,1,28,0,10,5,0,3,4,1,1,1,0,1,0,0,green,0,0,0,0,0,0,1,0,0,0,green,red\n",
            "Ethiopia,4,1,1222,31,10,1,0,3,3,1,1,0,1,0,0,0,green,0,0,0,0,0,0,0,0,0,0,green,red\n",
            "Faeroes,3,4,1,0,6,1,0,0,3,1,0,1,0,1,0,0,white,0,1,0,0,0,0,0,0,0,0,white,white\n",
            "Falklands-Malvinas,2,3,12,0,1,1,0,0,6,1,1,1,1,1,0,0,blue,1,1,1,1,0,0,0,1,1,1,white,blue\n",
            "Fiji,6,2,18,1,1,1,0,0,7,1,1,1,1,1,0,1,blue,0,2,1,1,0,0,0,1,1,0,white,blue\n",
            "Finland,3,1,337,5,9,1,0,0,2,0,0,1,0,1,0,0,white,0,1,0,0,0,0,0,0,0,0,white,white\n",
            "France,3,1,547,54,3,0,3,0,3,1,0,1,0,1,0,0,white,0,0,0,0,0,0,0,0,0,0,blue,red\n",
            "French-Guiana,2,4,91,0,3,0,3,0,3,1,0,1,0,1,0,0,white,0,0,0,0,0,0,0,0,0,0,blue,red\n",
            "French-Polynesia,6,3,4,0,3,0,0,3,5,1,0,1,1,1,1,0,red,1,0,0,0,1,0,0,1,0,0,red,red\n",
            "Gabon,4,2,268,1,10,5,0,3,3,0,1,1,1,0,0,0,green,0,0,0,0,0,0,0,0,0,0,green,blue\n",
            "Gambia,4,4,10,1,1,5,0,5,4,1,1,1,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Germany-DDR,3,1,108,17,4,6,0,3,3,1,0,0,1,0,1,0,gold,0,0,0,0,0,0,0,1,0,0,black,gold\n",
            "Germany-FRG,3,1,249,61,4,1,0,3,3,1,0,0,1,0,1,0,black,0,0,0,0,0,0,0,0,0,0,black,gold\n",
            "Ghana,4,4,239,14,1,5,0,3,4,1,1,0,1,0,1,0,red,0,0,0,0,1,0,0,0,0,0,red,green\n",
            "Gibraltar,3,4,0,0,1,1,0,1,3,1,0,0,1,1,0,0,white,0,0,0,0,0,0,0,1,0,0,white,red\n",
            "Greece,3,1,132,10,6,1,0,9,2,0,0,1,0,1,0,0,blue,0,1,0,1,0,0,0,0,0,0,blue,blue\n",
            "Greenland,1,4,2176,0,6,1,0,0,2,1,0,0,0,1,0,0,white,1,0,0,0,0,0,0,0,0,0,white,red\n",
            "Grenada,1,4,0,0,1,1,0,0,3,1,1,0,1,0,0,0,gold,1,0,0,0,7,0,1,0,1,0,red,red\n",
            "Guam,6,1,0,0,1,1,0,0,7,1,1,1,1,1,0,1,blue,0,0,0,0,0,0,0,1,1,1,red,red\n",
            "Guatemala,1,4,109,8,2,0,3,0,2,0,0,1,0,1,0,0,blue,0,0,0,0,0,0,0,0,0,0,blue,blue\n",
            "Guinea,4,4,246,6,3,2,3,0,3,1,1,0,1,0,0,0,gold,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Guinea-Bissau,4,4,36,1,6,5,1,2,4,1,1,0,1,0,1,0,gold,0,0,0,0,1,0,0,0,0,0,red,green\n",
            "Guyana,2,4,215,1,1,4,0,0,5,1,1,0,1,1,1,0,green,0,0,0,0,0,0,1,0,0,0,black,green\n",
            "Haiti,1,4,28,6,3,0,2,0,2,1,0,0,0,0,1,0,black,0,0,0,0,0,0,0,0,0,0,black,red\n",
            "Honduras,1,4,112,4,2,0,0,3,2,0,0,1,0,1,0,0,blue,0,0,0,0,5,0,0,0,0,0,blue,blue\n",
            "Hong-Kong,5,1,1,5,7,3,0,0,6,1,1,1,1,1,0,1,blue,1,1,1,1,0,0,0,1,1,1,white,blue\n",
            "Hungary,3,1,93,11,9,6,0,3,3,1,1,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Iceland,3,4,103,0,6,1,0,0,3,1,0,1,0,1,0,0,blue,0,1,0,0,0,0,0,0,0,0,blue,blue\n",
            "India,5,1,3268,684,6,4,0,3,4,0,1,1,0,1,0,1,orange,1,0,0,0,0,0,0,1,0,0,orange,green\n",
            "Indonesia,6,2,1904,157,10,2,0,2,2,1,0,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,white\n",
            "Iran,5,1,1648,39,6,2,0,3,3,1,1,0,0,1,0,0,red,0,0,0,0,0,0,0,1,0,1,green,red\n",
            "Iraq,5,1,435,14,8,2,0,3,4,1,1,0,0,1,1,0,red,0,0,0,0,3,0,0,0,0,0,red,black\n",
            "Ireland,3,4,70,3,1,0,3,0,3,0,1,0,0,1,0,1,white,0,0,0,0,0,0,0,0,0,0,green,orange\n",
            "Israel,5,1,21,4,10,7,0,2,2,0,0,1,0,1,0,0,white,0,0,0,0,1,0,0,0,0,0,blue,blue\n",
            "Italy,3,1,301,57,6,0,3,0,3,1,1,0,0,1,0,0,white,0,0,0,0,0,0,0,0,0,0,green,red\n",
            "Ivory-Coast,4,4,323,7,3,5,3,0,3,1,1,0,0,1,0,0,white,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Jamaica,1,4,11,2,1,1,0,0,3,0,1,0,1,0,1,0,green,0,0,1,0,0,0,1,0,0,0,gold,gold\n",
            "Japan,5,1,372,118,9,7,0,0,2,1,0,0,0,1,0,0,white,1,0,0,0,1,0,0,0,0,0,white,white\n",
            "Jordan,5,1,98,2,8,2,0,3,4,1,1,0,0,1,1,0,black,0,0,0,0,1,0,1,0,0,0,black,green\n",
            "Kampuchea,5,1,181,6,10,3,0,0,2,1,0,0,1,0,0,0,red,0,0,0,0,0,0,0,1,0,0,red,red\n",
            "Kenya,4,1,583,17,10,5,0,5,4,1,1,0,0,1,1,0,red,1,0,0,0,0,0,0,1,0,0,black,green\n",
            "Kiribati,6,1,0,0,1,1,0,0,4,1,0,1,1,1,0,0,red,0,0,0,0,1,0,0,1,1,0,red,blue\n",
            "Kuwait,5,1,18,2,8,2,0,3,4,1,1,0,0,1,1,0,green,0,0,0,0,0,0,0,0,0,0,green,red\n",
            "Laos,5,1,236,3,10,6,0,3,3,1,0,1,0,1,0,0,red,1,0,0,0,0,0,0,0,0,0,red,red\n",
            "Lebanon,5,1,10,3,8,2,0,2,4,1,1,0,0,1,0,1,red,0,0,0,0,0,0,0,0,1,0,red,red\n",
            "Lesotho,4,2,30,1,10,5,2,0,4,1,1,1,0,1,0,0,blue,0,0,0,0,0,0,0,1,0,0,green,blue\n",
            "Liberia,4,4,111,1,10,5,0,11,3,1,0,1,0,1,0,0,red,0,0,0,1,1,0,0,0,0,0,blue,red\n",
            "Libya,4,1,1760,3,8,2,0,0,1,0,1,0,0,0,0,0,green,0,0,0,0,0,0,0,0,0,0,green,green\n",
            "Liechtenstein,3,1,0,0,4,0,0,2,3,1,0,1,1,0,0,0,red,0,0,0,0,0,0,0,1,0,0,blue,red\n",
            "Luxembourg,3,1,3,0,4,0,0,3,3,1,0,1,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,blue\n",
            "Malagasy,4,2,587,9,10,1,1,2,3,1,1,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,white,green\n",
            "Malawi,4,2,118,6,10,5,0,3,3,1,1,0,0,0,1,0,red,0,0,0,0,1,0,0,0,0,0,black,green\n",
            "Malaysia,5,1,333,13,10,2,0,14,4,1,0,1,1,1,0,0,red,0,0,0,1,1,1,0,0,0,0,blue,white\n",
            "Maldive-Islands,5,1,0,0,10,2,0,0,3,1,1,0,0,1,0,0,red,0,0,0,0,0,1,0,0,0,0,red,red\n",
            "Mali,4,4,1240,7,3,2,3,0,3,1,1,0,1,0,0,0,gold,0,0,0,0,0,0,0,0,0,0,green,red\n",
            "Malta,3,1,0,0,10,0,2,0,3,1,0,0,0,1,1,0,red,0,1,0,0,0,0,0,1,0,0,white,red\n",
            "Marianas,6,1,0,0,10,1,0,0,3,0,0,1,0,1,0,0,blue,0,0,0,0,1,0,0,1,0,0,blue,blue\n",
            "Mauritania,4,4,1031,2,8,2,0,0,2,0,1,0,1,0,0,0,green,0,0,0,0,1,1,0,0,0,0,green,green\n",
            "Mauritius,4,2,2,1,1,4,0,4,4,1,1,1,1,0,0,0,red,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Mexico,1,4,1973,77,2,0,3,0,4,1,1,0,0,1,0,1,green,0,0,0,0,0,0,0,0,1,0,green,red\n",
            "Micronesia,6,1,1,0,10,1,0,0,2,0,0,1,0,1,0,0,blue,0,0,0,0,4,0,0,0,0,0,blue,blue\n",
            "Monaco,3,1,0,0,3,0,0,2,2,1,0,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,white\n",
            "Mongolia,5,1,1566,2,10,6,3,0,3,1,0,1,1,0,0,0,red,2,0,0,0,1,1,1,1,0,0,red,red\n",
            "Montserrat,1,4,0,0,1,1,0,0,7,1,1,1,1,1,1,0,blue,0,2,1,1,0,0,0,1,1,0,white,blue\n",
            "Morocco,4,4,447,20,8,2,0,0,2,1,1,0,0,0,0,0,red,0,0,0,0,1,0,0,0,0,0,red,red\n",
            "Mozambique,4,2,783,12,10,5,0,5,5,1,1,0,1,1,1,0,gold,0,0,0,0,1,0,1,1,0,0,green,gold\n",
            "Nauru,6,2,0,0,10,1,0,3,3,0,0,1,1,1,0,0,blue,0,0,0,0,1,0,0,0,0,0,blue,blue\n",
            "Nepal,5,1,140,16,10,4,0,0,3,0,0,1,0,1,0,1,brown,0,0,0,0,2,1,0,0,0,0,blue,blue\n",
            "Netherlands,3,1,41,14,6,1,0,3,3,1,0,1,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,blue\n",
            "Netherlands-Antilles,1,4,0,0,6,1,0,1,3,1,0,1,0,1,0,0,white,0,0,0,0,6,0,0,0,0,0,white,white\n",
            "New-Zealand,6,2,268,2,1,1,0,0,3,1,0,1,0,1,0,0,blue,0,1,1,1,4,0,0,0,0,0,white,blue\n",
            "Nicaragua,1,4,128,3,2,0,0,3,2,0,0,1,0,1,0,0,blue,0,0,0,0,0,0,0,0,0,0,blue,blue\n",
            "Niger,4,1,1267,5,3,2,0,3,3,0,1,0,0,1,0,1,orange,1,0,0,0,0,0,0,0,0,0,orange,green\n",
            "Nigeria,4,1,925,56,10,2,3,0,2,0,1,0,0,1,0,0,green,0,0,0,0,0,0,0,0,0,0,green,green\n",
            "Niue,6,3,0,0,1,1,0,0,4,1,0,1,1,1,0,0,gold,1,1,1,1,5,0,0,0,0,0,white,gold\n",
            "North-Korea,5,1,121,18,10,6,0,5,3,1,0,1,0,1,0,0,blue,1,0,0,0,1,0,0,0,0,0,blue,blue\n",
            "North-Yemen,5,1,195,9,8,2,0,3,4,1,1,0,0,1,1,0,red,0,0,0,0,1,0,0,0,0,0,red,black\n",
            "Norway,3,1,324,4,6,1,0,0,3,1,0,1,0,1,0,0,red,0,1,0,0,0,0,0,0,0,0,red,red\n",
            "Oman,5,1,212,1,8,2,0,2,3,1,1,0,0,1,0,0,red,0,0,0,0,0,0,0,1,0,0,red,green\n",
            "Pakistan,5,1,804,84,6,2,1,0,2,0,1,0,0,1,0,0,green,0,0,0,0,1,1,0,0,0,0,white,green\n",
            "Panama,2,4,76,2,2,0,0,0,3,1,0,1,0,1,0,0,red,0,0,0,4,2,0,0,0,0,0,white,white\n",
            "Papua-New-Guinea,6,2,463,3,1,5,0,0,4,1,0,0,1,1,1,0,black,0,0,0,0,5,0,1,0,1,0,red,black\n",
            "Parguay,2,3,407,3,2,0,0,3,6,1,1,1,1,1,1,0,red,1,0,0,0,1,0,0,1,1,1,red,blue\n",
            "Peru,2,3,1285,14,2,0,3,0,2,1,0,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,red\n",
            "Philippines,6,1,300,48,10,0,0,0,4,1,0,1,1,1,0,0,blue,0,0,0,0,4,0,1,0,0,0,blue,red\n",
            "Poland,3,1,313,36,5,6,0,2,2,1,0,0,0,1,0,0,white,0,0,0,0,0,0,0,0,0,0,white,red\n",
            "Portugal,3,4,92,10,6,0,0,0,5,1,1,1,1,1,0,0,red,1,0,0,0,0,0,0,1,0,0,green,red\n",
            "Puerto-Rico,1,4,9,3,2,0,0,5,3,1,0,1,0,1,0,0,red,0,0,0,0,1,0,1,0,0,0,red,red\n",
            "Qatar,5,1,11,0,8,2,0,0,2,0,0,0,0,1,0,1,brown,0,0,0,0,0,0,0,0,0,0,white,brown\n",
            "Romania,3,1,237,22,6,6,3,0,7,1,1,1,1,1,0,1,red,0,0,0,0,2,0,0,1,1,1,blue,red\n",
            "Rwanda,4,2,26,5,10,5,3,0,4,1,1,0,1,0,1,0,red,0,0,0,0,0,0,0,0,0,1,red,green\n",
            "San-Marino,3,1,0,0,6,0,0,2,2,0,0,1,0,1,0,0,white,0,0,0,0,0,0,0,0,0,0,white,blue\n",
            "Sao-Tome,4,1,0,0,6,0,0,3,4,1,1,0,1,0,1,0,green,0,0,0,0,2,0,1,0,0,0,green,green\n",
            "Saudi-Arabia,5,1,2150,9,8,2,0,0,2,0,1,0,0,1,0,0,green,0,0,0,0,0,0,0,1,0,1,green,green\n",
            "Senegal,4,4,196,6,3,2,3,0,3,1,1,0,1,0,0,0,green,0,0,0,0,1,0,0,0,0,0,green,red\n",
            "Seychelles,4,2,0,0,1,1,0,0,3,1,1,0,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,green\n",
            "Sierra-Leone,4,4,72,3,1,5,0,3,3,0,1,1,0,1,0,0,green,0,0,0,0,0,0,0,0,0,0,green,blue\n",
            "Singapore,5,1,1,3,7,3,0,2,2,1,0,0,0,1,0,0,white,0,0,0,0,5,1,0,0,0,0,red,white\n",
            "Soloman-Islands,6,2,30,0,1,1,0,0,4,0,1,1,1,1,0,0,green,0,0,0,0,5,0,1,0,0,0,blue,green\n",
            "Somalia,4,1,637,5,10,2,0,0,2,0,0,1,0,1,0,0,blue,0,0,0,0,1,0,0,0,0,0,blue,blue\n",
            "South-Africa,4,2,1221,29,6,1,0,3,5,1,1,1,0,1,0,1,orange,0,1,1,0,0,0,0,0,0,0,orange,blue\n",
            "South-Korea,5,1,99,39,10,7,0,0,4,1,0,1,0,1,1,0,white,1,0,0,0,0,0,0,1,0,0,white,white\n",
            "South-Yemen,5,1,288,2,8,2,0,3,4,1,0,1,0,1,1,0,red,0,0,0,0,1,0,1,0,0,0,red,black\n",
            "Spain,3,4,505,38,2,0,0,3,2,1,0,0,1,0,0,0,red,0,0,0,0,0,0,0,0,0,0,red,red\n",
            "Sri-Lanka,5,1,66,15,10,3,2,0,4,0,1,0,1,0,0,1,gold,0,0,0,0,0,0,0,1,1,0,gold,gold\n",
            "St-Helena,4,3,0,0,1,1,0,0,7,1,1,1,1,1,0,1,blue,0,1,1,1,0,0,0,1,0,0,white,blue\n",
            "St-Kitts-Nevis,1,4,0,0,1,1,0,0,5,1,1,0,1,1,1,0,green,0,0,0,0,2,0,1,0,0,0,green,red\n",
            "St-Lucia,1,4,0,0,1,1,0,0,4,0,0,1,1,1,1,0,blue,0,0,0,0,0,0,1,0,0,0,blue,blue\n",
            "St-Vincent,1,4,0,0,1,1,5,0,4,0,1,1,1,1,0,0,green,0,0,0,0,0,0,0,1,1,1,blue,green\n",
            "Sudan,4,1,2506,20,8,2,0,3,4,1,1,0,0,1,1,0,red,0,0,0,0,0,0,1,0,0,0,red,black\n",
            "Surinam,2,4,63,0,6,1,0,5,4,1,1,0,1,1,0,0,red,0,0,0,0,1,0,0,0,0,0,green,green\n",
            "Swaziland,4,2,17,1,10,1,0,5,7,1,0,1,1,1,1,1,blue,0,0,0,0,0,0,0,1,0,0,blue,blue\n",
            "Sweden,3,1,450,8,6,1,0,0,2,0,0,1,1,0,0,0,blue,0,1,0,0,0,0,0,0,0,0,blue,blue\n",
            "Switzerland,3,1,41,6,4,1,0,0,2,1,0,0,0,1,0,0,red,0,1,0,0,0,0,0,0,0,0,red,red\n",
            "Syria,5,1,185,10,8,2,0,3,4,1,1,0,0,1,1,0,red,0,0,0,0,2,0,0,0,0,0,red,black\n",
            "Taiwan,5,1,36,18,7,3,0,0,3,1,0,1,0,1,0,0,red,1,0,0,1,1,0,0,0,0,0,blue,red\n",
            "Tanzania,4,2,945,18,10,5,0,0,4,0,1,1,1,0,1,0,green,0,0,0,0,0,0,1,0,0,0,green,blue\n",
            "Thailand,5,1,514,49,10,3,0,5,3,1,0,1,0,1,0,0,red,0,0,0,0,0,0,0,0,0,0,red,red\n",
            "Togo,4,1,57,2,3,7,0,5,4,1,1,0,1,1,0,0,green,0,0,0,1,1,0,0,0,0,0,red,green\n",
            "Tonga,6,2,1,0,10,1,0,0,2,1,0,0,0,1,0,0,red,0,1,0,1,0,0,0,0,0,0,white,red\n",
            "Trinidad-Tobago,2,4,5,1,1,1,0,0,3,1,0,0,0,1,1,0,red,0,0,0,0,0,0,1,0,0,0,white,white\n",
            "Tunisia,4,1,164,7,8,2,0,0,2,1,0,0,0,1,0,0,red,1,0,0,0,1,1,0,0,0,0,red,red\n",
            "Turkey,5,1,781,45,9,2,0,0,2,1,0,0,0,1,0,0,red,0,0,0,0,1,1,0,0,0,0,red,red\n",
            "Turks-Cocos-Islands,1,4,0,0,1,1,0,0,6,1,1,1,1,1,0,1,blue,0,1,1,1,0,0,0,1,1,0,white,blue\n",
            "Tuvalu,6,2,0,0,1,1,0,0,5,1,0,1,1,1,0,0,blue,0,1,1,1,9,0,0,0,0,0,white,blue\n",
            "UAE,5,1,84,1,8,2,1,3,4,1,1,0,0,1,1,0,green,0,0,0,0,0,0,0,0,0,0,red,black\n",
            "Uganda,4,1,236,13,10,5,0,6,5,1,0,0,1,1,1,0,gold,1,0,0,0,0,0,0,0,1,0,black,red\n",
            "UK,3,4,245,56,1,1,0,0,3,1,0,1,0,1,0,0,red,0,1,1,0,0,0,0,0,0,0,white,red\n",
            "Uruguay,2,3,178,3,2,0,0,9,3,0,0,1,1,1,0,0,white,0,0,0,1,1,0,0,0,0,0,white,white\n",
            "US-Virgin-Isles,1,4,0,0,1,1,0,0,6,1,1,1,1,1,0,0,white,0,0,0,0,0,0,0,1,1,1,white,white\n",
            "USA,1,4,9363,231,1,1,0,13,3,1,0,1,0,1,0,0,white,0,0,0,1,50,0,0,0,0,0,blue,red\n",
            "USSR,5,1,22402,274,5,6,0,0,2,1,0,0,1,0,0,0,red,0,0,0,0,1,0,0,1,0,0,red,red\n",
            "Vanuatu,6,2,15,0,6,1,0,0,4,1,1,0,1,0,1,0,red,0,0,0,0,0,0,1,0,1,0,black,green\n",
            "Vatican-City,3,1,0,0,6,0,2,0,4,1,0,0,1,1,1,0,gold,0,0,0,0,0,0,0,1,0,0,gold,white\n",
            "Venezuela,2,4,912,15,2,0,0,3,7,1,1,1,1,1,1,1,red,0,0,0,0,7,0,0,1,1,0,gold,red\n",
            "Vietnam,5,1,333,60,10,6,0,0,2,1,0,0,1,0,0,0,red,0,0,0,0,1,0,0,0,0,0,red,red\n",
            "Western-Samoa,6,3,3,0,1,1,0,0,3,1,0,1,0,1,0,0,red,0,0,0,1,5,0,0,0,0,0,blue,red\n",
            "Yugoslavia,3,1,256,22,6,6,0,3,4,1,0,1,1,1,0,0,red,0,0,0,0,1,0,0,0,0,0,blue,red\n",
            "Zaire,4,2,905,28,10,5,0,0,4,1,1,0,1,0,0,1,green,1,0,0,0,0,0,0,1,1,0,green,green\n",
            "Zambia,4,2,753,6,10,5,3,0,4,1,1,0,0,0,1,1,green,0,0,0,0,0,0,0,0,1,0,green,brown\n",
            "Zimbabwe,4,2,391,8,10,5,0,7,5,1,1,0,1,1,1,0,green,0,0,0,0,1,0,1,1,1,0,green,green\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UKfOq1tlUvbZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Step 2 - load the data\n",
        "\n",
        "# How to deal with a csv? 🐼\n",
        "import pandas as pd\n",
        "flag_data = pd.read_csv(flag_data_url)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "exKPtcJyUyCX",
        "colab_type": "code",
        "outputId": "ab8bbd2b-4236-4e9b-c043-21636c0d340f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        }
      },
      "source": [
        "# Step 3 - verify we've got *something*\n",
        "flag_data.head()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Afghanistan</th>\n",
              "      <th>5</th>\n",
              "      <th>1</th>\n",
              "      <th>648</th>\n",
              "      <th>16</th>\n",
              "      <th>10</th>\n",
              "      <th>2</th>\n",
              "      <th>0</th>\n",
              "      <th>3</th>\n",
              "      <th>5.1</th>\n",
              "      <th>...</th>\n",
              "      <th>0.5</th>\n",
              "      <th>0.6</th>\n",
              "      <th>1.6</th>\n",
              "      <th>0.7</th>\n",
              "      <th>0.8</th>\n",
              "      <th>1.7</th>\n",
              "      <th>0.9</th>\n",
              "      <th>0.10</th>\n",
              "      <th>black</th>\n",
              "      <th>green.1</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Albania</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>red</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Algeria</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>2388</td>\n",
              "      <td>20</td>\n",
              "      <td>8</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>green</td>\n",
              "      <td>white</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>American-Samoa</td>\n",
              "      <td>6</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>5</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>blue</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Andorra</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>blue</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Angola</td>\n",
              "      <td>4</td>\n",
              "      <td>2</td>\n",
              "      <td>1247</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>red</td>\n",
              "      <td>black</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 30 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      Afghanistan  5  1   648  16  10  2  0  3  5.1  ...  0.5  0.6  1.6  0.7  \\\n",
              "0         Albania  3  1    29   3   6  6  0  0    3  ...    0    0    1    0   \n",
              "1         Algeria  4  1  2388  20   8  2  2  0    3  ...    0    0    1    1   \n",
              "2  American-Samoa  6  3     0   0   1  1  0  0    5  ...    0    0    0    0   \n",
              "3         Andorra  3  1     0   0   6  0  3  0    3  ...    0    0    0    0   \n",
              "4          Angola  4  2  1247   7  10  5  0  2    3  ...    0    0    1    0   \n",
              "\n",
              "   0.8  1.7  0.9 0.10  black  green.1  \n",
              "0    0    0    1    0    red      red  \n",
              "1    0    0    0    0  green    white  \n",
              "2    1    1    1    0   blue      red  \n",
              "3    0    0    0    0   blue      red  \n",
              "4    0    1    0    0    red    black  \n",
              "\n",
              "[5 rows x 30 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rNmkv2g8VfAm",
        "colab_type": "code",
        "outputId": "055bcf09-ed6b-4dea-957b-3a911481536b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 555
        }
      },
      "source": [
        "# Step 4 - Looks a bit odd - verify that it is what we want\n",
        "flag_data.count()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Afghanistan    193\n",
              "5              193\n",
              "1              193\n",
              "648            193\n",
              "16             193\n",
              "10             193\n",
              "2              193\n",
              "0              193\n",
              "3              193\n",
              "5.1            193\n",
              "1.1            193\n",
              "1.2            193\n",
              "0.1            193\n",
              "1.3            193\n",
              "1.4            193\n",
              "1.5            193\n",
              "0.2            193\n",
              "green          193\n",
              "0.3            193\n",
              "0.4            193\n",
              "0.5            193\n",
              "0.6            193\n",
              "1.6            193\n",
              "0.7            193\n",
              "0.8            193\n",
              "1.7            193\n",
              "0.9            193\n",
              "0.10           193\n",
              "black          193\n",
              "green.1        193\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iqPEwx3aWBDR",
        "colab_type": "code",
        "outputId": "6acf3192-dac1-4007-debc-7c5e820b6aa5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        }
      },
      "source": [
        "!curl https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data | wc"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n",
            "                                 Dload  Upload   Total   Spent    Left  Speed\n",
            "\r  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0\r100 15240  100 15240    0     0  92363      0 --:--:-- --:--:-- --:--:-- 92363\n",
            "    194     194   15240\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5R1d1Ka2WHAY",
        "colab_type": "code",
        "outputId": "0b4539d9-52ba-4d4e-edd1-6c540d93b55f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 5081
        }
      },
      "source": [
        "# So we have 193 observations with funny names, file has 194 rows\n",
        "# Looks like the file has no header row, but read_csv assumes it does\n",
        "help(pd.read_csv)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Help on function read_csv in module pandas.io.parsers:\n",
            "\n",
            "read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='\"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)\n",
            "    Read a comma-separated values (csv) file into DataFrame.\n",
            "    \n",
            "    Also supports optionally iterating or breaking of the file\n",
            "    into chunks.\n",
            "    \n",
            "    Additional help can be found in the online docs for\n",
            "    `IO Tools <http://pandas.pydata.org/pandas-docs/stable/io.html>`_.\n",
            "    \n",
            "    Parameters\n",
            "    ----------\n",
            "    filepath_or_buffer : str, path object, or file-like object\n",
            "        Any valid string path is acceptable. The string could be a URL. Valid\n",
            "        URL schemes include http, ftp, s3, and file. For file URLs, a host is\n",
            "        expected. A local file could be: file://localhost/path/to/table.csv.\n",
            "    \n",
            "        If you want to pass in a path object, pandas accepts either\n",
            "        ``pathlib.Path`` or ``py._path.local.LocalPath``.\n",
            "    \n",
            "        By file-like object, we refer to objects with a ``read()`` method, such as\n",
            "        a file handler (e.g. via builtin ``open`` function) or ``StringIO``.\n",
            "    sep : str, default ','\n",
            "        Delimiter to use. If sep is None, the C engine cannot automatically detect\n",
            "        the separator, but the Python parsing engine can, meaning the latter will\n",
            "        be used and automatically detect the separator by Python's builtin sniffer\n",
            "        tool, ``csv.Sniffer``. In addition, separators longer than 1 character and\n",
            "        different from ``'\\s+'`` will be interpreted as regular expressions and\n",
            "        will also force the use of the Python parsing engine. Note that regex\n",
            "        delimiters are prone to ignoring quoted data. Regex example: ``'\\r\\t'``.\n",
            "    delimiter : str, default ``None``\n",
            "        Alias for sep.\n",
            "    header : int, list of int, default 'infer'\n",
            "        Row number(s) to use as the column names, and the start of the\n",
            "        data.  Default behavior is to infer the column names: if no names\n",
            "        are passed the behavior is identical to ``header=0`` and column\n",
            "        names are inferred from the first line of the file, if column\n",
            "        names are passed explicitly then the behavior is identical to\n",
            "        ``header=None``. Explicitly pass ``header=0`` to be able to\n",
            "        replace existing names. The header can be a list of integers that\n",
            "        specify row locations for a multi-index on the columns\n",
            "        e.g. [0,1,3]. Intervening rows that are not specified will be\n",
            "        skipped (e.g. 2 in this example is skipped). Note that this\n",
            "        parameter ignores commented lines and empty lines if\n",
            "        ``skip_blank_lines=True``, so ``header=0`` denotes the first line of\n",
            "        data rather than the first line of the file.\n",
            "    names : array-like, optional\n",
            "        List of column names to use. If file contains no header row, then you\n",
            "        should explicitly pass ``header=None``. Duplicates in this list will cause\n",
            "        a ``UserWarning`` to be issued.\n",
            "    index_col : int, sequence or bool, optional\n",
            "        Column to use as the row labels of the DataFrame. If a sequence is given, a\n",
            "        MultiIndex is used. If you have a malformed file with delimiters at the end\n",
            "        of each line, you might consider ``index_col=False`` to force pandas to\n",
            "        not use the first column as the index (row names).\n",
            "    usecols : list-like or callable, optional\n",
            "        Return a subset of the columns. If list-like, all elements must either\n",
            "        be positional (i.e. integer indices into the document columns) or strings\n",
            "        that correspond to column names provided either by the user in `names` or\n",
            "        inferred from the document header row(s). For example, a valid list-like\n",
            "        `usecols` parameter would be ``[0, 1, 2]`` or ``['foo', 'bar', 'baz']``.\n",
            "        Element order is ignored, so ``usecols=[0, 1]`` is the same as ``[1, 0]``.\n",
            "        To instantiate a DataFrame from ``data`` with element order preserved use\n",
            "        ``pd.read_csv(data, usecols=['foo', 'bar'])[['foo', 'bar']]`` for columns\n",
            "        in ``['foo', 'bar']`` order or\n",
            "        ``pd.read_csv(data, usecols=['foo', 'bar'])[['bar', 'foo']]``\n",
            "        for ``['bar', 'foo']`` order.\n",
            "    \n",
            "        If callable, the callable function will be evaluated against the column\n",
            "        names, returning names where the callable function evaluates to True. An\n",
            "        example of a valid callable argument would be ``lambda x: x.upper() in\n",
            "        ['AAA', 'BBB', 'DDD']``. Using this parameter results in much faster\n",
            "        parsing time and lower memory usage.\n",
            "    squeeze : bool, default False\n",
            "        If the parsed data only contains one column then return a Series.\n",
            "    prefix : str, optional\n",
            "        Prefix to add to column numbers when no header, e.g. 'X' for X0, X1, ...\n",
            "    mangle_dupe_cols : bool, default True\n",
            "        Duplicate columns will be specified as 'X', 'X.1', ...'X.N', rather than\n",
            "        'X'...'X'. Passing in False will cause data to be overwritten if there\n",
            "        are duplicate names in the columns.\n",
            "    dtype : Type name or dict of column -> type, optional\n",
            "        Data type for data or columns. E.g. {'a': np.float64, 'b': np.int32,\n",
            "        'c': 'Int64'}\n",
            "        Use `str` or `object` together with suitable `na_values` settings\n",
            "        to preserve and not interpret dtype.\n",
            "        If converters are specified, they will be applied INSTEAD\n",
            "        of dtype conversion.\n",
            "    engine : {'c', 'python'}, optional\n",
            "        Parser engine to use. The C engine is faster while the python engine is\n",
            "        currently more feature-complete.\n",
            "    converters : dict, optional\n",
            "        Dict of functions for converting values in certain columns. Keys can either\n",
            "        be integers or column labels.\n",
            "    true_values : list, optional\n",
            "        Values to consider as True.\n",
            "    false_values : list, optional\n",
            "        Values to consider as False.\n",
            "    skipinitialspace : bool, default False\n",
            "        Skip spaces after delimiter.\n",
            "    skiprows : list-like, int or callable, optional\n",
            "        Line numbers to skip (0-indexed) or number of lines to skip (int)\n",
            "        at the start of the file.\n",
            "    \n",
            "        If callable, the callable function will be evaluated against the row\n",
            "        indices, returning True if the row should be skipped and False otherwise.\n",
            "        An example of a valid callable argument would be ``lambda x: x in [0, 2]``.\n",
            "    skipfooter : int, default 0\n",
            "        Number of lines at bottom of file to skip (Unsupported with engine='c').\n",
            "    nrows : int, optional\n",
            "        Number of rows of file to read. Useful for reading pieces of large files.\n",
            "    na_values : scalar, str, list-like, or dict, optional\n",
            "        Additional strings to recognize as NA/NaN. If dict passed, specific\n",
            "        per-column NA values.  By default the following values are interpreted as\n",
            "        NaN: '', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan',\n",
            "        '1.#IND', '1.#QNAN', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan',\n",
            "        'null'.\n",
            "    keep_default_na : bool, default True\n",
            "        Whether or not to include the default NaN values when parsing the data.\n",
            "        Depending on whether `na_values` is passed in, the behavior is as follows:\n",
            "    \n",
            "        * If `keep_default_na` is True, and `na_values` are specified, `na_values`\n",
            "          is appended to the default NaN values used for parsing.\n",
            "        * If `keep_default_na` is True, and `na_values` are not specified, only\n",
            "          the default NaN values are used for parsing.\n",
            "        * If `keep_default_na` is False, and `na_values` are specified, only\n",
            "          the NaN values specified `na_values` are used for parsing.\n",
            "        * If `keep_default_na` is False, and `na_values` are not specified, no\n",
            "          strings will be parsed as NaN.\n",
            "    \n",
            "        Note that if `na_filter` is passed in as False, the `keep_default_na` and\n",
            "        `na_values` parameters will be ignored.\n",
            "    na_filter : bool, default True\n",
            "        Detect missing value markers (empty strings and the value of na_values). In\n",
            "        data without any NAs, passing na_filter=False can improve the performance\n",
            "        of reading a large file.\n",
            "    verbose : bool, default False\n",
            "        Indicate number of NA values placed in non-numeric columns.\n",
            "    skip_blank_lines : bool, default True\n",
            "        If True, skip over blank lines rather than interpreting as NaN values.\n",
            "    parse_dates : bool or list of int or names or list of lists or dict, default False\n",
            "        The behavior is as follows:\n",
            "    \n",
            "        * boolean. If True -> try parsing the index.\n",
            "        * list of int or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3\n",
            "          each as a separate date column.\n",
            "        * list of lists. e.g.  If [[1, 3]] -> combine columns 1 and 3 and parse as\n",
            "          a single date column.\n",
            "        * dict, e.g. {'foo' : [1, 3]} -> parse columns 1, 3 as date and call\n",
            "          result 'foo'\n",
            "    \n",
            "        If a column or index cannot be represented as an array of datetimes,\n",
            "        say because of an unparseable value or a mixture of timezones, the column\n",
            "        or index will be returned unaltered as an object data type. For\n",
            "        non-standard datetime parsing, use ``pd.to_datetime`` after\n",
            "        ``pd.read_csv``. To parse an index or column with a mixture of timezones,\n",
            "        specify ``date_parser`` to be a partially-applied\n",
            "        :func:`pandas.to_datetime` with ``utc=True``. See\n",
            "        :ref:`io.csv.mixed_timezones` for more.\n",
            "    \n",
            "        Note: A fast-path exists for iso8601-formatted dates.\n",
            "    infer_datetime_format : bool, default False\n",
            "        If True and `parse_dates` is enabled, pandas will attempt to infer the\n",
            "        format of the datetime strings in the columns, and if it can be inferred,\n",
            "        switch to a faster method of parsing them. In some cases this can increase\n",
            "        the parsing speed by 5-10x.\n",
            "    keep_date_col : bool, default False\n",
            "        If True and `parse_dates` specifies combining multiple columns then\n",
            "        keep the original columns.\n",
            "    date_parser : function, optional\n",
            "        Function to use for converting a sequence of string columns to an array of\n",
            "        datetime instances. The default uses ``dateutil.parser.parser`` to do the\n",
            "        conversion. Pandas will try to call `date_parser` in three different ways,\n",
            "        advancing to the next if an exception occurs: 1) Pass one or more arrays\n",
            "        (as defined by `parse_dates`) as arguments; 2) concatenate (row-wise) the\n",
            "        string values from the columns defined by `parse_dates` into a single array\n",
            "        and pass that; and 3) call `date_parser` once for each row using one or\n",
            "        more strings (corresponding to the columns defined by `parse_dates`) as\n",
            "        arguments.\n",
            "    dayfirst : bool, default False\n",
            "        DD/MM format dates, international and European format.\n",
            "    iterator : bool, default False\n",
            "        Return TextFileReader object for iteration or getting chunks with\n",
            "        ``get_chunk()``.\n",
            "    chunksize : int, optional\n",
            "        Return TextFileReader object for iteration.\n",
            "        See the `IO Tools docs\n",
            "        <http://pandas.pydata.org/pandas-docs/stable/io.html#io-chunking>`_\n",
            "        for more information on ``iterator`` and ``chunksize``.\n",
            "    compression : {'infer', 'gzip', 'bz2', 'zip', 'xz', None}, default 'infer'\n",
            "        For on-the-fly decompression of on-disk data. If 'infer' and\n",
            "        `filepath_or_buffer` is path-like, then detect compression from the\n",
            "        following extensions: '.gz', '.bz2', '.zip', or '.xz' (otherwise no\n",
            "        decompression). If using 'zip', the ZIP file must contain only one data\n",
            "        file to be read in. Set to None for no decompression.\n",
            "    \n",
            "        .. versionadded:: 0.18.1 support for 'zip' and 'xz' compression.\n",
            "    \n",
            "    thousands : str, optional\n",
            "        Thousands separator.\n",
            "    decimal : str, default '.'\n",
            "        Character to recognize as decimal point (e.g. use ',' for European data).\n",
            "    lineterminator : str (length 1), optional\n",
            "        Character to break file into lines. Only valid with C parser.\n",
            "    quotechar : str (length 1), optional\n",
            "        The character used to denote the start and end of a quoted item. Quoted\n",
            "        items can include the delimiter and it will be ignored.\n",
            "    quoting : int or csv.QUOTE_* instance, default 0\n",
            "        Control field quoting behavior per ``csv.QUOTE_*`` constants. Use one of\n",
            "        QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).\n",
            "    doublequote : bool, default ``True``\n",
            "       When quotechar is specified and quoting is not ``QUOTE_NONE``, indicate\n",
            "       whether or not to interpret two consecutive quotechar elements INSIDE a\n",
            "       field as a single ``quotechar`` element.\n",
            "    escapechar : str (length 1), optional\n",
            "        One-character string used to escape other characters.\n",
            "    comment : str, optional\n",
            "        Indicates remainder of line should not be parsed. If found at the beginning\n",
            "        of a line, the line will be ignored altogether. This parameter must be a\n",
            "        single character. Like empty lines (as long as ``skip_blank_lines=True``),\n",
            "        fully commented lines are ignored by the parameter `header` but not by\n",
            "        `skiprows`. For example, if ``comment='#'``, parsing\n",
            "        ``#empty\\na,b,c\\n1,2,3`` with ``header=0`` will result in 'a,b,c' being\n",
            "        treated as the header.\n",
            "    encoding : str, optional\n",
            "        Encoding to use for UTF when reading/writing (ex. 'utf-8'). `List of Python\n",
            "        standard encodings\n",
            "        <https://docs.python.org/3/library/codecs.html#standard-encodings>`_ .\n",
            "    dialect : str or csv.Dialect, optional\n",
            "        If provided, this parameter will override values (default or not) for the\n",
            "        following parameters: `delimiter`, `doublequote`, `escapechar`,\n",
            "        `skipinitialspace`, `quotechar`, and `quoting`. If it is necessary to\n",
            "        override values, a ParserWarning will be issued. See csv.Dialect\n",
            "        documentation for more details.\n",
            "    tupleize_cols : bool, default False\n",
            "        Leave a list of tuples on columns as is (default is to convert to\n",
            "        a MultiIndex on the columns).\n",
            "    \n",
            "        .. deprecated:: 0.21.0\n",
            "           This argument will be removed and will always convert to MultiIndex\n",
            "    \n",
            "    error_bad_lines : bool, default True\n",
            "        Lines with too many fields (e.g. a csv line with too many commas) will by\n",
            "        default cause an exception to be raised, and no DataFrame will be returned.\n",
            "        If False, then these \"bad lines\" will dropped from the DataFrame that is\n",
            "        returned.\n",
            "    warn_bad_lines : bool, default True\n",
            "        If error_bad_lines is False, and warn_bad_lines is True, a warning for each\n",
            "        \"bad line\" will be output.\n",
            "    delim_whitespace : bool, default False\n",
            "        Specifies whether or not whitespace (e.g. ``' '`` or ``'    '``) will be\n",
            "        used as the sep. Equivalent to setting ``sep='\\s+'``. If this option\n",
            "        is set to True, nothing should be passed in for the ``delimiter``\n",
            "        parameter.\n",
            "    \n",
            "        .. versionadded:: 0.18.1 support for the Python parser.\n",
            "    \n",
            "    low_memory : bool, default True\n",
            "        Internally process the file in chunks, resulting in lower memory use\n",
            "        while parsing, but possibly mixed type inference.  To ensure no mixed\n",
            "        types either set False, or specify the type with the `dtype` parameter.\n",
            "        Note that the entire file is read into a single DataFrame regardless,\n",
            "        use the `chunksize` or `iterator` parameter to return the data in chunks.\n",
            "        (Only valid with C parser).\n",
            "    memory_map : bool, default False\n",
            "        If a filepath is provided for `filepath_or_buffer`, map the file object\n",
            "        directly onto memory and access the data directly from there. Using this\n",
            "        option can improve performance because there is no longer any I/O overhead.\n",
            "    float_precision : str, optional\n",
            "        Specifies which converter the C engine should use for floating-point\n",
            "        values. The options are `None` for the ordinary converter,\n",
            "        `high` for the high-precision converter, and `round_trip` for the\n",
            "        round-trip converter.\n",
            "    \n",
            "    Returns\n",
            "    -------\n",
            "    DataFrame or TextParser\n",
            "        A comma-separated values (csv) file is returned as two-dimensional\n",
            "        data structure with labeled axes.\n",
            "    \n",
            "    See Also\n",
            "    --------\n",
            "    to_csv : Write DataFrame to a comma-separated values (csv) file.\n",
            "    read_csv : Read a comma-separated values (csv) file into DataFrame.\n",
            "    read_fwf : Read a table of fixed-width formatted lines into DataFrame.\n",
            "    \n",
            "    Examples\n",
            "    --------\n",
            "    >>> pd.read_csv('data.csv')  # doctest: +SKIP\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o-thnccIWTvc",
        "colab_type": "code",
        "outputId": "57799072-a851-4d4f-fd37-e24f6997492b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 273
        }
      },
      "source": [
        "# Alright, we can pass header=None to fix this\n",
        "flag_data = pd.read_csv(flag_data_url, header=None)\n",
        "flag_data.head()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "      <th>3</th>\n",
              "      <th>4</th>\n",
              "      <th>5</th>\n",
              "      <th>6</th>\n",
              "      <th>7</th>\n",
              "      <th>8</th>\n",
              "      <th>9</th>\n",
              "      <th>...</th>\n",
              "      <th>20</th>\n",
              "      <th>21</th>\n",
              "      <th>22</th>\n",
              "      <th>23</th>\n",
              "      <th>24</th>\n",
              "      <th>25</th>\n",
              "      <th>26</th>\n",
              "      <th>27</th>\n",
              "      <th>28</th>\n",
              "      <th>29</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>648</td>\n",
              "      <td>16</td>\n",
              "      <td>10</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>5</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>black</td>\n",
              "      <td>green</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Albania</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>29</td>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>red</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Algeria</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>2388</td>\n",
              "      <td>20</td>\n",
              "      <td>8</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>green</td>\n",
              "      <td>white</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>American-Samoa</td>\n",
              "      <td>6</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>5</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>blue</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Andorra</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>blue</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 30 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "               0   1   2     3   4   5   6   7   8   9   ...    20  21  22  \\\n",
              "0     Afghanistan   5   1   648  16  10   2   0   3   5  ...     0   0   1   \n",
              "1         Albania   3   1    29   3   6   6   0   0   3  ...     0   0   1   \n",
              "2         Algeria   4   1  2388  20   8   2   2   0   3  ...     0   0   1   \n",
              "3  American-Samoa   6   3     0   0   1   1   0   0   5  ...     0   0   0   \n",
              "4         Andorra   3   1     0   0   6   0   3   0   3  ...     0   0   0   \n",
              "\n",
              "   23  24  25  26 27     28     29  \n",
              "0   0   0   1   0  0  black  green  \n",
              "1   0   0   0   1  0    red    red  \n",
              "2   1   0   0   0  0  green  white  \n",
              "3   0   1   1   1  0   blue    red  \n",
              "4   0   0   0   0  0   blue    red  \n",
              "\n",
              "[5 rows x 30 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iG9ZOkSMWZ6D",
        "colab_type": "code",
        "outputId": "d8b6f16a-6964-41f4-b438-9ddbff9eb08a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 555
        }
      },
      "source": [
        "flag_data.count()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     194\n",
              "1     194\n",
              "2     194\n",
              "3     194\n",
              "4     194\n",
              "5     194\n",
              "6     194\n",
              "7     194\n",
              "8     194\n",
              "9     194\n",
              "10    194\n",
              "11    194\n",
              "12    194\n",
              "13    194\n",
              "14    194\n",
              "15    194\n",
              "16    194\n",
              "17    194\n",
              "18    194\n",
              "19    194\n",
              "20    194\n",
              "21    194\n",
              "22    194\n",
              "23    194\n",
              "24    194\n",
              "25    194\n",
              "26    194\n",
              "27    194\n",
              "28    194\n",
              "29    194\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gMcxnWbkWla1",
        "colab_type": "code",
        "outputId": "52fc01aa-00bd-4420-8539-0fe7dba9e263",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 555
        }
      },
      "source": [
        "flag_data.isna().sum()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     0\n",
              "1     0\n",
              "2     0\n",
              "3     0\n",
              "4     0\n",
              "5     0\n",
              "6     0\n",
              "7     0\n",
              "8     0\n",
              "9     0\n",
              "10    0\n",
              "11    0\n",
              "12    0\n",
              "13    0\n",
              "14    0\n",
              "15    0\n",
              "16    0\n",
              "17    0\n",
              "18    0\n",
              "19    0\n",
              "20    0\n",
              "21    0\n",
              "22    0\n",
              "23    0\n",
              "24    0\n",
              "25    0\n",
              "26    0\n",
              "27    0\n",
              "28    0\n",
              "29    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AihdUkaDT8We",
        "colab_type": "text"
      },
      "source": [
        "### Yes, but what does it *mean*?\n",
        "\n",
        "This data is fairly nice - it was \"donated\" and is already \"clean\" (no missing values). But there are no variable names - so we have to look at the codebook (also from the site).\n",
        "\n",
        "```\n",
        "1. name: Name of the country concerned\n",
        "2. landmass: 1=N.America, 2=S.America, 3=Europe, 4=Africa, 4=Asia, 6=Oceania\n",
        "3. zone: Geographic quadrant, based on Greenwich and the Equator; 1=NE, 2=SE, 3=SW, 4=NW\n",
        "4. area: in thousands of square km\n",
        "5. population: in round millions\n",
        "6. language: 1=English, 2=Spanish, 3=French, 4=German, 5=Slavic, 6=Other Indo-European, 7=Chinese, 8=Arabic, 9=Japanese/Turkish/Finnish/Magyar, 10=Others\n",
        "7. religion: 0=Catholic, 1=Other Christian, 2=Muslim, 3=Buddhist, 4=Hindu, 5=Ethnic, 6=Marxist, 7=Others\n",
        "8. bars: Number of vertical bars in the flag\n",
        "9. stripes: Number of horizontal stripes in the flag\n",
        "10. colours: Number of different colours in the flag\n",
        "11. red: 0 if red absent, 1 if red present in the flag\n",
        "12. green: same for green\n",
        "13. blue: same for blue\n",
        "14. gold: same for gold (also yellow)\n",
        "15. white: same for white\n",
        "16. black: same for black\n",
        "17. orange: same for orange (also brown)\n",
        "18. mainhue: predominant colour in the flag (tie-breaks decided by taking the topmost hue, if that fails then the most central hue, and if that fails the leftmost hue)\n",
        "19. circles: Number of circles in the flag\n",
        "20. crosses: Number of (upright) crosses\n",
        "21. saltires: Number of diagonal crosses\n",
        "22. quarters: Number of quartered sections\n",
        "23. sunstars: Number of sun or star symbols\n",
        "24. crescent: 1 if a crescent moon symbol present, else 0\n",
        "25. triangle: 1 if any triangles present, 0 otherwise\n",
        "26. icon: 1 if an inanimate image present (e.g., a boat), otherwise 0\n",
        "27. animate: 1 if an animate image (e.g., an eagle, a tree, a human hand) present, 0 otherwise\n",
        "28. text: 1 if any letters or writing on the flag (e.g., a motto or slogan), 0 otherwise\n",
        "29. topleft: colour in the top-left corner (moving right to decide tie-breaks)\n",
        "30. botright: Colour in the bottom-left corner (moving left to decide tie-breaks)\n",
        "```\n",
        "\n",
        "Exercise - read the help for `read_csv` and figure out how to load the data with the above variable names. One pitfall to note - with `header=None` pandas generated variable names starting from 0, but the above list starts from 1..."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "okEjAUHwEZtE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XUgOnmc_0kCL",
        "colab_type": "text"
      },
      "source": [
        "## Steps of Loading and Exploring a Dataset:\n",
        "\n",
        "- Find a dataset that looks interesting\n",
        "- Learn what you can about it \n",
        " - What's in it? \n",
        " - How many rows and columns? \n",
        " - What types of variables?\n",
        "- Look at the raw contents of the file\n",
        "- Load it into your workspace (notebook)\n",
        " - Handle any challenges with headers\n",
        " - Handle any problems with missing values\n",
        "- Then you can start to explore the data\n",
        " - Look at the summary statistics\n",
        " - Look at counts of different categories\n",
        " - Make some plots to look at the distribution of the data"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "U8gXBy_NX_GY",
        "colab_type": "text"
      },
      "source": [
        "## 3 ways of loading a dataset"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EcOkhyxZYlN0",
        "colab_type": "text"
      },
      "source": [
        "### From its URL"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LGFEA44KYcBi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_3_po1C3Yo_s",
        "colab_type": "text"
      },
      "source": [
        "### From a local file"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kuZtM98oYcKX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Kxq5l_9CYrAI",
        "colab_type": "text"
      },
      "source": [
        "### Using the `!wget` command"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SZ_Tyt9NYcMr",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tmJSfyXJ1x6f",
        "colab_type": "text"
      },
      "source": [
        "# Part 2 - Deal with Missing Values"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bH46YMHEDzpD",
        "colab_type": "text"
      },
      "source": [
        "## Diagnose Missing Values\n",
        "\n",
        "Lets use the Adult Dataset from UCI. <https://github.com/ryanleeallred/datasets>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5ScSPPDbY_iX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SYK5vXqt7zp1",
        "colab_type": "text"
      },
      "source": [
        "## Fill Missing Values"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qzEunYExZAE3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CFnUMJy6Zbjc",
        "colab_type": "text"
      },
      "source": [
        "# Part 3 - Explore the Dataset:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rQIiPTZfZsqQ",
        "colab_type": "text"
      },
      "source": [
        "## Look at \"Summary Statistics"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SFIqoURnZ5jD",
        "colab_type": "text"
      },
      "source": [
        "### Numeric"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dlrSyfb8Z9-n",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qkJZBFBTZ7m3",
        "colab_type": "text"
      },
      "source": [
        "###Non-Numeric"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6LYDwJ62Z46o",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NhrQ0qWlZyzw",
        "colab_type": "text"
      },
      "source": [
        "## Look at Categorical Values"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aI2oN4kj1uVQ",
        "colab_type": "text"
      },
      "source": [
        "# Part 4 - Basic Visualizations (using the Pandas Library)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y2NB4XQwbuvB",
        "colab_type": "text"
      },
      "source": [
        "## Histogram"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qWIO8zuhArEr",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Pandas Histogram "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VBDMJsUQbxE9",
        "colab_type": "text"
      },
      "source": [
        "## Density Plot (KDE)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NyeZPpxRD1BA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Pandas Density Plot"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "54unTcvhb0u5",
        "colab_type": "text"
      },
      "source": [
        "## Scatter Plot"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zxEajNvjAvfB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Pandas Scatterplot"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}