![travisCI](https://travis-ci.org/brennan-v-/flaskr-dataset.svg) [![codecov.io](https://codecov.io/github/brennan-v-/flaskr-dataset/coverage.svg?branch=master)](https://codecov.io/github/brennan-v-/flaskr-dataset?branch=master)
 ![pythons](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5%2C%203.5--dev-blue.svg)

                         / flaskr-dataset /

                 a minimal blog application


    ~ What is flaskr-dataset?

      A Dataset powered thumble blog application

    ~ How do I use it?

      1. clone the repo and step into it

          git clone git@github.com:brennan-v-/flaskr-dataset.git
          cd flaskr-dataset

      2. create a virtual environment and install packages

          virtualenv venv
          source venv/bin/activate

          pip install -r requirements.txt

            or
            
          pip install flask
          pip install dataset

      3. start the application

          python flaskr.py

         the application will greet you on
         http://localhost:5000/

    ~ Attributions:

[mitsuhiko/flask/examples/flaskr](https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/)
      
[pudo/dataset](https://github.com/pudo/dataset)
