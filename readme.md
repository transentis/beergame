# Having Fun With the Beer Distribution Game
## Computational notebooks, System Dynamics and Agent-based Simulations and AI Training Algorithms

The Beer Game was developed in the 1960s at MIT to illustrate how difficult it is to manage dynamic systems – in this case a supply chain that delivers beer from a brewery to the end consumer.

This repository contains computational notebooks, simulation models and AI training algorithms that explore the game in depth.

Please read the companion blog posts on our [website](https://www.transentis.com/case-study-play-the-beer-game/en/).

Have a go at playing the Beer Game (on your own or – much more fun – in a group) before you read the notebooks:

You can play the online alone or in a group on our [website](https://www.transentis.com/case-study-play-the-beer-game/en/). 

The notebooks use the [BPTK-Py package](https://www.transentis.com/business-prototyping-toolkit/en/), which provides System Dynamics and Agent-based modeling in Python.

## Repository Contents

### Notebooks

This repository contains a number of Jupyter notebooks. The key ones are:

* __[Understanding the Beer Game](understanding_the_beergame.ipynb).__ This is the best place to get started - play the Beer Game in single player mode and learn about the dynamics governing the game. This version uses a SD DSL implementation of the Beer Game.
* __[Simulating the Beer Game](beergame_sd_dsl.ipynb)__ This notebook introduces a stock and flow model for the Beer Game and discusses an implementation of that model using the SD DSL.
* __[An Agent-based Approach To Modeling the Beer Game](beergame_abm.ipynb).__ An agent-based simulation of the Beer Game that can be used to test policies. It is also used as the basis for the reinforcement learning apporach described in the notebook [Training AI to play the Beer Game](training_ai_beergame.ipynb)
* __[Training AI to play the Beer Game – A Reinforcement Learning Approach](training_ai_beergame.ipynb).__ This notebook introduces the concept of reinforcement learning and then applies it to training intelligent agents to play the Beer Game.

### Models

This repository contains three simulation models of the Beer Game:

* One version of the Beer Game model built in Python using the SD DSL provided by BPTK. This version is used in the [Understanding the Beer Game](understanding_the_beergame.ipynb) notebook and is discussed in detail in the [Simulating the Beer Game](beergame_sd_dsl.ipynb) notebook. The code for this version can be found in the _src/sd_dsl_ directory.
* One version of the Beer Game model built using Stella Architect and then utilizing the XMILE transpiler that is part of BPTK. The Stella model can be found in the _simulation_models_ directory. This version of the simulation is used in the [Understanding the Beer Game (XMILE)](understanding_the_beergame_xmile.ipynb) notebook.
* One built using the Agent-based modeling framework that is part of BPTK-Py. The ABM version can be found in the  _src/abm_ directory.  This version is is used in the [An Agent-based Approach To Modeling the Beer Game](beergame_abm.ipynb) and [Training AI to Play The Beer Game](training_ai_beergame.ipynb) notebooks.

Both SD models produce identical results.

## Installation And Testing Instructions

### Using Docker

If you have Docker installed (e.g. Docker Desktop on MacOS or on Windows), follow these steps:

1. Clone this repo in a directory of your choice: `git clone`
2. Run ```docker-compose up```
3. Point your browser at [http://localhost:8888](http://localhost:8888) – this will open JupyterLab showing a directory `work` in the file browser. This directory contains your working directory.
4. Open the readme file ```work/readme.md``` from within JupyterLab.
5. When you are finished, close your browser and call ```docker-compose down``` from within your directory. This will stop and remove the container.

### Installing using a Python virtual environment

Alternatively you can install using a Python virtual environment:

1. Clone this repo in a directory of your choice: `git clone`
2. Make sure you have python3 installed
2. Change into the repo and setup a python venv: `python3 -m venv venv`
3. Activate the venv: `source venv/bin/activate`
4. Install the required modules: `pip install -r requirements.txt`
5. Install the jupyter lab widgets: `jupyter labextension install @jupyter-widgets/jupyterlab-manager`
6. Start jupyter lab: `jupyter lab`

### Testing Your Installation

Once you have installed, to make sure everything is working open the notebook [beergame_abm.ipynb](beergame_abm.ipynb) and run all the cells - there should be no error messages and the last graph should look like the one below.

![Notebook Screenshot](beergame_screenshot.png)

If you have any questions, let us know via email to [support@transentis.com](mailto://support@transentis.com).

## Further Reading

You can find extensive [documentation](https://bptk.transentis.com) online and advanced tutorials and examples on [GitHub](https://github.com/transentis/bptk_py_tutorial).

You can also find more Jupyter notebooks and simulation models on GitHub:

* [Introduction to BPTK](https://github.com/transentis/bptk_intro). Introductory notebooks and dashboards to get you started with BPTK.
* [COVID Simulation](https://github.com/transentis/sim-covid-19). Jupyter notebooks and dashboards illustrating the SIR model.
* [COVID Simulation Dashboard](https://github.com/transentis/sim-covid-dashboard). A web-based simulation dashboard for the COVID simulation built using our BPTK Widgets library for Javascript. View a [live version](http://www.covid-sim.com) of the dashboard online.
