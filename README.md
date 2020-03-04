# Rock, Paper, Scissors - Project

## Table of Contents

* [Introduction](#introduction)
* [App specifics](#app-specifics)
* [Prerequisites](#prerequisites)
* [Background](#background)
* [License and Attribution](#license-and-attribution)

## Introduction

This code runs a game of **Rock, Paper, Scissors**. The original [starter code](https://github.com/udacity/ipnd_rps_starter_code) was created by Udacity for a course project assessment.  The objective of this project from the student perspective, was to write further python code, to fulfil the additional Udacity requirements listed at the website link, in the [Background](#background) section.

## App specifics

The game has two players. In a single round of the game, each player secretly chooses one of three moves, or "throws" — rock, paper, or scissors. Then, players reveal their moves at the same time. If both players picked the same move, there is no winner. Otherwise, **rock beats scissors**; **paper beats rock**; and **scissors beat paper**.
Players can play a single round, or "best of x number of rounds".
You can configure the player types that you wish to use e.g. one of the _computer player_ types or _human player_, by editing _line 154_ in the `.py` file, as so e.g:
`game = Game(HumanPlayer(), CyclePlayer())`

## Prerequisites

To get started, ensure:
1. That you have **python version 3** installed. In a terminal, to check the version of Python you have type `python -V`.
Depending on your setup, if `python -V` shows a v2 version, instead type `python3 -V`.
If you don't have **python version 3** installed, navigate to Python's [website](https://www.python.org/) to download and install the software.
2. That you have the following project dependencies installed (attribution given in the `.py` file):
    * The 'colored' module from [PyPI](https://pypi.org/project/colored/#description)
    and thus can be installed via [pip](https://pypi.org/project/pip/) (package installer for python).
3. That you have downloaded the files from this github repo to a directory on your computer.
4. Then from a terminal application on your computer. Navigate to the directory where the python file is and input the following:
`python3 (filename).py`. Replacing `filename`, with the chosen name for the file downloaded.
    * Note -  For Windows systems, Python 3.x is installed as `python` by default.

## Background

To see the detail of the specific requirements that the project needed to meet, look at the project instructions on the [Udacity website](https://classroom.udacity.com/).

## License and Attribution

This project just added to the initial application builds from [Udacity's starter code GitHub repo](https://github.com/udacity/ipnd_rps_starter_code), so additional code is licensed under the same terms. See the **LICENSE file** for license rights and limitations.

Attribution for any project dependencies or reference resources used during this project, are detailed, either in the attribution section of the relevant .py files or the dependencies folder, within this project.
