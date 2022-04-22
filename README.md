# A shallow deep dive of SQL Alchemy

This repository is a bottom-up walkthrough of the layers that make up SQL Alchemy - open-source **SQL toolkit** ***and*** **object-relational mapper** for python.

The notebooks in this repository are supposed to show side-by-side comparisons of 3 different layers of sqlalchemy to provide a better understanding of how/why.

Many times, new developers approach SQL Alchemy as an ORM only and typically in a larger project where it's easy to overlook a lot of the nuances inside of the library - here I want to flip the script and go bottom-up working our way up to the ORM.

> Note: this repository was used as supporting material for a talk 

## Setup
1. Install VS Code.

2. Install the [Remote Containers extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). This allows you to open this project into a bootstrapped docker container inside of VS Code with all dependencies, extensions, etc. installed and manged for you.

3. Open this project in VS Code - a dialog box should appear recognizing that this folder contains a Dev Container configuration file and asking if you would like to reopen the project in the container - select **Reopn in Container**. 

4. Wait a few minutes as everything gets setup.

5. Open the *.ipynb files in VS Code
    * note there's an extension pre-installed for you to view the postgres database that gets automatically setup
