# Scatter Plot lab

This lab will introduce students to Jupyter Notebooks and ask students to collaborate as a group to create a scatter plotting program in a shared jupyter notebook.


## Jupyter notebooks setup (for Mac)
You can install Jupyter using pip in the Terminal:

    $ pip install --upgrade pip
    $ pip install --upgrade ipython jupyter jupytext pandas
    
Our class will work on .ipynb files locally while committing .Rmb files to github to avoid committing the output of notebooks (which causes huge diffs for small changes and makes mergining changes to notebooks ugly and difficult).

To configure your Jupyter hooks to sync .ipynb files with .Rmb files, use the following Terminal commands:

    $ jupyter notebook --generate-config
    $ printf 'c.NotebookApp.contents_manager_class="jupytext.TextFileContentsManager"
    c.ContentsManager.default_jupytext_formats = ".ipynb,.Rmd"' >> /Users/`whoami`/.jupyter/jupyter_notebook_config.py

Now, you're ready to easily use git for version control with Jupyter notebooks using the following workflow:

  * `clone` or `pull` the Jupyter notebook repo to your local directory
  * run `jupyter notebook` in your working directory
  * open the .Rmb file
  * Save `cmd+S` the file
  * Close and halt the .Rmb file
  * Open the .ipynb file and edit as usual (this will save the output as usual while automatically updating the .Rmb file)


## Jupyter notebooks setup (for WINDOWS)
You can install Jupyter using pip in the Terminal:

    $ sudo apt-get update
    $ sudo apt-get install python3-pip
    $ pip3 install --upgrade pip
    $ pip3 install --user jupyter
    $ pip3 install --upgrade --user ipython jupyter jupytext pandas
    $ vim ~/.bashrc
     
Inside bashrc, scroll to the very end of the document. Press `I`.
Then add: 

    alias jupyter-notebook="~/.local/bin/jupyter-notebook --no-browser"
    
Once completed, press `ESC` button. 
    
    $ source ~/.bashrc
    $ jupyter-notebook 
    
Our class will work on .ipynb files locally while committing .Rmb files to github to avoid committing the output of notebooks (which causes huge diffs for small changes and makes mergining changes to notebooks ugly and difficult).

To configure your Jupyter hooks to sync .ipynb files with .Rmb files, use the following Terminal commands:

    $ jupyter-notebook --generate-config
    
This should print out a path. Replace ****** with the path that was just printed out for this next command:
    
    $ printf 'c.NotebookApp.contents_manager_class="jupytext.TextFileContentsManager"
    c.ContentsManager.default_jupytext_formats = ".ipynb,.Rmd"' >> ******
    
Now, you're ready to easily use git for version control with Jupyter notebooks using the following workflow:

  * `git clone` or `git pull` the Jupyter notebook repo to your local directory
  * run `jupyter-notebook` in your working directory
  * open the .Rmb file
  * Save `cmd+S` the file
  * Close and halt the .Rmb file
  * Open the .ipynb file and edit as usual (this will save the output as usual while automatically updating the .Rmb file)
