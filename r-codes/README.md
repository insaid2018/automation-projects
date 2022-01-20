- All the projects based on R automation have been developed using Jupyter Notebooks.
- If you are not sure how to use R in Jupyter Notebook, follow the setup given below.

# Setup R Kernel in Jupyter Notebook

- Download R from here and install it in your system.

- After installing R, run the following command in R software to install essential libraries:

  ```
  install.packages(c(‘repr’, ‘IRdisplay’, ‘evaluate’, ‘crayon’, ‘pbdZMQ’, ‘devtools’, ‘uuid’, ‘digest’))
  install.packages(‘IRkernel’)
  ```

- To make Kernel available to Jupyter execute the following commands:

  ```
  IRkernel::installspec()
  OR IRkernel::installspec(user = FALSE) #install system-wide
  ```
  
- Open a notebook and open a new R script.
