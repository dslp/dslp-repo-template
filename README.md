# Data Science Lifecycle Base Repo

Use this repo as a template repository for data science projects using the Data Science Life Cycle Process. This repo is meant to serve as a launch off point. Our goal is to introduce only **minimum viable opinions** into the structure of this repo in order to make this repository/framework useful across a variety of data science projects and workflows. Therefore, we will tend to err to the side of omitting something if we're not confident that it's widely useful or think it's overly opinionated. That shouldn't stop you from forking this repo and adapting it to fit the needs of your project/team/organization.

With that in mind, if there is something that you think we're missing or should change, open an issue and we'll talk!

## Get started.

The only manual step required is that you have to manually create the labels. The label names, descriptions, and color codes can be found in the [.github/labels.yaml](/.github/labels.yaml) file. For more information on creating labels, review the GitHub docs [here](https://help.github.com/en/github/managing-your-work-on-github/creating-a-label).

## Contributing

Issues and suggestions for this template repo should be opened in the main [dslp repo](https://github.com/MicrosoftDSST/dslp/issues).

## Default Directory Structure

```
├── .cloud              # for storing cloud configuration files and templates (e.g. ARM, Terraform, etc)
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── Ask.md
│   │   ├── Data.Aquisition.md
│   │   ├── Data.Create.md
│   │   ├── Experiment.md
│   │   ├── Explore.md
│   │   └── Model.md
│   ├── labels.yaml
│   └── workflows
├── .gitignore
├── README.md
├── code
│   ├── datasets        # code for creating or getting datasets
│   ├── deployment      # code for deploying models
│   ├── features        # code for creating features
│   └── models          # code for building and training models
├── data                # directory is for consistent data placement. contents are gitignored by default.
│   ├── README.md
│   ├── interim         # storing intermediate results (mostly for debugging)
│   ├── processed       # storing transformed data used for reporting, modeling, etc
│   └── raw             # storing raw data to use as inputs to rest of pipeline
├── docs
│   ├── code            # documenting everything in the code directory (could be sphinx project for example)
│   ├── data            # documenting datasets, data profiles, behaviors, column definitions, etc
│   ├── media           # storing images, videos, etc, needed for docs.
│   ├── references      # for collecting and documenting external resources relevant to the project
│   └── solution_architecture.md    # describe and diagram solution design and architecture
├── environments
├── notebooks
├── pipelines           # for pipeline orchestrators i.e. AzureML Pipelines, Airflow, Luigi, etc.
├── setup.py            # if using python, for finding all the packages inside of code.
└── tests               # for testing your code, data, and outputs
    ├── data_validation
    └── unit
```