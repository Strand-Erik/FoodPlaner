# FoodPlanner

FoodPlanner is an application designed to simplify your meal planning process. By allowing you to add recipes, it automatically generates a grocery list based on the ingredients required for those recipes.

## Installation and Setup

### Prerequisites

Before running the application, you need to install all the dependencies. This can easily be done by executing the environment initialization script provided:

```bash
./init_env.sh
```

## Running the Application

Once all dependencies have been installed, start the application by running:

```bash
./app.py
```

## Troubleshooting

### Common Issues and Solutions

- **Issue**: `ModuleNotFoundError: No module named 'tkinter'`

    **Solution**: This error typically means that tkinter is not included in your base Python installation. You can install tkinter using the following command:

    For Debian/Ubuntu-based systems:
    ```bash
    sudo apt-get install python3-tk
    ```